pkgrel=1
pkgver=0.1.0
arch=('any')
pkgname=artwork-tui
license=('GPL-3.0-only')
pkgdesc='Flexible Artwork Generator in TUI format'
url='https://github.com/andri-berger/artwork-tui'
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('3bac49928120cc6df2528723fa4220b8c6e6cc93f36e7f67b8b55fe4252ecea7')
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

