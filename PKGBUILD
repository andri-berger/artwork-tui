pkgname=artwork-tui
pkgver=0.0.1
pkgrel=1
arch=('any')
pkgdesc="Flexible Artwork Generator in TUI format"
url="https://github.com/andri-berger/artwork-tui"
makedepends=('python-build' 'python-pip')
depends=('python-playwright' 'chromium')
# depends=('python' 'uv')
license=('GPL-3.0-only')
  source=("${pkgname}-${pkgver}.tar.gz::https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('abc123...')
depends=(
    'gmic'
    'opencv'
    'vtracer'
    'python-numpy'
    'python-pillow'
    'python-opencv'
    'python-playwright'
    'python-platformdirs'
    'python-textual-fspicker'
    'python-textual-image'
    'python-textual'
    'python-vtracer'
)



  build() {
      cd "$srcdir/${pkgname}-${pkgver}"
      uv build --wheel
  }

  package() {
      cd "$srcdir/${pkgname}-${pkgver}"
      pip install \
          --root="$pkgdir" \
          --prefix=/usr \
          --no-deps \
          dist/*.whl
  }
