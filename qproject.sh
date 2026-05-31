#!/usr/bin/env sh

# Modern Art
# Geometric Art
# Minimalist Art
# Generative Art
# Algorithmic Art
# Procedural Art
# Contemporary Art
# Abstract Painting
# Modern Painting
# Geometric Painting
# Minimalist Painting
# Generative Painting
# Algorithmic Painting
# Procedural Painting
# Contemporary Painting
# Create Abstract Art Fast
# Your Custom Art in HD
# Abstract Prints, Your Way
# Make Unique Abstract Art
# Design Abstract Art Now
# Abstract Art, No AI Needed
# Generate Art, Download HD
# Abstract Canvas Generator
# Abstract Art — Your Style
# Make Art, Print on Canvas
# Create Abstract Wall Art
# DIY Abstract Art Online
# High-Res Abstract Prints
# Custom Art, Instant File
# Abstract Art, No Limits
# Design Abstract Wall Art, Print It, Show It Off
# Make Abstract Art That’s 100% You — No AI Required
# Tired of AI Art? Make Your Own Abstract Masterpiece
# Design Abstract Art, Download in HD, Print on Canvas
# Create Custom Abstract Art — High-Res, Ready to Print
# Abstract Art Generator: From Screen to Wall in Minutes
# Generate Abstract Art You Can Actually Download & Print
# DIY Abstract Art: Make It, Download It, Print It, Flex It
# Design Your Own Abstract Art — No AI, Just Your Imagination
# Unleash Your Inner Artist: Create Custom Abstract Art for Print
# Your Vision, Your Art: Generate Stunning Abstracts, Download or Print
# Make custom abstract art in minutes. Download or print your masterpiece!
# Design your abstract art and print it or download high-res files instantly.
# Create unique abstract artwork online — print on canvas or download HD art.
# Generate abstract art that’s 100% yours. Print or save high-resolution art.
# Your art, your rules. Create abstract pieces, download, or print on canvas.

# artwork-tui is a terminal-native artwork and layout generator built on G'MIC, operating entirely within the constraints of the TUI. It combines a spreadsheet-driven interface for manual layout composition with a randomizer engine for generative artwork, supporting custom fonts and image assets. The tool emerged from a simple frustration: existing creative layout tools are either locked behind expensive subscriptions, tied to a specific OS, or bloated with features that obscure rather than enable the creative process. The terminal, by contrast, offers a direct and honest working surface – what you type is what happens, no hidden layers, no telemetry, no forced updates. artwork-tui occupies a genuinely vacant niche: somewhere between a generative art framework (too code-heavy, no interface) and a design tool (too GUI-dependent, too opinionated), it offers a middle ground that has no real equivalent in the current landscape. The spreadsheet metaphor is deliberate – familiar enough to require no learning curve, structured enough to impose a productive constraint on the creative process.

# gensheet – A terminal-based artwork and layout generator with font and image support
# tui-press – Spreadsheet-driven layout and artwork generation for the terminal
# gmic-gen – Terminal layout and artwork generator powered by G'MIC

# composit – A terminal compositing and layout engine for generative artwork
# foundry-tui – A terminal-native artwork foundry with randomized generation and manual layout
# pressroom – Layout and artwork generation from the terminal, spreadsheet-driven
# atelier – A terminal design atelier for generative and composed artwork

# seedpress – Randomizer-driven artwork and layout generator for the terminal
# manifold – Generative artwork and layout composition from a terminal spreadsheet
# typeset-tui – Font, image and layout composition engine for the terminal
# castbox – Terminal-native artwork caster with randomized generation and manual layout control

# apngasm output.apng frame1.png frame2.png frame3.png -d 100  # 100ms per frame
# apngasm output.apng frame1.png 1/2 frame2.png 1/4 frame3.png 1/1
# apngasm output.apng frames/*.png -d 10  # 10ms per frame
# apngasm output.apng frame*.png 1 10

INTERVAL=2
OUTPUT_DIR="$HOME/screenshots"
mkdir -p "$OUTPUT_DIR"

i=0
while true; do
    grim "$OUTPUT_DIR/frame_$(printf '%04d' $i).png"
    i=$((i+1))
    sleep "$INTERVAL"
done

