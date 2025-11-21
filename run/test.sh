#!/usr/bin/env bash
# Run Python tests inside Docker container from host
# English comments only.

set -euo pipefail

# Build image if needed
echo "[host] Building test-runner image..."
docker compose build test-runner

# Run tests in container
echo "[host] Running tests inside Docker..."
docker compose run --rm test-runner
