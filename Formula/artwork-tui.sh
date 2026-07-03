#!/usr/bin/env sh
# release-formula.sh — run from the artwork-tui repo root after tag+push
set -e

FORMULA="Formula/artwork-tui.rb"
DEV_TAP="andri-berger/dev"
DEV_TAP_DIR="$(brew --repository)/Library/Taps/andri-berger/homebrew-dev"

# 0. url + sha derived from the newest tag
TAG=$(git describe --tags --abbrev=0)
SHA=$(curl -sL "https://github.com/andri-berger/artwork-tui/archive/refs/tags/${TAG}.tar.gz" \
      | sha256sum | cut -d' ' -f1)
sed -i "s|archive/v[0-9.]*\.tar\.gz|archive/${TAG}.tar.gz|" "$FORMULA"
sed -i "s/^\(\s*sha256 \)\"[a-f0-9]*\"/\1\"${SHA}\"/" "$FORMULA"

# 1. playwright pin derived from uv.lock
PW_VERSION=$(uv export --no-dev --no-emit-project --no-hashes \
             | grep '^playwright==' | cut -d'=' -f3)
[ -n "$PW_VERSION" ] || { echo "playwright not found in lock" >&2; exit 1; }
sed -i "s/pip_install \"playwright==[0-9.]*\"/pip_install \"playwright==${PW_VERSION}\"/" "$FORMULA"

# 2. scratch-tap dev harness (idempotent: created once, verified thereafter)
brew tap | grep -qx "$DEV_TAP" || brew tap-new "$DEV_TAP"
[ -e "$DEV_TAP_DIR/Formula/artwork-tui.rb" ] || \
    ln -s "$PWD/$FORMULA" "$DEV_TAP_DIR/Formula/artwork-tui.rb"
[ -L "$DEV_TAP_DIR/Formula/artwork-tui.rb" ] || {
    echo "warning: tap copy is a real file, not a symlink — two truths!" >&2; exit 1; }

# 3. regenerate the resource blocks (via the scratch-tap name)
brew update-python-resources \
    --exclude-packages playwright,pillow,numpy,opencv-python artwork-tui

# 4. show what changed, leave the commit to you
git diff --stat "$FORMULA"
echo "review with: git diff Formula/ — then commit & push"
