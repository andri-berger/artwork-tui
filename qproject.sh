#!/usr/bin/env sh

# Descriptive / functional:
# gensheet – A terminal-based artwork and layout generator with font and image support
# tui-press – Spreadsheet-driven layout and artwork generation for the terminal
# gmic-gen – Terminal layout and artwork generator powered by G'MIC

# More conceptual / evocative:
# composit – A terminal compositing and layout engine for generative artwork
# foundry-tui – A terminal-native artwork foundry with randomized generation and manual layout
# pressroom – Layout and artwork generation from the terminal, spreadsheet-driven
# atelier – A terminal design atelier for generative and composed artwork

# Leaning into the novelty / generative angle:
# seedpress – Randomizer-driven artwork and layout generator for the terminal
# manifold – Generative artwork and layout composition from a terminal spreadsheet
# typeset-tui – Font, image and layout composition engine for the terminal
# castbox – Terminal-native artwork caster with randomized generation and manual layout control



INTERVAL=2
OUTPUT_DIR="$HOME/screenshots"
mkdir -p "$OUTPUT_DIR"

i=0
while true; do
    hyprshot -m output -f "$OUTPUT_DIR/frame_$(printf '%04d' $i).png"
    i=$((i+1))
    sleep "$INTERVAL"
done

# Then stitch into APNG with ffmpeg:
ffmpeg -framerate 0.5 -i "$OUTPUT_DIR/frame_%04d.png" -plays 0 output.apng

# Or if you prefer GIF:
ffmpeg -framerate 0.5 -i "$OUTPUT_DIR/frame_%04d.png" output.gif


