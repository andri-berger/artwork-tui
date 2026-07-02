# <img src="readme.png" width="50" valign="middle" alt="logo"> Artwork-TUI
Generative design tool with a terminal UI — compose layouts, render to canvas, export to Hi-Res Png (any resolution your machine can handle). artwork-tui is a terminal-native artwork and layout generator, operating entirely within the constraints of the TUI. It combines a spreadsheet-driven interface for manual layout composition with a randomizer engine for generative artwork, supporting custom fonts and image assets. 

The tool emerged from a simple frustration: existing creative layout tools are either locked behind expensive subscriptions, tied to a specific OS, or bloated with features that obscure rather than enable the creative process. The terminal, by contrast, offers a direct and honest working surface – what you type is what happens, no hidden layers, no telemetry, no forced updates. artwork-tui occupies a genuinely vacant niche: somewhere between a generative art framework (too code-heavy, no interface) and a design tool (too GUI-dependent, too opinionated), it offers a middle ground that has no real equivalent in the current landscape. The spreadsheet metaphor is deliberate – familiar enough to require no learning curve, structured enough to impose a productive constraint on the creative process.

[Installation](#installation) / 
[Configuration](#configuration) / 
[API Reference](#reference) / 
[API Credit](#credit) / 
[Gallery](#gallery)



<img src="Backend/modules/7100000000.png" width="100%">
<table>
    <tr>
        <td><a href="Backend/modules/7100000000.png">
        <img src="Backend/modules/7100000000.png"></a></td>
        <td><a href="Backend/modules/7100000001.png">
        <img src="Backend/modules/7100000001.png"></a></td>
        <td><a href="Backend/modules/7100000001.png">
        <img src="Backend/modules/7100000001.png"></a></td>
        <td><a href="Backend/modules/7100000002.png">
        <img src="Backend/modules/7100000002.png"></a></td>
        <td><a href="Backend/modules/7100000002.png">
    </tr>
</table>
<table>
    <tr>
        <td><a href="Backend/modules/7100000000.png">
        <img src="Backend/modules/7100000000.png"></a></td>
        <td><a href="Backend/modules/7100000001.png">
        <img src="Backend/modules/7100000001.png"></a></td>
        <td><a href="Backend/modules/7100000001.png">
        <img src="Backend/modules/7100000001.png"></a></td>
        <td><a href="Backend/modules/7100000002.png">
        <img src="Backend/modules/7100000002.png"></a></td>
        <td><a href="Backend/modules/7100000002.png">
        <img src="Backend/modules/7100000002.png">
        </a></td>
    </tr>
</table>

## Installation
Like its sibling filterx-tui, this is a Python TUI installed in an isolated
environment — no npm, no Electron shell. One honest caveat upfront: the
rendering engine is a real browser. Playwright drives a headless Chromium to
compose and rasterize the layouts, so the install includes a one-time browser
download (~150 MB). That is the price for GPU-accelerated WebGL filters and
pixel-perfect output; everything else stays lean.

#### Generic Install (Native)
Pulls the install script directly from the repo and wires everything up,
including the Playwright browser download. Requires Python 3.11+. As always
with curl-into-sh: the script is short and readable — take a look before you
run it.

```bash
curl -fsSL https://raw.githubusercontent.com/\
andri-berger/artwork-tui/main/install.sh | sh
```

#### macOS (Homebrew)
Tap the formula and let Homebrew resolve the Python side; the second command
fetches the Chromium build Playwright renders with. Dependencies are bundled
in that download, so no further setup is needed.

```bash
brew install andri-berger/artwork-tui/tap
playwright install chromium #deps are included
```

#### Linux Arch (AUR)
Use your AUR helper of choice. The `--with-deps` flag lets Playwright pull the
system libraries Chromium needs — on a minimal Arch install this saves you a
round of hunting missing shared objects. Firefox works as an alternative
engine if you prefer it; webkit is not supported.

```bash
yay -S artwork-tui #Or use paru instead
playwright install chromium --with-deps
# playwright install firefox --with-deps
```


## Configuration
The interface follows the same anatomy as filterx-tui: file trees on the left
feed the pipeline, a tabbed spreadsheet in the center holds every parameter,
and a button row drives generation and export. Buttons and function keys are
twins here as well — F5 simply presses Afs programmatically — so the API
Reference below and this table describe one surface from two angles.

The central idea is that an artwork is nothing but a spreadsheet. Six tabs
partition the parameter space: one for global settings, one for the master
layout, two for styling the element groups, and two for the image and
typography settings that apply across all elements. Every cell is editable,
every value ends up in the exported json — which means a finished piece can
be reopened, inspected, and modified cell by cell. There is no hidden state.

Elements are addressed by group and index, A00 through F99 — six groups of up
to a hundred elements each. The groups A–C can be seeded independently via
their buttons, which is what makes generated layouts reproducible: same
project file, same seeds, same artwork. As with the sibling project, image
previews render inline, so a terminal with a graphics protocol is required —
kitty, ghostty, or wezterm.
```bash
artwork-tui #Launches the TUI
# kitty, ghostty, wezterm 
# are supported as of now
```
<table>
    <tr>
        <th width="20">Docs</th>
        <th align="left">Element</th>
        <th align="left">Description</th>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Filetree JSON
        </kbd></td>
        <td>Choose your project. Every exported artwork doubles as a project file —
select any json here to reopen it with all parameters intact.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Filetree PNG
        </kbd></td>
        <td>Choose your background image for the elements. Any png works; the layout
engine composes all elements on top of it.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Filepicker OTF
        </kbd></td>
        <td>Choose your fonts for the elements on the canvas. Fonts are loaded per
project, so each artwork carries its own typography.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Table Tab I</kbd></td>
        <td>Global Setup / Settings — canvas dimensions, output options, and
everything that applies to the artwork as a whole rather than to a single
element.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Table Tab II</kbd></td>
        <td>Main Layout — position and arrangement of the elements on the canvas.
This is where the composition itself is defined.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Table Tab III</kbd></td>
        <td>Styling A00-C99 Elements. Visual parameters for the first three element
groups, one row per element.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Table Tab IV</kbd></td>
        <td>Styling D00-F99 Elements. Same structure as Tab III, covering the
remaining three groups.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Table Tab V</kbd></td>
        <td>Image Settings all Elements (A00 - F99) — filter and rendering parameters
applied to image-based elements across all groups.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Table Tab VI</kbd></td>
        <td>Text/Font Settings all Elements (A00 - F99) — typography parameters such
as font assignment, size, and spacing across all groups.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Button X</kbd></td>
        <td>Clear the Canvas and all associated Table Params (in all 6 Tabs). Basically start from scratch. Please export before.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Button Afs</kbd></td>
        <td>Set Seed for A00-A99 Elements. Pins the random generator for this group,
making generated results reproducible across runs.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Button Bfs</kbd></td>
        <td>Set Seed for B00-B99. Same principle, scoped to the B group — the three
seedable groups are independent of each other.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Button Cfs</kbd></td>
        <td>Set Seed for C00-C99. With all three seeds set, a generated layout is
fully deterministic.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Button Create</kbd></td>
        <td>Generate Artwork via Random Generator. Draws random values into the grid
using the seeds where given — a discovery tool as much as a shortcut.</td>
    </tr>
    <tr>
        <td><a href="Backend/modules/7000000029.png">
        <img src="Backend/modules/17000000029.png"></a></td>
        <td><kbd>Button Export</kbd></td>
        <td>Export both generated (png) and project file (json) into the directory from where the app was executed / started. Clean Unix-timestamp format.</td>
    </tr>
</table>


## API Reference
Everything is keyboard-driven, and the function keys are deliberately thin:
F4 through F9 do not implement anything themselves — they programmatically
press their button twins from the Configuration table above. One action, one
code path, two ways to reach it; whatever holds for a button holds for its
key, and the two tables stay in sync by construction rather than by
discipline.

The remaining bindings are spreadsheet vocabulary. F1/F2/F3 give you
copy/cut/paste on cells — the grid is meant to be worked like a spreadsheet,
including moving values between rows, tabs, and element groups. Navigation
follows terminal conventions throughout: if you have used any TUI before,
your hands already know this table.

<table>
    <tr>
        <th align="left">Key</th>
        <th align="left">Binding</th>
        <th align="left">Description</th>
    </tr>
    <tr>
        <td><kbd>Del
        </kbd></td>
        <td>Delete</td>
        <td>Delete table cell.</td>
    </tr>
    <tr>
        <td><kbd>F1
        </kbd></td>
        <td>Copy</td>
        <td>Copy table cell. Think of it as Ctrl-C in a spreadsheet. </td>
    </tr>
    <tr>
        <td><kbd>F2
        </kbd></td>
        <td>Cut</td>
        <td>Cut table cell. Think of it as Ctrl-C in a spreadsheet. </td>
    </tr>
    <tr>
        <td><kbd>
        F3</kbd></td>
        <td>Paste</td>
        <td>Paste table cell. Think of it as Ctrl-V in a spreadsheet. </td>
    </tr>
    <tr>
        <td><kbd>
        F4</kbd></td>
        <td>Clear</td>
        <td>Triggers <kbd>Button X</kbd> programmatically (see Table above).</td>
    </tr>
    <tr>
        <td><kbd>
        F5</kbd></td>
        <td>Afs</td>
        <td>Triggers <kbd>Button Afs</kbd> programmatically (see Table above).</td>
    </tr>
    <tr>
        <td><kbd>
        F6</kbd></td>
        <td>Bfs</td>
        <td>Triggers <kbd>Button Bfs</kbd> programmatically (see Table above).</td>
    </tr>
    <tr>
        <td><kbd>
        F7</kbd></td>
        <td>Cfs</td>
        <td>Triggers <kbd>Button Cfs</kbd> programmatically (see Table above).</td>
    </tr>
    <tr>
        <td><kbd>
        F8</kbd></td>
        <td>Create</td>
        <td>Triggers <kbd>Button Create</kbd> programmatically (see Table above).</td>
    </tr>
    <tr>
        <td><kbd>
        F9</kbd></td>
        <td>Export</td>
        <td>Triggers <kbd>Button Export</kbd> programmatically (see Table above).</td>
    </tr>
    <tr>
        <td><kbd>
        Tab</kbd></td>
        <td>Navigate</td>
        <td>Cycle forward through all navigational UI elements — file trees, the six
table tabs, and the button row — in a fixed, predictable order.</td>
    </tr>
    <tr>
        <td><kbd>
        Arrow-keys</kbd></td>
        <td>Navigation</td>
        <td>Navigate table/grid cells in all directions: left, right, up, down.
Within the file trees, up/down move through entries.</td>
    </tr>
    <tr>
        <td><kbd>
        BackSpace</kbd></td>
        <td>Navigation</td>
        <td>Step back one level — leaves cell editing without applying the change,
or collapses the current node in a file tree.</td>
    </tr>
    <tr>
        <td><kbd>
        Space</kbd></td>
        <td>Navigation</td>
        <td>Toggle the element under the cursor — expands or collapses a tree node
without moving focus.</td>
    </tr>
    <tr>
        <td><kbd>
        Enter</kbd></td>
        <td>Navigation</td>
        <td>Confirm — commits the edited cell value, or opens the highlighted file
into the project.</td>
    </tr>
    <tr>
        <td><kbd>
        Ctrl-Q</kbd></td>
        <td>System</td>
        <td>Exit the app. There is no exit prompt — F9 is the explicit save, so
export first if the current grid state matters to you.</td>
    </tr>
</table>


## API Credit
This tool stands on other people's work, and the table below is meant as more
than a dependency list. Entries are grouped by layer: **Build** covers what
produces the README assets, **Utility** the Python and JavaScript toolchain —
including d3-random, whose seedable generators are what makes reproducible
artwork possible in the first place. **Framework** is the TUI foundation,
while **Conversion** and **Processing** form the rendering heart: Playwright
drives the browser, html-to-image rasterizes the composed layout, and the
PixiJS filter collection provides the WebGL effects layered on top. The layout
engine itself is homegrown, but it would have nothing to run on without these.

The **Inspiration** entries are of a different kind than in filterx-tui: no
code, not even patterns — purely visual debts. The linked Pinterest board is
the moodboard this tool was built to chase, and print-artwork.com is the
commercial ancestor both sibling projects were carved out of. If you want to
understand what the random generator is aiming at aesthetically, those two
links say more than any parameter documentation could.

<table width="100%">
    <tr>
        <th align="left">Layer</th>
        <th align="left">Name</th>
        <th align="left">Link</th>
    </tr>
    </tr>
    <tr>
        <td><kbd>
        Build</kbd></td>
        <td>Apng</td><td>
        <a href="//github.com/apngasm/apngasm">
        https://github.com/apngasm/apng</a></td>
    </tr>
    </tr>
        <tr><td><kbd>
        Build</kbd></td>
        <td>Grim</td><td>
        <a href="//github.com/emersion/grim">
        https://github.com/emersion/grim</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utility</kbd></td>
        <td>Biome</td><td>
        <a href="//github.com/biomejs/biome">
        https://github.com/biomejs/biome</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utility</kbd></td>
        <td>Ruff</td><td>
        <a href="//github.com/astral-sh/ruff">
        https://github.com/astral-sh/ruff</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utility</kbd></td>
        <td>Pip Uv</td><td>
        <a href="//github.com/astral-sh/uv">
        https://github.com/astral-sh/uv</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utilities</kbd></td>
        <td>Numpy</td><td>
        <a href="//github.com/numpy/numpy">
        https://github.com/numpy/numpy</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utilities</kbd></td>
        <td>Random</td><td>
        <a href="https://github.com/d3/d3-random">
        https://github.com/d3/d3-random</a></td>
    </tr>
    <tr>
        <td><kbd>
        Framework</kbd></td>
        <td>Textual</td><td>
        <a href="//github.com/Textualize/textual">
        https://github.com/Textualize/textual</a></td>
    </tr>
    <tr>
        <td><kbd>
        Framework</kbd></td>
        <td>Textual Img</td><td>
        <a href="//github.com/lnqs/textual-image">
        https://github.com/lnqs/textual-image</a></td>
    </tr>
    <tr>
        <td><kbd>
        Conversion</kbd></td>
        <td>Html Image</td><td>
        <a href="//github.com/bubkoo/html-to-image">
        https://github.com/bubkoo/html-to-image</a></td>
    </tr>
    <tr>
        <td><kbd>
        Conversion</kbd></td>
        <td>Playwright</td><td>
        <a href="https://github.com/microsoft/playwright">
        https://github.com/microsoft/playwright</a></td>
    </tr>
    <tr>
        <td><kbd>
        Processing</kbd></td>
        <td>OpenCV</td><td>
        <a href="https://github.com/opencv/opencv">
        https://github.com/opencv/opencv</a></td>
    </tr>
    <tr>
        <td><kbd>
        Processing</kbd></td>
        <td>Pixi Filter</td><td>
        <a href="//github.com/pixijs/filters">
        https://github.com/pixijs/filters</a></td>
    </tr>
    <tr>
        <td><kbd>
        Inspiration</kbd></td>
        <td>Pinterest</td><td>
        <a href="//de.pinterest.com/andriberger/_saved">
        https://de.pinterest.com/andri</a></td>
    </tr>
    <tr>
        <td><kbd>
        Inspiration</kbd></td>
        <td>Artwork</td><td>
        <a href="//print-artwork.com">
        https://print-artwork.com</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td> 
    </tr>
</table>


## PI Gallery
Thirty layouts straight from the random generator — where the filterx gallery
shows one image transformed many ways, this one shows the opposite: many
compositions from one machine. Each piece below was generated with Create,
rendered through the Playwright/PixiJS pipeline, and exported untouched; the
differences between them are nothing but different values in the six-tab
spreadsheet.

None of these are dead ends, either. Every png in the grid has a json sibling
carrying its complete parameter set — reopen it, change a seed or a single
cell, and you get a variation instead of starting over. Filenames are the
Unix timestamps of their render runs, left as-is: batch outputs, not a
curated portfolio. Click any thumbnail for full resolution.

<table>
  <tr>
    <td><a href="Backend/module/17000000000.png">
    <img src="Backend/module/17000000000.png">
    </a></td>
    <td><a href="Backend/module/17000000001.png">
    <img src="Backend/module/17000000001.png">
    </a></td>
    <td><a href="Backend/module/17000000002.png">
    <img src="Backend/module/17000000002.png">
    </a></td>
    <td><a href="Backend/module/17000000003.png">
    <img src="Backend/module/17000000003.png">
    </a></td>
    <td><a href="Backend/module/17000000004.png">
    <img src="Backend/module/17000000004.png">
    </a></td>
    <td><a href="Backend/module/17000000005.png">
    <img src="Backend/module/17000000005.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/module/17000000006.png">
    <img src="Backend/module/17000000006.png">
    </a></td>
    <td><a href="Backend/module/17000000007.png">
    <img src="Backend/module/17000000007.png">
    </a></td>
    <td><a href="Backend/module/17000000008.png">
    <img src="Backend/module/17000000008.png">
    </a></td>
    <td><a href="Backend/module/17000000009.png">
    <img src="Backend/module/17000000009.png">
    </a></td>
    <td><a href="Backend/module/17000000010.png">
    <img src="Backend/module/17000000010.png">
    </a></td>
    <td><a href="Backend/module/17000000011.png">
    <img src="Backend/module/17000000011.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/module/17000000012.png">
    <img src="Backend/module/17000000012.png">
    </a></td>
    <td><a href="Backend/module/17000000013.png">
    <img src="Backend/module/17000000013.png">
    </a></td>
    <td><a href="Backend/module/17000000014.png">
    <img src="Backend/module/17000000014.png">
    </a></td>
    <td><a href="Backend/module/17000000015.png">
    <img src="Backend/module/17000000015.png">
    </a></td>
    <td><a href="Backend/module/17000000016.png">
    <img src="Backend/module/17000000016.png">
    </a></td>
    <td><a href="Backend/module/17000000017.png">
    <img src="Backend/module/17000000017.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/module/17000000018.png">
    <img src="Backend/module/17000000018.png">
    </a></td>
    <td><a href="Backend/module/17000000019.png">
    <img src="Backend/module/17000000019.png">
    </a></td>
    <td><a href="Backend/module/17000000020.png">
    <img src="Backend/module/17000000020.png">
    </a></td>
    <td><a href="Backend/module/17000000021.png">
    <img src="Backend/module/17000000021.png">
    </a></td>
    <td><a href="Backend/module/17000000022.png">
    <img src="Backend/module/17000000022.png">
    </a></td>
    <td><a href="Backend/module/17000000023.png">
    <img src="Backend/module/17000000023.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/module/17000000024.png">
    <img src="Backend/module/17000000024.png">
    </a></td>
    <td><a href="Backend/module/17000000025.png">
    <img src="Backend/module/17000000025.png">
    </a></td>
    <td><a href="Backend/module/17000000026.png">
    <img src="Backend/module/17000000026.png">
    </a></td>
    <td><a href="Backend/module/17000000027.png">
    <img src="Backend/module/17000000027.png">
    </a></td>
    <td><a href="Backend/module/17000000028.png">
    <img src="Backend/module/17000000028.png">
    </a></td>
    <td><a href="Backend/module/17000000029.png">
    <img src="Backend/module/17000000029.png">
    </a></td>
  </tr>
</table>
<br>
