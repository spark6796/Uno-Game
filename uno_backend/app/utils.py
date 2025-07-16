import random
from .config import colors, cards_per_player
import uuid

def bot_throw_card(x_cards: list, aval_plays: list) -> list:
    
    cards_can_throw = []
    for card in x_cards:
        if any(part in aval_plays for part in card.split('/')) or card in ['special/+4.png', 'special/wild.png']:
            cards_can_throw.append(card)

    if not cards_can_throw:
        return None
    
    return random.choice(cards_can_throw)



def generate_session_key() -> str:
    return str(uuid.uuid4())

def generate_game_key() -> str:
    return str(uuid.uuid4()).replace('-', '')[:6]


def distribute_cards(cards_list: list) -> dict:
    cards_dict = {color: [] for color in colors}

    for color in colors:
        for _ in range(cards_per_player):
            card = random.choice(cards_list)
            cards_dict[color].append(card)
    
    return cards_dict