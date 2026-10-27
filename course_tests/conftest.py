"""Lets `pytest` find the `server` package from any folder of your repository."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
