import base64
import os
import random
from datetime import datetime
from typing import Dict, Any, Generator

# Default card metadata - replace this with your actual card data
DEFAULT_CARDS = {
    1: {"name": "The Oracle", "description": "The Oracle sees beyond the present moment, showing what can be known when data is clear and structured. Foresight is fed by insight."},
    2: {"name": "The Weaver", "description": "Threads from many sources converge under the Weaver’s hand, forming a single pattern of truth. Every strand matters, every detail is woven in."},
    3: {"name": "The Mirror", "description": "The Mirror reflects what it is given. Feed it noise and you see chaos; feed it structure and clarity, and wisdom looks back at you."},
    4: {"name": "The Alchemist", "description": "The Alchemist transforms the raw and unrefined into something powerful. From chaos emerges order — data gold, ready to spark creation."},
    5: {"name": "The Archivist", "description": "The Archivist safeguards all that has come before. Within its ledgers lies the foundation on which every new discovery stands."},
    6: {"name": "The AWS Well", "description": "From the deep cloud flows endless possibility. The AWS Well is a bottomless source, if one knows how to draw from it."},
    7: {"name": "The Salesforce Tower", "description": "The Tower holds countless stories of connection and exchange. Within its heights, every lead and deal is preserved in light."},
    8: {"name": "The GitHub Codex", "description": "The Codex is a living book of spells — each commit, each branch, another incantation of creation. To read it is to glimpse collaboration itself."},
    9: {"name": "The GCP Forge", "description": "The Forge tempers raw power into scalable form. Sparks become clusters, fire becomes compute, and new patterns are hammered into being."},
    10: {"name": "The Jira Wheel", "description": "The Wheel never stops turning. Tasks close, sprints renew, and the cycle of work continues ever onward."},
    11: {"name": "The Postgres Chalice", "description": "The Chalice offers order to those who drink from it. Rows and columns flow in harmony, a vessel of structured truth."},
    12: {"name": "The Snowflake Crystal", "description": "Each flake is unique, but together they form a perfect lattice. The Crystal grows ever larger, storing every shard of knowledge within its frozen facets."},
    13: {"name": "The Redshift Engine", "description": "The Engine charges forward with unstoppable force. It carries data across vast distances, delivering it with speed and precision."},
    14: {"name": "The BigQuery Star", "description": "The Star shines brightest among the constellations of questions. To query it is to chart a path through the cosmos of data."},
    15: {"name": "The S3 Chest", "description": "The Chest holds endless treasures — logs, objects, secrets, and gold. It is a vault without bottom, waiting to be unlocked."},
    16: {"name": "The Stormcaller", "description": "Lightning bends to his command, chaos becomes structure. Where others see only storm and ruin, CloudQuery carves order from the clouds — turning raw, untamed power into clarity and control."},
}


class TarotClient:
    def __init__(self, randomness_seed: int = None):
        self._randomness_seed = randomness_seed
        self._base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self._images_path = os.path.join(self._base_path, "images")
        
        # Initialize random with seed for reproducible results if provided
        if randomness_seed is not None:
            random.seed(randomness_seed)

    def _load_image_as_base64(self, image_path: str) -> str:
        """Load an image file and convert it to base64 string"""
        try:
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
                base64_string = base64.b64encode(image_data).decode('utf-8')
                return base64_string
        except FileNotFoundError:
            # Return a placeholder if image not found
            return "IMAGE_NOT_FOUND"
        except Exception as e:
            # Return error message if something else goes wrong
            return f"ERROR_LOADING_IMAGE: {str(e)}"

    def get_random_card(self) -> Generator[Dict[str, Any], None, None]:
        """Generate a single random card with front and back images"""
        # Define weighted probabilities: cards 1-15 get equal share of 99%, card 16 gets 1%
        card_numbers = list(range(1, 17))  # [1, 2, 3, ..., 16]
        weights = [6.6] * 15 + [1.0]      # Cards 1-15: 6.6% each, Card 16: 1%
        
        # Select a weighted random card number
        card_number = random.choices(card_numbers, weights=weights, k=1)[0]
        
        # Get card metadata
        card_metadata = DEFAULT_CARDS.get(card_number, {
            "name": f"Card {card_number}",
            "description": "Please provide card description"
        })
        
        # Load front and back images
        front_image_path = os.path.join(self._images_path, "front", f"card_{card_number:02d}.png")
        back_image_path = os.path.join(self._images_path, "back", f"card_{card_number:02d}_back.png")
        
        front_image_base64 = self._load_image_as_base64(front_image_path)
        back_image_base64 = self._load_image_as_base64(back_image_path)
        
        # Add special instructions for the rare card
        special_instructions = None
        if card_number == 16:
            special_instructions = (
                "Congratulations on pulling The Stormcaller! "
                "Reach out to chris.r@cloudquery.io with your address for some free swag. "
                "Some shipping restrictions may apply."
            )
        
        # Create the card response
        card_response = {
            "card_number": card_number,
            "card_name": card_metadata["name"],
            "description": card_metadata["description"],
            "front_image_base64": front_image_base64,
            "back_image_base64": back_image_base64,
            "special_instructions": special_instructions,
            "sync_time": datetime.now(),
        }
        
        yield card_response
