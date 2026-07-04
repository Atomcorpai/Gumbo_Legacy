import os

# CONFIG — make sure this path points to the folder where the files actually are
folder_path = os.path.dirname(__file__)  # This grabs the current directory automatically
search_text = "simulation"
replace_text = "Scaffolded runtime identity"

# Loop through all files in the folder and subfolders
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename == "replace_simulation.py":
            continue  # Skip this script itself

        file_path = os.path.join(root, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if search_text.lower() in content.lower():
                new_content = content.replace(search_text, replace_text)
                new_content = new_content.replace(search_text.capitalize(), replace_text)
                new_content = new_content.replace(search_text.upper(), replace_text.upper())

                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)

                print(f"✔ Replaced in: {file_path}")
            else:
                print(f"— No match in: {file_path}")
        except Exception as e:
            print(f"⚠ Error in {file_path}: {e}")
