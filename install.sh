#!/usr/bin/env sh

if ! command -v uv >/dev/null 2>&1; then
    echo "installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "uv already installed, skipping"
fi

uv tool install git+https://github.com/andri-berger/artwork-tui.git --quiet --group main
# uv tool run playwright install chromium --with-deps
playwright install chromium --with-deps

echo "done — run: artwork-tui"
echo "if command not found, add to your shell config: export PATH=\"\$HOME/.local/bin:\$PATH\""
