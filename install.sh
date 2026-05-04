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
# playwright install chromium --with-deps

# install chromium via playwright
OS=$(uname -s)
if [ "$OS" = "Linux" ]; then
    playwright install chromium --with-deps
elif [ "$OS" = "Darwin" ]; then
    playwright install chromium
else
    echo "unsupported OS: $OS — install Chromium manually via: playwright install chromium"
fi

echo "done — run: artwork-tui"
echo "if command not found, add to your shell config: export PATH=\"\$HOME/.local/bin:\$PATH\""
