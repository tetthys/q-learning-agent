#!/usr/bin/env bash
# Execute pytest inside container
# English comments only.

set -euo pipefail

echo "[container] Running Python tests..."
pytest tests -vv
