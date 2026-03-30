# Bedside Mono

A simple monospace font inspired by bedside digital clocks.

![Sample image of the font](./art/preview.png)

## Requirements

You need the following tools to rebuild the font from source:

- [FontForge](https://fontforge.org/) with Python scripting support
- `make` (optional, but recommended for the provided build target)

The build uses these source files:

- `Zero.svg` through `Nine.svg`
- `Colon.svg`
- `build_bedside_mono.py`

## Usage

The repository includes a prebuilt font file at `BedsideMono.ttf`. If you just want to use the font, install that file on your system.

To rebuild the font from the SVG glyph sources:

```sh
make build
```

This generates:

```text
BedsideMono.ttf
```

You can also run the build script directly:

```sh
fontforge -script build_bedside_mono.py
```

## Cleaning

To remove the generated font file:

```sh
make clean
```

## Notes

- The font currently contains glyphs for `0-9`, `:`, plus `.notdef` and space.
- The build script centers imported SVG outlines into a fixed-width monospace advance.
