import random

def calculate_damage(strength, item_bonus=0, crit_chance = 10, crit_multi = 2):
    dmg = random.randint(1, strength + item_bonus)
    crit_roll = random.randrange(1, 100)
    if crit_roll <= crit_chance:
        dmg *= crit_multi
        print("Critical hit!")
    return dmg

def draw_cards(draw_deck, draw_amount, hand, discard_deck):
    for i in range(draw_amount):
        if len(draw_deck) == 0:
            print("Shuffling discard deck into draw deck...")
            draw_deck = discard_deck
            discard_deck = []
        card = random.choice(draw_deck)
        draw_deck.remove(card)
        hand.append(card)
        print(f"Drew card: {card}")
        i+=1
    return draw_deck, hand, discard_deck

player_draw_deck = ['Card1', 'Card2', 'Card3', 'Card4', 'Card5']
player_discard_deck = ['Card6', 'Card7', 'Card8']
player_hand = []

player_draw_deck, player_hand, player_discard_deck = draw_cards(player_draw_deck, 7, player_hand, player_discard_deck)
print(f"Player's hand: {player_hand}")