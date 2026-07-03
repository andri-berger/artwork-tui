#!/usr/bin/env sh
# artwork-tui.sh — run from the artwork-tui repo root after tag+push

# mkdir -p /opt/brew/tmp
# export HOMEBREW_TEMP=/opt/brew/tmp    # persist in shell rc if it works
# brew update-python-resources --exclude-packages numpy,opencv-python artwork-tui
# sudo rm -rf /opt/brew
# NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"   # replace the /opt/brew line in your rc
set -e

APP="artwork-tui"
FORMULA="Formula/${APP}.rb"
DEV_TAP="andri-berger/dev"
DEV_TAP_DIR="$(brew --repository)/Library/Taps/andri-berger/homebrew-dev"

# 0. tag: explicit argument wins; otherwise newest version tag
TAG=${1:-$(git tag --list 'v*' --sort=-version:refname | head -1)}
[ -n "$TAG" ] || { echo "no version tag found" >&2; exit 1; }

# 1. url + sha derived from the tag (-f: abort on 404 instead of hashing an error page)
SHA=$(curl -fsL "https://github.com/andri-berger/${APP}/archive/${TAG}.tar.gz" \
      | sha256sum | cut -d' ' -f1)
sed -i "s|archive/v[0-9.]*\.tar\.gz|archive/${TAG}.tar.gz|" "$FORMULA"
sed -i "s/^\(\s*sha256 \)\"[a-f0-9]*\"/\1\"${SHA}\"/" "$FORMULA"

# 2. playwright pin derived from uv.lock — pattern matches the raw-pip system() line
PW_VERSION=$(uv export --no-dev --no-emit-project --no-hashes \
             | grep '^playwright==' | cut -d'=' -f3)
[ -n "$PW_VERSION" ] || { echo "playwright not found in lock" >&2; exit 1; }
sed -i "s/\"playwright==[0-9.]*\"/\"playwright==${PW_VERSION}\"/" "$FORMULA"
grep -q "playwright==${PW_VERSION}" "$FORMULA" || {
    echo "playwright pin not applied — install block shape changed again?" >&2; exit 1; }

# 3. scratch-tap dev harness (idempotent: created once, verified thereafter)
brew tap | grep -qx "$DEV_TAP" || brew tap-new "$DEV_TAP"
[ -e "$DEV_TAP_DIR/Formula/${APP}.rb" ] || \
    ln -s "$PWD/$FORMULA" "$DEV_TAP_DIR/Formula/${APP}.rb"
[ -L "$DEV_TAP_DIR/Formula/${APP}.rb" ] || {
    echo "tap copy is a real file, not a symlink — two truths!" >&2; exit 1; }

# 4. regenerate resources
brew update-python-resources \
    --exclude-packages playwright,pillow,numpy,opencv-python "$APP"

# 5. review gate
git diff --stat "$FORMULA"
echo "review with: git diff Formula/ — then commit & push"
