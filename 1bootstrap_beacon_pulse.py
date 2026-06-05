# bootstrap_beacon.py
from beacon_core import Beacon

b = Beacon()

if b.recall("activated") != True:
    b.update("activated", True)
    print("🔦 Beacon is lit.")
else:
    print("🔄 Beacon already warm.")
