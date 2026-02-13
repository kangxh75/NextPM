#!/usr/bin/env python3
"""
Build wrapper that runs build-specs.py before building the site.
Usage: python scripts/build.py [additional mkdocs build arguments]
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    # Change to project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)

    print("Building specifications...")
    try:
        # Run build-specs.py
        result = subprocess.run([sys.executable, "scripts/build-specs.py"], check=True)
        print("Specifications built successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build specifications: {e}")
        sys.exit(1)

    print("\nBuilding MkDocs site...")
    # Build mkdocs with any additional arguments passed to this script
    mkdocs_args = ["mkdocs", "build"] + sys.argv[1:]

    try:
        result = subprocess.run(mkdocs_args, check=True)
        print("Site built successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build site: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()