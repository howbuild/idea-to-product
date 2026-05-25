#!/usr/bin/env sh
set -eu

PYTHON_BIN="${PYTHON_BIN:-python3}"

"$PYTHON_BIN" scripts/validate-manifests.py
"$PYTHON_BIN" scripts/validate-python-hooks.py
"$PYTHON_BIN" plugins/idea-to-product/hooks/output-validator.py --manifest
