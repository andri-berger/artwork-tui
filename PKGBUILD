pkgname=artwork-tui
pkgver=0.0.1
pkgrel=1
arch=('x86_64')
license=('GPL-3.0-only')
provides=('artwork-tui')
conflicts=('artwork-tui')
pkgdesc="Flexible Artwork Generator in TUI format"
url="https://github.com/andri-berger/artwork-tui"  source=("https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('10790e80a965d21087a53c40286817f7f7835356d917c2bce1c152dc004edcab')
makedepends=('python-build' 'python-installer' 'python-wheel')
depends=(
    'python-numpy'
    'python-pillow'
    'python-playwright'
    'python-platformdirs'
    'python-textual-image'
    'python-textual'
    'python-wand'
    'imagemagick'
    'opencv-python'
    'opencv'
)

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

  # post_install() {
  #   echo ""
  #   echo "==> artwork-tui requires Playwright's Chromium browser."
  #   echo "==> If not already installed, run as your normal user:"
  #   echo ""
  #   echo "    playwright install chromium --with-deps"
  #   echo ""
  #   if ! find ~/.cache/ms-playwright -name 'chrome' 2>/dev/null | grep -q .; then
  #       echo "==> WARNING: Chromium not detected — app will fail without it."
  #   fi
  # }

  # post_install() {
  #   echo ""
  #   echo "╔════════════════════════════════════════════════╗"
  #   echo "║           artwork-tui — post install           ║"
  #   echo "╚════════════════════════════════════════════════╝"
  #   echo ""
  #   echo " Chromium is required but must be installed as"
  #   echo " your normal user (not root). Run:"
  #   echo ""
  #   echo "   playwright install chromium --with-deps"
  #   echo ""
  #   echo " artwork-tui will not function without this step."
  #   echo ""
  # }

  # post_upgrade() {
  #   post_install
  # }
