# 🔮 Feed Your AI Tarot Cards

**Get mystical with your data!** This CloudQuery plugin delivers random tarot card images every time you sync. Perfect for AI training, content generation, or just adding some cosmic energy to your data workflows! ✨

Every time you run CloudQuery sync, you receive:

🎴 **One random tarot card** from a collection of 16 unique cards  
🖼️ **Front & back images** (stored as base64) 
📝 **Card meanings and descriptions** for each draw  
🎯 **Ultra-rare cards** with special rewards (see below!)  

## 🚀 Quick Start

### Step 1: Install CloudQuery
```bash
# macOS
brew install cloudquery/tap/cloudquery

### Step 2: Create Your Config File
Create a file called `tarot-config.yaml`:

```yaml
kind: source
spec:
  name: "tarot-cards"
  registry: "docker"
  path: "ghcr.io/cloudquery/tarot-cards:latest"
  tables: ['*']
  destinations: ["sqlite"]
  spec:
    randomness_seed: null  # Leave null for true randomness!

---
kind: destination
spec:
  name: sqlite
  path: cloudquery/sqlite
  version: "v2.4.11"
  spec:
    connection_string: ./my_tarot_cards.sqlite
```

### Step 3: Draw Your Cards! 🎴
```bash
cloudquery sync tarot-config.yaml
```

**That's it!** Your mystical card is now stored in `my_tarot_cards.sqlite`

## 🔍 View Your Cards

### Quick Card Check
```bash
sqlite3 my_tarot_cards.sqlite "SELECT card_number, card_name FROM tarot_cards ORDER BY sync_time DESC LIMIT 1;"
```

### Extract Visual Images
The cards come with base64-encoded images! If you're unsure, ask ChatGPT how to decode them.

## 🎰 The Rare Card Hunt!

**Here's where it gets exciting!** 

- 🎲 **Cards 1-15**: Regular cards (~6.6% each)
- 🔥 **Card 16 "The Stormcaller"**: **ULTRA-RARE** (only 1% chance!)

### When You Pull The Stormcaller:

🎉 CONGRATULATIONS! 🎉

You pulled the legendary Stormcaller!

Contact chris.r@cloudquery.io with your address for FREE CloudQuery swag (Some shipping restrictions may apply)

**Keep syncing to chase the rare card!** Most people need 50-100 tries! 😈

## ⚡ Pro Tips

### Get More Cards
```bash
# Draw 5 cards quickly
for i in {1..5}; do cloudquery sync tarot-config.yaml; done
```

### Check Your Collection
```bash
sqlite3 my_tarot_cards.sqlite "SELECT card_number, card_name, COUNT(*) as times_pulled FROM tarot_cards GROUP BY card_number ORDER BY card_number;"
```

### Export All Cards
```bash
sqlite3 -header -csv my_tarot_cards.sqlite "SELECT * FROM tarot_cards;" > my_tarot_collection.csv
```