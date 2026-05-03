"""Run this script whenever you add a new day folder: python generate_pyrightconfig.py"""
import json
import os

src = os.path.join(os.path.dirname(__file__), "src")

extra_paths = []
for dirpath, dirnames, filenames in os.walk(src):
    if any(f.endswith(".py") for f in filenames):
        rel = os.path.relpath(dirpath, os.path.dirname(__file__)).replace("\\", "/")
        extra_paths.append(rel)

config = {
    "extraPaths": extra_paths
}

out = os.path.join(os.path.dirname(__file__), "pyrightconfig.json")
with open(out, "w") as f:
    json.dump(config, f, indent=2)

print(f"Updated pyrightconfig.json with {len(extra_paths)} path(s):")
for p in extra_paths:
    print(f"  {p}")
