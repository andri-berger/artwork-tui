
#!/bin/sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
  uv sync
  playwright install chromium --with-deps

#!/bin/sh
  if ! command -v uv >/dev/null 2>&1; then
      curl -LsSf https://astral.sh/uv/install.sh | sh
      export PATH="$HOME/.local/bin:$PATH"
  fi
  uv tool install layout-tui



#!/usr/bin/env sh
  set -e   # exit on any error

  # install uv if not already present
  if ! command -v uv >/dev/null 2>&1; then
    echo "installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
  else
    echo "uv already installed, skipping"
  fi

  # install python if not present
  uv python install 3.14

  # bootstrap dependencies
  uv sync --frozen   # --frozen respects lockfile exactly

  # run
  uv run layout-tui

#!/usr/bin/env sh
  set -e

  # install uv
  if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
  fi

  # use Guix Python if available
  # avoids glibc path issues
  if command -v python3 >/dev/null 2>&1; then
    PYTHON=$(command -v python3)
    uv sync --python "$PYTHON" --frozen
  else
    uv python install 3.14
    uv sync --frozen
  fi

  uv run layout-tui

  #!/usr/bin/env sh
  set -e

  # silent install — no package manager visible to user
  install_uv() {
    curl -LsSf https://astral.sh/uv/install.sh | sh \
      2>/dev/null   # suppress output
    export PATH="$HOME/.local/bin:$PATH"
  }

  # check and install silently
  if ! command -v uv >/dev/null 2>&1; then
    install_uv
  fi

  # install tool globally if not present
  if ! command -v layout-tui >/dev/null 2>&1; then
    uv tool install layout-tui --quiet
  fi

  # launch — user sees nothing of above
  layout-tui

#!/bin/sh
  set -e

  REPO="https://github.com/you/layout-tui"
  VERSION="v1.0.0"

  # install uv if missing
  if ! command -v uv >/dev/null 2>&1; then
      curl -LsSf https://astral.sh/uv/install.sh | sh
      export PATH="$HOME/.local/bin:$PATH"
  fi

  # install directly from GitHub — no PyPI needed
  uv tool install "git+${REPO}.git@${VERSION}"

  User runs one command:
  curl -LsSf https://github.com/you/layout-tui/install.sh | sh


    # your original VPS script:
  curl -LsSf https://astral.sh/uv/install.sh | sh
  uv sync                        ← fails — no pyproject.toml here
  playwright install chromium

  # corrected:
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
  git clone https://github.com/you/layout-tui  ← missing step
  cd layout-tui                                ← missing step
  uv sync                        ← now works
  playwright install chromium --with-deps

  ---
  The mental model

  uv tool install   →   fetches project + dependencies
                         knows URL
                         self-contained

  uv sync           →   only fetches dependencies
                         project already present
                         reads local pyproject.toml
                         URL irrelevant

  ---
  Three scripts, three distinct purposes

  install.sh (end user):
  → curl uv installer
  → uv tool install git+URL    ← fetches project + deps

  deploy.sh (VPS):
  → curl uv installer
  → git clone URL              ← fetches project
  → cd into project
  → uv sync                    ← fetches deps only
  → playwright install chromium

  bootstrap.sh (developer):
  → git clone URL              ← already has uv
  → cd into project
  → uv sync                    ← fetches deps only
  → ready to develop