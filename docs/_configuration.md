kind: source
spec:
  # Source spec section
  name: "feed-your-ai-tarot"
  path: "cloudquery/feed-your-ai-tarot"
  registry: "cloudquery"
  version: "VERSION_SOURCE_FEED_YOUR_AI_TAROT"
  tables: ["tarot_cards"]
  destinations: ["DESTINATION_NAME"]
  # Feed Your AI Tarot Spec
  # Learn more about the configuration options at https://github.com/cloudquery/feed-your-ai-tarot
  spec:
    # Optional: Set a seed for reproducible randomness
    # If not set or null, each sync produces truly random cards
    # randomness_seed: 42

---
kind: destination
spec:
  name: "DESTINATION_NAME"
  path: "cloudquery/DESTINATION_NAME"
  registry: "cloudquery"
  version: "VERSION_DESTINATION"
  spec:
    # IMPORTANT: Use append mode to collect multiple cards
    # Default overwrite-delete-stale mode will only keep the latest card
    write_mode: "append"
