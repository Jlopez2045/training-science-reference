#!/usr/bin/env bash
# Rebuild muscle-technique.pdf with working internal links.
# Obsidian's own PDF export drops same-file anchors; this route keeps them.
set -euo pipefail
cd "$(dirname "$0")"
python3 md2pdf-html.py muscle-technique.md /tmp/muscle-technique.html
google-chrome-stable --headless=new --disable-gpu --no-sandbox \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw \
  --virtual-time-budget=120000 \
  --print-to-pdf=muscle-technique.pdf "file:///tmp/muscle-technique.html"
echo "muscle-technique.pdf rebuilt"
