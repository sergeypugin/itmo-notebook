#!/usr/bin/env python3
"""Compatibility entry point; use scripts/main.py for normalization."""
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import main as canonical_main


def main(argv=None):
    return canonical_main.main(argv)


if __name__ == "__main__":
    sys.exit(main())
