pkgname=layout-tui
  pkgver=1.0.0
  pkgrel=1
  pkgdesc="Flexible Layout Generator in TUI format"
  arch=('any')
  url="https://github.com/you/layout-tui"
  license=('GPL-3.0-only')
  depends=('python' 'uv')
  makedepends=('python-build' 'python-pip')
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