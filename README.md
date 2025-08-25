# Feed Your AI Tarot - CloudQuery Plugin 🔮

A CloudQuery source plugin that delivers random tarot card images for your AI and data workflows! This plugin randomly selects one tarot card per sync and delivers both the front and back images along with metadata.

## 🎴 What You Get

Each sync delivers:
- **One random tarot card** from 16 available cards
- **Front and back images** in base64 format  
- **Card metadata**: name, number, and description
- **Timestamp** of when the card was drawn

## 📦 Plugin Architecture

- [plugin/tables/items.py](plugin/tables/items.py)
  - `TarotCards` - Table definition for tarot card data
  - `TarotCardResolver` - Resolver that fetches random cards
- [plugin/tarot/client.py](plugin/tarot/client.py)
  - `TarotClient` - Core client that handles card selection and image loading
- [plugin/client/client.py](plugin/client/client.py)
  - `Spec` - Plugin configuration including randomness seed
  - `Client` - CloudQuery client wrapper
- [plugin/plugin.py](plugin/plugin.py)
  - `TarotCardsPlugin` - Main plugin registration

## 🚀 Getting Started

### 1. Add Your Tarot Card Images

Place your 16 PNG images in the `images/` directory:

```
images/
├── front/
│   ├── card_01.png
│   ├── card_02.png
│   ├── ...
│   └── card_16.png
└── back/
    ├── card_01_back.png
    ├── card_02_back.png
    ├── ...
    └── card_16_back.png
```

### 2. Update Card Metadata

Edit `plugin/tarot/client.py` and replace the `DEFAULT_CARDS` dictionary with your card names and descriptions:

```python
DEFAULT_CARDS = {
    1: {"name": "Your Card Name", "description": "Your card description"},
    2: {"name": "Another Card", "description": "Another description"},
    # ... add all 16 cards
}
```

### 3. Configure Randomness (Optional)

In your CloudQuery config (`TestConfig.yaml`), you can optionally set a randomness seed for reproducible results:

```yaml
kind: source
spec:
  name: "tarot-cards"
  registry: "grpc"
  path: "localhost:7777"
  tables: ['*']
  destinations: ["sqlite"]
  spec:
    randomness_seed: 42  # Optional: for reproducible randomness
```

If you omit `randomness_seed`, each sync will be truly random!

## 🧪 Testing the Plugin

### Local Development

1. **Install dependencies:**
   ```bash
   pip install poetry
   poetry install
   ```

2. **Run the plugin server:**
   ```bash
   poetry run main serve
   ```

3. **In another terminal, sync your cards:**
   ```bash
   cloudquery sync
   ```

This creates a `db.sqlite` database with your randomly selected tarot card!

### Database Schema

The `tarot_cards` table contains:
- `card_number` (int) - Card number (1-16)
- `card_name` (string) - Name of the card  
- `description` (string) - Card description/meaning
- `front_image_base64` (string) - Front image as base64
- `back_image_base64` (string) - Back image as base64  
- `special_instructions` (string) - Special message (only for rare cards)
- `sync_time` (timestamp) - When the card was drawn

### 🔮 Rare Card Feature

**Card 16 ("The Stormcaller")** is ultra-rare with only **1% probability**! When someone pulls this special card, they receive:
- The rare card images  
- **Special instructions** to contact chris.r@cloudquery.io for free CloudQuery swag!

This gamification mechanic encourages repeated CloudQuery usage as users chase the rare card. 🎯

## 🎯 Use Cases

- **AI Training Data**: Random tarot imagery for training AI models
- **Marketing Growth Hacks**: Encourage CloudQuery usage with mystical rewards  
- **Data Pipeline Fun**: Add personality to your data workflows
- **Content Generation**: Random inspirational content for apps/websites
- **A/B Testing**: Different imagery for user engagement experiments

## 🚀 Publishing Your Plugin

1. Update your card images and metadata
2. Test locally to ensure everything works
3. Run `python main.py package -m "Initial release" "v0.1.0" .`
4. Run `cloudquery plugin publish -f` to publish to CloudQuery registry

## 🔮 Future Enhancements

Want to extend this plugin? Ideas:
- Add card orientation (upright/reversed)
- Include zodiac information  
- Add multiple card spreads (3-card, Celtic Cross)
- Integrate with AI image generation APIs
- Add card reading interpretations

## 📚 Resources

- [CloudQuery Plugin Development](https://docs.cloudquery.io/docs/developers/creating-new-plugin/python-source)
- [CloudQuery Architecture](https://www.cloudquery.io/docs/developers/architecture)
- [Python SDK Reference](https://github.com/cloudquery/plugin-sdk-python)
