#!/usr/bin/env sh

if ! command -v uv >/dev/null 2>&1; then
    echo "installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "uv already installed, skipping"
fi

uv tool install git+https://github.com/andri-berger/artwork-tui.git --quiet
PW="$(uv tool dir)/artwork-tui/bin/playwright"
if [ ! -x "$PW" ]; then
    echo "error: playwright not found in artwork-tui environment" >&2
    exit 1
fi

OS=$(uname -s)
if [ "$OS" = "Linux" ]; then
    if command -v apt-get >/dev/null 2>&1; then
        "$PW" install chromium --with-deps
    else
        echo "note: non-apt distro detected — installing browser only."
        echo "      system libraries must come from your distro's package manager."
        "$PW" install chromium
    fi
elif [ "$OS" = "Darwin" ]; then
    "$PW" install chromium
else
    echo "unsupported OS: $OS — install Chromium manually via: playwright install chromium"
fi

echo "done — run: artwork-tui"
echo "if command not found, add to your shell config: export PATH=\"\$HOME/.local/bin:\$PATH\""

