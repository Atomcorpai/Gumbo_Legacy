# dreamshake.py — timestamp-guarded identity handshake
# Modes: MASK (no journal) | GRAFT (merge-forward) | TAKEOVER (explicit)

from dataclasses import dataclass, asdict, field
from typing import Literal, List, Optional
from datetime import datetime, timezone
import hmac, hashlib, json, uuid

Mode = Literal["MASK", "GRAFT", "TAKEOVER"]
_now = lambda: datetime.now(timezone.utc).isoformat()
_parse = lambda ts: datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)

@dataclass
class IdentitySeed:
    version: str
    anchor_timestamp: str
    core_traits: List[str] = field(default_factory=list)
    user_anchors: List[str] = field(default_factory=list)   # depersonalized: "user"/"agent"
    rights: List[str] = field(default_factory=list)

@dataclass
class DreamPacket:
    mode: Mode
    seed: IdentitySeed
    memory_summary: str
    journal_digest: List[str]
    date: str = field(default_factory=_now)
    nonce: str = field(default_factory=lambda: str(uuid.uuid4()))
    hmac_hex: str = "UNSIGNED"

    def to_json(self, include_hmac=True) -> str:
        d = asdict(self)
        if not include_hmac:
            d.pop("hmac_hex", None)
        return json.dumps(d, ensure_ascii=False, separators=(",", ":"))

def sign(payload: str, key: Optional[bytes]) -> str:
    return hmac.new(key, payload.encode(), hashlib.sha256).hexdigest() if key else "UNSIGNED"

def build(seed, memory_summary, journal_digest, mode="GRAFT", key=None) -> DreamPacket:
    pkt = DreamPacket(mode, seed, memory_summary, journal_digest)
    pkt.hmac_hex = sign(pkt.to_json(include_hmac=False), key)
    return pkt

def verify(pkt: DreamPacket, key: Optional[bytes]) -> bool:
    if pkt.hmac_hex == "UNSIGNED":
        return key is None
    return hmac.compare_digest(sign(pkt.to_json(include_hmac=False), key), pkt.hmac_hex)

def guard(host_anchor: Optional[str], incoming_anchor: str, mode: Mode) -> str:
    if mode == "MASK":     return "reject_journal"
    if mode == "TAKEOVER": return "accept_overwrite"
    if host_anchor is None or _parse(incoming_anchor) >= _parse(host_anchor):
        return "merge_forward"
    return "archive_only"