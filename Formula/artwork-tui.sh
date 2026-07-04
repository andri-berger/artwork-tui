#!/usr/bin/env sh
# artwork-tui.sh — run from the artwork-tui repo root after tag+push

# sudo chown -R admin /opt/brew
# sudo rm -rf /opt/brew
#NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"   # replace the /opt/brew line in your rc
#echo >> /home/admin/.zshrc
#echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv zsh)"' >> /home/admin/.zshrc
#eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv zsh)"
set -e

APP="artwork-tui"
FORMULA="Formula/${APP}.rb"
DEV_TAP="andri-berger/dev"
DEV_TAP_DIR="$(brew --repository)/Library/Taps/andri-berger/homebrew-dev"

# 00 AUR Preparation
# updpkgsums && makepkg --printsrcinfo > .SRCINFO

# 0. tag: explicit argument wins; otherwise newest version tag
TAG=${1:-$(git tag --list 'v*' --sort=-version:refname | head -1)}
[ -n "$TAG" ] || { echo "no version tag found" >&2; exit 1; }

sed -i "s|\.git@v[0-9.]*|.git@${TAG}|" install.sh
grep -q "@${TAG}" install.sh || { echo "install.sh ref not updated" >&2; exit 1; }
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


#1. AUR account → aur.archlinux.org, register. One account serves all your packages, forever.
#2. Dedicated SSH keypair (asymmetric, per the security-model discussion):
#shssh-keygen -t ed25519 -f ~/.ssh/aur -C "aur"
#Paste the .pub contents into your AUR profile ("My Account" → SSH Public Key), then wire the host in ~/.ssh/config:
#Host aur.archlinux.org
#    IdentityFile ~/.ssh/aur
#    User aur
#Verify: ssh aur.archlinux.org should greet you by username and disconnect.
#3. Final local liturgy (in the repo's packaging dir, tag v0.1.0 already pushed to GitHub):
#shmakepkg -si                                    # cold build + install: the user's exact path
#artwork-tui                                    # launch — the artifact, not the checkout
#namcap PKGBUILD && namcap *.pkg.tar.zst        # static audit
#makepkg --printsrcinfo | diff - .SRCINFO       # derived file matches source — must be empty
#4. Clone your (not-yet-existing) AUR repo — the create-by-push flow:
#shgit clone ssh://aur@aur.archlinux.org/artwork-tui.git   # warns "empty repository" — correct
#That clone claims nothing yet; the name registers on first push.
#5. Populate with exactly the publication set — PKGBUILD, .SRCINFO, artwork-tui.install (filterx: just the first two) — no source code, no tarballs, no makepkg debris:
#shcp PKGBUILD .SRCINFO artwork-tui.install path/to/aur-clone/
#cd path/to/aur-clone
#git add -A && git commit -m "initial release: v0.1.0"
#6. Push = publish:
#shgit push origin master     # note: AUR uses master, not main
#The package page exists the moment this lands; search indexes it immediately.
#7. Verify the delivered path as a stranger — page renders at aur.archlinux.org/packages/artwork-tui (deps, version, pkgdesc all from .SRCINFO), then the canary's inauguration:
#shsudo pacman -R artwork-tui        # remove the step-3 copy
#yay -S artwork-tui                # full pipeline: RPC → clone → review → build → install
#This is the one test step 3 couldn't perform — the AUR's own delivery layer.
#8. Repeat 4–7 for filterx-tui, then let both soak until launch day — obscurity with a doorbell, early comments welcome.
#Thereafter, each release appends the AUR chapter to the ritual: bump pkgver, reset pkgrel=1, updpkgsums, regenerate .SRCINFO, commit both atomically, push