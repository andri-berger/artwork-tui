class Tap < Formula
  include Language::Python::Virtualenv

  license "GPL-3.0-only"
  desc "Flexible Artwork Generator in TUI format"
  homepage "https://github.com/andri-berger/artwork-tui"
  url "https://github.com/andri-berger/artwork-tui/archive/v0.0.1.tar.gz"
  sha256 "10790e80a965d21087a53c40286817f7f7835356d917c2bce1c152dc004edcab"
  depends_on "python@3.14"
  depends_on "imagemagick"


  resource "wand" do
      url "https://files.pythonhosted.org/packages/c5/f6/feb40fadb7f3a6c5d45c02840c329725f6ec907eb3581c5de27445700e8a/wand-0.7.0.tar.gz"
      sha256 "e48f983cc248c23f752e5ba8a6aa1b09370c87d81425d2cc7474f4536c0740f9"
    end
  
  resource "platformdirs" do
    url "https://files.pythonhosted.org/packages/9f/4a/0883b8e3802965322523f0b200ecf33d31f10991d0401162f4b23c698b42/platformdirs-4.9.6.tar.gz"
    sha256 "3bfa75b0ad0db84096ae777218481852c0ebc6c727b3168c1b9e0118e458cf0a"
  end

  resource "textual-image" do
    url "https://files.pythonhosted.org/packages/c2/e7/c82ea0604874b6d51d5717a0911061ae5810e36dad2e4d2b11fa7d54cdaa/textual_image-0.12.0.tar.gz"
    sha256 "fdd0b5ff9c8a99740bc360a99ce014d563fa97d07a5b49b472470809f57c0a74"
  end

  resource "textual" do
    url "https://files.pythonhosted.org/packages/62/1e/1eedc5bac184d00aaa5f9a99095f7e266af3ec46fa926c1051be5d358da1/textual-8.2.5.tar.gz"
    sha256 "6c894e65a879dadb4f6cf46ddcfedb0173ff7e0cb1fe605ff7b357a597bdbc90"
  end
  
  on_arm do
    resource "playwright" do
      url "https://files.pythonhosted.org/packages/08/71/5e4d98b2ce3641b4343623c6450ff33b9de1c979d12a957505e392338b07/playwright-1.59.0-py3-none-macosx_11_0_arm64.whl"
      sha256 "af068143a0c045ec11608b67d6c42e58db7e9cf65a742dd21fddedc1a9802c47"
    end
  end

  on_intel do
    resource "playwright" do
      url "https://files.pythonhosted.org/packages/5b/48/abab23f40643b4de8f2665816f0a1bf0994eeecda39d6d62f0f292b2ad01/playwright-1.59.0-py3-none-macosx_10_13_x86_64.whl"
      sha256 "bfc6940100b57423175c819ce2422ec5880d55fa2769987f62ab7a1f5fe6783e"
    end
  end

    on_arm do
      resource "opencv-python" do
        url "https://files.pythonhosted.org/packages/fc/6f/5a28fef4c4a382be06afe3938c64cc168223016fa520c5abaf37e8862aa5/opencv_python-4.13.0.92-cp37-abi3-macosx_13_0_arm64.whl"
        sha256 "caf60c071ec391ba51ed00a4a920f996d0b64e3e46068aac1f646b5de0326a19"
      end
    end

    on_intel do
      resource "opencv-python" do
        url "https://files.pythonhosted.org/packages/08/ac/6c98c44c650b8114a0fb901691351cfb3956d502e8e9b5cd27f4ee7fbf2f/opencv_python-4.13.0.92-cp37-abi3-macosx_14_0_x86_64.whl"
        sha256 "5868a8c028a0b37561579bfb8ac1875babdc69546d236249fff296a8c010ccf9"
      end
    end
  
  on_arm do
    resource "pillow" do
      url "https://files.pythonhosted.org/packages/19/1e/dce46f371be2438eecfee2a1960ee2a243bbe5e961890146d2dee1ff0f12/pillow-12.2.0-cp314-cp314t-macosx_11_0_arm64.whl"
      sha256 "d5d38f1411c0ed9f97bcb49b7bd59b6b7c314e0e27420e34d99d844b9ce3b6f3"
    end
  end

  on_intel do
    resource "pillow" do
      url "https://files.pythonhosted.org/packages/b6/ab/1b426a3974cb0e7da5c29ccff4807871d48110933a57207b5a676cccc155/pillow-12.2.0-cp314-cp314t-macosx_10_15_x86_64.whl"
      sha256 "57850958fe9c751670e49b2cecf6294acc99e562531f4bd317fa5ddee2068463"
    end
  end
  
  on_arm do
    resource "numpy" do
      url "https://files.pythonhosted.org/packages/05/1a/d8007a5138c179c2bf33ef44503e83d70434d2642877ee8fbb230e7c0548/numpy-2.4.4-cp314-cp314t-macosx_14_0_arm64.whl"
      sha256 "42c16925aa5a02362f986765f9ebabf20de75cdefdca827d14315c568dcab113"
    end
  end

  on_intel do
    resource "numpy" do
      url "https://files.pythonhosted.org/packages/99/64/ffb99ac6ae93faf117bcbd5c7ba48a7f45364a33e8e458545d3633615dda/numpy-2.4.4-cp314-cp314t-macosx_14_0_x86_64.whl"
      sha256 "874f200b2a981c647340f841730fc3a2b54c9d940566a3c4149099591e2c4c3d"
    end
  end

  
  # def caveats  <<~EOS
  #     Chromium is managed by Playwright and installed separately.
  #     If Chromium is missing or broken, reinstall it manually:
  #      #{libexec}/bin/playwright install chromium

  #     On Linux, system dependencies may also be needed:
  #        #{libexec}/bin/playwright install chromium --with-deps
  #     EOS
  # end

  def caveats
    <<~EOS
    artwork-tui requires Chromium via Playwright.
    After installation run:

    playwright install chromium

    EOS
  end

  test do
    system "#{bin}/artwork-tui", "--version"
  end
end
