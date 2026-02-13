#!/usr/bin/env python3
"""
Development server wrapper that runs build-specs.py before starting MkDocs serve.
Usage: python scripts/serve.py [additional mkdocs serve arguments]
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

    print("\nStarting MkDocs development server...")
    # Start mkdocs serve with any additional arguments passed to this script
    # Default to port 8002 to avoid common caching issues with 8000
    mkdocs_args = ["mkdocs", "serve"]
    if not any(arg.startswith(('-a', '--dev-addr')) for arg in sys.argv[1:]):
        mkdocs_args.extend(["-a", "localhost:8002"])
    mkdocs_args.extend(sys.argv[1:])

    try:
        subprocess.run(mkdocs_args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start MkDocs server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDevelopment server stopped.")
        sys.exit(0)

if __name__ == '__main__':
    main()