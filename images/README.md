# Tarot Card Images

This directory contains the tarot card images that will be bundled into the plugin.

## Structure
- `front/` - Contains 16 front-facing tarot card images (PNG format)
- `back/` - Contains 16 corresponding back-facing tarot card images (PNG format)

## Naming Convention
Please name your images as follows:
- Front cards: `card_01.png`, `card_02.png`, ..., `card_16.png`
- Back cards: `card_01_back.png`, `card_02_back.png`, ..., `card_16_back.png`

This ensures the plugin can correctly match front and back images for each card.

## Usage
When you add your images here, the plugin will:
1. Randomly select one of the 16 cards during sync
2. Load both the front and back images
3. Convert them to base64 encoding
4. Include them in the CloudQuery destination along with metadata
