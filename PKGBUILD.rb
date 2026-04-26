  class LayoutTui < Formula
    include Language::Python::Virtualenv

    desc "Flexible Layout Generator in TUI format"
    homepage "https://github.com/you/layout-tui"
    url "https://github.com/you/layout-tui/archive/refs/tags/v1.0.0.tar.gz"
    sha256 "abc123..."
    license "AGPL-3.0-only"

    depends_on "python@3.14"

    # each PyPI dependency listed as resource
    # brew audit enforces this
    resource "textual" do
      url "https://files.pythonhosted.org/packages/.../textual-x.x.x.tar.gz"
      sha256 "..."
    end

    resource "pillow" do
      url "https://files.pythonhosted.org/packages/.../Pillow-x.x.x.tar.gz"
      sha256 "..."
    end

    # ... all dependencies from pyproject.toml

    def install
      virtualenv_install_with_resources
    end

    test do
      system bin/"layout-tui", "--version"
    end
  end


  # generates resource blocks from PyPI
  brew install pipgrip