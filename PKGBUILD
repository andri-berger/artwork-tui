pkgrel=1
pkgver=1.0.0
arch=('any')
pkgname=artwork-tui
license=('GPL-3.0-only')
pkgdesc='Flexible Artwork Generator in TUI format'
url='https://github.com/andri-berger/artwork-tui'
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('e36ede2cefea1fa889311b82d64f35b96e1b39a01a733529d8cd40f98ae6f163')
makedepends=(
    'python-hatchling'
    'python-installer'
    'python-build'
    'python-wheel')
depends=(
    'python-textual-image'
    'python-platformdirs'
    'python-playwright'
    'python-textual'
    'python-opencv'
    'python-numpy'
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

