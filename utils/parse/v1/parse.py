import json
from ...cards import UnoCard, PokerCard
from ...levels import Level1D, Rules1D, Dimension1D

def get_card_class(card_type: str) -> type:
  if card_type == 'Poker':
    return PokerCard
  if card_type == 'Uno':
    return UnoCard
  raise ValueError("Invalid card type")

def parse_card(data):
  card_class = get_card_class(data['type'])
  card = card_class(value=data['value'],
                    color=data['color'],
                    symbol=data['symbol'])
  card.validate()
  return card

def parse_layout(data):
  layout = [None for _ in range(len(data))] 
  for i in range(len(layout)):
    if data[i] is None:
      continue
    layout[i] = parse_card(data[i])
  return layout

def parse_deck(data):
  deck = [None for _ in range(len(data))] 
  for i in range(len(deck)):
    deck[i] = parse_card(data[i])
  return deck

def parse_level(file_name: str) -> Level:
  with open(file_name, 'r') as fstream:
    data = json.load(fstream)
    dim = Dimension1D(data['dimensions'])
    rules = Rules1D(data['rules'])
    layout = parse_layout(data['layout'])
    deck = parse_deck(data['deck'])

    level = Level1D(dim, rules)
    level.layout = layout
    level.deck = deck
