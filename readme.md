# artwork-tui

![banner](./banner.png)

Generative design tool with a terminal UI — compose layouts, render to canvas, export to SVG/PDF.

Built with [Textual](https://github.com/Textualize/textual) · [Playwright](https://playwright.dev) · [PixiJS](https://pixijs.com)

---

## Install

**macOS (Homebrew)**
```bash
brew install you/tap/layoutgen
```

**Arch Linux (AUR)**
```bash
yay -S layoutgen
```

**Universal (pip/uv)**
```bash
uv tool install layoutgen
```

---

## Usage

```bash
layoutgen
```

Launches the TUI. Keyboard-driven, no mouse required.

---

## Development

### Prerequisites

Install [mise](https://mise.jdx.dev) — manages all required runtimes and tools:

```bash
# macOS
brew install mise

# Arch Linux
yay -S mise

# Universal
curl https://mise.run | sh
```

### Setup

```bash
git clone https://github.com/you/layoutgen
cd layoutgen
mise install    # python, uv, biome, esbuild, typescript
uv sync         # python dependencies
uv run layoutgen
```

### Commands

```bash
uv run layoutgen        # launch TUI
uv run pytest           # run tests
uv run ruff check .     # lint Python
biome check frontend/   # lint + format JS
tsc --noEmit            # type check JS
```

---

## Stack

| Layer | Technology |
|---|---|
| TUI | Textual |
| Canvas rendering | Playwright + PixiJS |
| Image processing | OpenCV, Pillow |
| SVG conversion | vtracer, resvg-py |
| PDF support | textual-pdf |
| Audio | sounddevice, soundfile |

---

## Release (maintainers)

```bash
uv build
git tag v0.1.0 && git push origin v0.1.0
uv publish
```

---

## License
```bash
 Copyright (C) 2024 Adrian Rothlisberger

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <https://www.gnu.org/licenses/>.
```
