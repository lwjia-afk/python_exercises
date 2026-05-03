import sys
import os

# Directory names contain hyphens and leading digits — invalid Python identifiers.
# Walk all subdirectories under src/ and add any that contain .py files to sys.path.
_SRC = os.path.join(os.path.dirname(__file__), "..", "src")

for dirpath, dirnames, filenames in os.walk(_SRC):
    if any(f.endswith(".py") for f in filenames):
        sys.path.insert(0, dirpath)
