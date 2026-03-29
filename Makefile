FONTFORGE ?= fontforge
BUILD_SCRIPT := build_bedside_mono.py
OUTPUT_FONT := BedsideMono.ttf

.PHONY: all build clean

all: build

build: $(OUTPUT_FONT)

$(OUTPUT_FONT): $(BUILD_SCRIPT) Zero.svg One.svg Two.svg Three.svg Four.svg Five.svg Six.svg Seven.svg Eight.svg Nine.svg Colon.svg
	$(FONTFORGE) -script $(BUILD_SCRIPT)

clean:
	rm -f $(OUTPUT_FONT)
