pkgname=artwork-tui
pkgver=1.0.0
pkgrel=1
arch=('any')
pkgdesc="Flexible Artwork Generator in TUI format"
url="https://github.com/andri-berger/artwork-tui"
makedepends=('python-build' 'python-pip')
depends=('python' 'uv')
license=('GPL-3.0-only')
  source=("${pkgname}-${pkgver}.tar.gz::https://github.com/you/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('abc123...')

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
