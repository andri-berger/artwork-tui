
![Readme](./readme.png)
# Artwork-TUI (WIP)
Generative design tool with a terminal UI — compose layouts, render to canvas, export to Hi-Res Png (any resolution your machine can handle). artwork-tui is a terminal-native artwork and layout generator, operating entirely within the constraints of the TUI. It combines a spreadsheet-driven interface for manual layout composition with a randomizer engine for generative artwork, supporting custom fonts and image assets. The tool emerged from a simple frustration: existing creative layout tools are either locked behind expensive subscriptions, tied to a specific OS, or bloated with features that obscure rather than enable the creative process. The terminal, by contrast, offers a direct and honest working surface – what you type is what happens, no hidden layers, no telemetry, no forced updates. artwork-tui occupies a genuinely vacant niche: somewhere between a generative art framework (too code-heavy, no interface) and a design tool (too GUI-dependent, too opinionated), it offers a middle ground that has no real equivalent in the current landscape. The spreadsheet metaphor is deliberate – familiar enough to require no learning curve, structured enough to impose a productive constraint on the creative process.

[Installation](#installation) / 
[Configuration](#configuration) / 
[API Reference](#reference) / 
[API Credit](#credit) / 
[Gallery](#gallery)


<img src="Backend/modules/17100000000.png" width="100%">
<table>
  <tr>
    <td><a href="Backend/modules/17100000000.png">
    <img src="Backend/modules/17100000000.png">
    </a></td>
    <td><a href="Backend/modules/17100000001.png">
    <img src="Backend/modules/17100000001.png">
    </a></td>
    <td><a href="Backend/modules/17100000001.png">
    <img src="Backend/modules/17100000001.png">
    </a></td>
    <td><a href="Backend/modules/17100000002.png">
    <img src="Backend/modules/17100000002.png">
    </a></td>
    <td><a href="Backend/modules/17100000002.png">
    <img src="Backend/modules/17100000002.png">
    </a></td>
  </tr>

<!-- 
<tr>
    <td><a href="Backend/modules/1710000008.png">
    <img src="Backend/modules/1710000008.png">
    </a></td>
    <td><a href="Backend/modules/1710000009.png">
    <img src="Backend/modules/1710000009.png">
    </a></td>
    <td><a href="Backend/modules/1710000010.png">
    <img src="Backend/modules/1710000010.png">
    </a></td>
    <td><a href="Backend/modules/1710000011.png">
    <img src="Backend/modules/1710000011.png">
    </a></td>
    <td><a href="Backend/modules/1710000012.png">
    <img src="Backend/modules/1710000012.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/modules/1710000014.png">
    <img src="Backend/modules/1710000014.png">
    </a></td>
    <td><a href="Backend/modules/1710000015.png">
    <img src="Backend/modules/1710000015.png">
    </a></td>
    <td><a href="Backend/modules/1710000016.png">
    <img src="Backend/modules/1710000016.png">
    </a></td>
    <td><a href="Backend/modules/1710000017.png">
    <img src="Backend/modules/1710000017.png">
    </a></td>
    <td><a href="Backend/modules/1710000018.png">
    <img src="Backend/modules/1710000018.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/modules/1710000020.png">
    <img src="Backend/modules/1710000020.png">
    </a></td>
    <td><a href="Backend/modules/1710000021.png">
    <img src="Backend/modules/1710000021.png">
    </a></td>
    <td><a href="Backend/modules/1710000022.png">
    <img src="Backend/modules/1710000022.png">
    </a></td>
    <td><a href="Backend/modules/1710000023.png">
    <img src="Backend/modules/1710000023.png">
    </a></td>
    <td><a href="Backend/modules/1710000024.png">
    <img src="Backend/modules/1710000024.png">
    </a></td>
  </tr>
  <tr>
    <td><a href="Backend/modules/1710000026.png">
    <img src="Backend/modules/1710000026.png">
    </a></td>
    <td><a href="Backend/modules/1710000027.png">
    <img src="Backend/modules/1710000027.png">
    </a></td>
    <td><a href="Backend/modules/1710000028.png">
    <img src="Backend/modules/1710000028.png">
    </a></td>
    <td><a href="Backend/modules/1710000029.png">
    <img src="Backend/modules/1710000029.png">
    </a></td>
    <td><a href="Backend/modules/1710000030.png">
    <img src="Backend/modules/1710000030.png">
    </a></td>
  </tr> 
-->
</table>
<br>


## Installation
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

#### Generic Install (Native)
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua

```bash
curl -fsSL https://raw.githubusercontent.com/\
andri-berger/artwork-tui/main/install.sh | sh
```

#### macOS (Homebrew)
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua

```bash
brew install andri-berger/artwork-tui/tap
playwright install chromium #deps are included
```

#### Linux Arch (AUR)
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua

```bash
yay -S artwork-tui #Or use paru instead
playwright install chromium --with-deps
# playwright install firefox --with-deps
```

## Configuration
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

```bash
artwork-tui #Launches the TUI
```

<table width="100%">
    <tr>
        <th align="left">KPG</th>
        <th align="left">Terminal</th>
        <th align="left">Plattform</th>
        <th align="left">Notes</th>
    </tr>
    <tr>
        <td>&#x2705;</td>
        <td>Kitty</td>
        <td>Linux, macOS</td>
        <td>The originator — reference implementation</td>
    </tr>
    <tr>
        <td>&#x2705;</td>
        <td>Ghostty</td>
        <td>Linux, macOS</td>
        <td>The new kid on the block — native support</td>
    </tr>
    <tr>
        <td>&#x2705;</td>
        <td>WezTerm</td>
        <td>Linux, macOS</td>
        <td>Also supports Sixel + iTerm2 protocol — widest coverage</td>
    </tr>
    <tr>
        <td>&#x1F7E1;</td>
        <td>suckless</td>
        <td>Linux</td>
        <td>Patch available implementing a subset of KGP - not built-in</td>
    </tr>
    <tr>
        <td>&#x274C;</td>
        <td>foot</td>
        <td>Linux (Wayland)</td>
        <td>Sixel only — notable omission given it's the go-to Wayland minimal terminal</td>
    </tr>
    <tr>
        <td>&#x274C;</td>
        <td>Alacritty</td>
        <td>Linux, macOS</td>
        <td>Intentionally does not support font ligatures or modern image protocols</td>
    </tr>
    <tr>
        <td>&#x274C;</td>
        <td>iTerm2</td>
        <td>macOS</td>
        <td>Has its own inline image protocol (iTerm2 protocol), not KGP</td>
    </tr>
     <tr>
        <td>&#x274C;</td>
        <td>Konsole</td>
        <td>Linux</td>
        <td>Sixely only</td>
    </tr>
    <tr>
        <td>&#x274C;</td>
        <td>Hyper</td>
        <td>Linux, macOS</td>
        <td>Electron-based, no image protocol</td>
    </tr>
    <tr>
        <td>&#x274C;</td>
        <td>Tabby</td>
        <td>Linux, macOS</td>
        <td>No image protocol</td>
    </tr>
</table>



## API Reference
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

<table>
    <tr>
        <th align="left">Key</th>
        <th align="left">Binding</th>
        <th align="left">Description</th>
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
        <td>Clear the Canvas. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td><kbd>
        F5</kbd></td>
        <td>Afs</td>
        <td>Set Seed for A00-A99 Elements. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td><kbd>
        F6</kbd></td>
        <td>Bfs</td>
        <td>Set Seed for B00-B99. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td><kbd>
        F7</kbd></td>
        <td>Cfs</td>
        <td>Set Seed for C00-C99. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td><kbd>
        F8</kbd></td>
        <td>Create</td>
        <td>Generate Artwork via Random Generator. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td><kbd>
        F9</kbd></td>
        <td>Export</td>
        <td>Export both generated (png) and project file (json) into the directory from where the app was executed / started.</td>
    </tr>
    <tr>
        <td><kbd>
        F10</kbd></td>
        <td>Scrolling</td>
        <td>Extra functionality (I) with regards to fullscreen toggle and scroll-emulation (=> see also shift-arrows)</td>
    </tr>
    <tr>
        <td><kbd>
        F11</kbd></td>
        <td>Scrolling</td>
        <td>Extra functionality (II) with regards to fullscreen toggle and scroll-emulation (=> see also shift-arrows)</td>
    </tr>
    <tr>
        <td><kbd>
        F12</kbd></td>
        <td>Scrolling</td>
        <td>Extra functionality (II) with regards to fullscreen toggle and scroll-emulation (=> see also shift-arrows)</td>
    </tr>
    <tr>
        <td><kbd>Del
        </kbd></td>
        <td>Delete</td>
        <td>Delete table/grid cell.</td>
    </tr>
    <tr>
        <td><kbd>
        Tab</kbd></td>
        <td>Navigate</td>
        <td>Cycle forward all navigational UI-Elements. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        Shift-Tab</kbd></td>
        <td>Navigate</td>
        <td>Cycle backward all navigational UI-Elements. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        Shift-Arrow</kbd></td>
        <td>Navigation</td>
        <td>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        Arrow-keys</kbd></td>
        <td>Navigation</td>
        <td>Navigate table/grid cells in all directions, left, right, top, bottom. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        BackSpace</kbd></td>
        <td>Navigation</td>
        <td>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        Space</kbd></td>
        <td>Navigation</td>
        <td>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        Enter</kbd></td>
        <td>Navigation</td>
        <td>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td><kbd>
        Ctrl-Q</kbd></td>
        <td>System</td>
        <td>Exit the app. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
</table>


## API Credit
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

<table width="100%">
    <tr>
        <th align="left">Layer</th>
        <th align="left">Name</th>
        <th align="left">
        Link <img width="560"></th>
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
        <td>PixiJs</td><td>
        <a href="//github.com/pixijs/filters">
        https://github.com/pixijs/filters</a></td>
    </tr>
</table>

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

## PI Gallery
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

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
    <!-- replace with bandcamp album-link !!! -->
    <img src="Backend/module/17000000029.png">
    </a></td>
  </tr>
</table>



## Rationale

If you encounter any issues, please file an issue on GitHub.
<br>If you find this module useful, please consider starring the repository on GitHub. 

This project began by moving most of the functionality from a commercial WEB SaaS-project https://print-artwork.com (minus the physical print / POD, minus the vectorizer => vtracer), free of charge, now at the complete opposite in copyleft territory, with some additional code-tweaks to accommodate the different UI-requirements in archaic TUI-land as opposed to shiny WEB-land. The app has been split up into the generation part, the meat and bones with this repository, and the glaze/gloss with the sibling <a href="https://github.com/andri-berger/filterx-tui>filterx-TUI">filterx-TUI</a> listed under the same GitHub Profile. Thus, they complement each another really well. One for the substance, the matter, the other for the refinement. 

We strongly believe that the TUI's very own nature, its limitations are its biggest strength! They might outlast every centralized UI-App (UI's are hostage to the cyclic Zeitgeist) due to their self-sufficient, decentralized nature, taking advantage of each user's own infrastructure. The less visual features there are, the less maintenance, the less choices, the less moving parts, the less friction, the more ease of mind, the more sparked creativity, the longer lasting a tool will be — this is our deepest conviction. Ultimately, what we strive for are timeless, stateless conditions, derived from first-order principles, from basic building blocks, be it in Art, Engineering or Elsewhere.

<br>
<br>
<br>
