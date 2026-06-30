#!/usr/bin/env sh

# REDDIT:: r/commandline r/tui - I built a terminal-native layout composer and generative art tool because I was tired of paying for things that export watermarked PNGs - Long story short: I wanted a creative layout tool that runs locally, works the same on any Unix box, doesn't require a login, and doesn't upsell me mid-session. Couldn't find one. Built it instead. artwork-tui is a Python TUI built with Textual. The interface is a spreadsheet — you fill cells, configure layout properties, and either compose manually or let the randomizer engine take over and iterate from there. Rendering goes through a Playwright/Chromium pipeline with PixiJS doing the filter work (WebGL-based, so things like ASCII and noise effects run properly). Supports custom fonts and image assets. It's somewhere between a generative art framework (usually: write code first, see results never) and a design tool (usually: $20/month, Windows/Mac only, cloud save). Neither felt right. This does. Still WIP but functional. GPL-3, no telemetry, no account.

# HACKERNEWS:: artwork-tui – generative layout composer for the terminal, spreadsheet-driven - Most creative layout tools sit at one of two extremes: generative art frameworks that require you to write code before anything appears on screen, or GUI design tools that make every decision for you and phone home while doing it. artwork-tui lives in the gap. It's a TUI with a spreadsheet interface for composing layouts manually — or handing control to a randomizer engine and iterating from there. Custom fonts, image assets, G'MIC filters underneath. The whole thing runs in a terminal, which means it works the same on any Unix box without an Electron runtime eating your RAM. The spreadsheet metaphor isn't ironic. A grid with cells you fill in turns out to be a surprisingly honest constraint for layout work — structured enough to keep things from becoming formless, familiar enough that there's nothing to learn before you start. No subscription. No OS lock-in. No update nag. Just a table and a render loop.

# PRODUCTHUNT:: artwork-tui — A generative layout composer that lives in your terminal - Spreadsheet meets generative art. No GUI, no subscription, no nonsense. - artwork-tui is a terminal-native creative tool that lets you compose layouts and generate artwork — either by hand or by letting the randomizer take the wheel. The interface is a spreadsheet. Not because terminals are cool (they are), but because a grid turns out to be the right mental model for layout work: cells, constraints, and a clear output. Add your own fonts, drop in image assets, chain G'MIC filters for effects. Hit render. What makes it different: * No subscription — runs locally, forever * No OS lock-in — any Unix terminal, same experience * Two modes: manual composition or generative randomizer * Built on G'MIC, one of the most powerful open-source image processing engines available * If you've ever wanted a creative tool that respects your filesystem and doesn't require a login screen, this is the gap it fills.

# GITHUB:: artwork-tui is a terminal-native artwork and layout generator built on G'MIC, operating entirely within the constraints of the TUI. It combines a spreadsheet-driven interface for manual layout composition with a randomizer engine for generative artwork, supporting custom fonts and image assets. The tool emerged from a simple frustration: existing creative layout tools are either locked behind expensive subscriptions, tied to a specific OS, or bloated with features that obscure rather than enable the creative process. The terminal, by contrast, offers a direct and honest working surface – what you type is what happens, no hidden layers, no telemetry, no forced updates. artwork-tui occupies a genuinely vacant niche: somewhere between a generative art framework (too code-heavy, no interface) and a design tool (too GUI-dependent, too opinionated), it offers a middle ground that has no real equivalent in the current landscape. The spreadsheet metaphor is deliberate – familiar enough to require no learning curve, structured enough to impose a productive constraint on the creative process.

# GITHUB:: Fully customizable, artwork and layout generator as images, operated from the terminal, spreadsheet based.
# GITHUB:: castbox – Terminal-native artwork caster with randomized generation and manual layout control
# GITHUB:: foundry-tui – A terminal-native artwork foundry with randomized generation and manual layout
# GITHUB:: gensheet – A terminal-based artwork and layout generator with font and image support
# GITHUB:: manifold – Generative artwork and layout composition from a terminal spreadsheet
# GITHUB:: pressroom – Layout and artwork generation from the terminal, spreadsheet-driven
# GITHUB:: tui-press – Spreadsheet-driven layout and artwork generation for the terminal
# GITHUB:: seedpress – Randomizer-driven artwork and layout generator for the terminal
# GITHUB:: composit – A terminal compositing and layout engine for generative artwork
# GITHUB:: typeset-tui – Font, image and layout composition engine for the terminal
# GITHUB:: atelier – A terminal design atelier for generative and composed artwork
# GITHUB:: gmic-gen – Terminal layout and artwork generator powered by G'MIC

# PRINT-ARTWORK:: Design your abstract art and print it or download high-res files instantly.
# PRINT-ARTWORK:: Create unique abstract artwork online — print on canvas or download HD art.
# PRINT-ARTWORK:: Generate abstract art that’s 100% yours. Print or save high-resolution art.
# PRINT-ARTWORK:: Your art, your rules. Create abstract pieces, download, or print on canvas.
# PRINT-ARTWORK:: Make custom abstract art in minutes. Download or print your masterpiece!
# PRINT-ARTWORK:: Your Vision, Your Art: Generate Stunning Abstracts, Download or Print
# PRINT-ARTWORK:: Unleash Your Inner Artist: Create Custom Abstract Art for Print
# PRINT-ARTWORK:: Design Your Own Abstract Art — No AI, Just Your Imagination
# PRINT-ARTWORK:: DIY Abstract Art: Make It, Download It, Print It, Flex It
# PRINT-ARTWORK:: Generate Abstract Art You Can Actually Download & Print
# PRINT-ARTWORK:: Abstract Art Generator: From Screen to Wall in Minutes
# PRINT-ARTWORK:: Create Custom Abstract Art — High-Res, Ready to Print
# PRINT-ARTWORK:: Design Abstract Art, Download in HD, Print on Canvas
# PRINT-ARTWORK:: Tired of AI Art? Make Your Own Abstract Masterpiece
# PRINT-ARTWORK:: Make Abstract Art That’s 100% You — No AI Required
# PRINT-ARTWORK:: Design Abstract Wall Art, Print It, Show It Off
# PRINT-ARTWORK:: Abstract Art, No AI Needed
# PRINT-ARTWORK:: Abstract Prints, Your Way
# PRINT-ARTWORK:: Generate Art, Download HD
# PRINT-ARTWORK:: Abstract Canvas Generator
# PRINT-ARTWORK:: Abstract Art — Your Style
# PRINT-ARTWORK:: Make Art, Print on Canvas
# PRINT-ARTWORK:: Make Unique Abstract Art
# PRINT-ARTWORK:: Create Abstract Art Fast
# PRINT-ARTWORK:: High-Res Abstract Prints
# PRINT-ARTWORK:: Custom Art, Instant File
# PRINT-ARTWORK:: Create Abstract Wall Art
# PRINT-ARTWORK:: DIY Abstract Art Online
# PRINT-ARTWORK:: Design Abstract Art Now
# PRINT-ARTWORK:: Abstract Art, No Limits
# PRINT-ARTWORK:: Contemporary Painting
# PRINT-ARTWORK:: Your Custom Art in HD
# PRINT-ARTWORK:: Algorithmic Painting
# PRINT-ARTWORK:: Minimalist Painting
# PRINT-ARTWORK:: Generative Painting
# PRINT-ARTWORK:: Procedural Painting
# PRINT-ARTWORK:: Geometric Painting
# PRINT-ARTWORK:: Abstract Painting
# PRINT-ARTWORK:: Contemporary Art
# PRINT-ARTWORK:: Algorithmic Art
# PRINT-ARTWORK:: Modern Painting
# PRINT-ARTWORK:: Procedural Art
# PRINT-ARTWORK:: Minimalist Art
# PRINT-ARTWORK:: Generative Art
# PRINT-ARTWORK:: Geometric Art
# PRINT-ARTWORK:: Modern Art

# apngasm output.apng frames/*.png -d 2000
# apngasm output.apng frames/*.png -d 1600
# apngasm output.apng frames/*.png -d 1200

INTERVAL=2
OUTPUT_DIR="$HOME/screenshots"
mkdir -p "$OUTPUT_DIR"

i=0
while true; do
    grim "$OUTPUT_DIR/frame_$(printf '%04d' $i).png"
    i=$((i+1))
    sleep "$INTERVAL"
done

