from .abstract import AbstractCard
from ..constants import Colors

class PokerCardValues:
  UNIVERSAL = 'Universal' # Special value to match every thing
  # --
  ONE = '1'
  TWO = '2'
  THREE = '3'
  FOUR = '4'
  FIVE = '5'
  SIX = '6'
  SEVEN = '7'
  EIGHT = '8'
  NINE = '9'
  TEN = '10'
  JACK = 'J'
  QUEEN = 'Q'
  KING = 'K'
  ACE = 'A'

class PokerCardSymbols:
  UNIVERSAL = 'Universal' # Special value to match every thing
  # --
  HEART = 'H'
  DIAMOND = 'D'
  CLUB = 'C'
  SPADE = 'S'

class PokerCard(AbstractCard):
  VALID_VALUES = [
    PokerCardValues.ONE, PokerCardValues.TWO, PokerCardValues.THREE,
    PokerCardValues.FOUR, PokerCardValues.FIVE, PokerCardValues.SIX, PokerCardValues.SEVEN, 
    PokerCardValues.EIGHT, PokerCardValues.NINE, PokerCardValues.TEN, PokerCardValues.JACK,
    PokerCardValues.QUEEN, PokerCardValues.KING, PokerCardValues.ACE
  ]
  VALID_SYMBOLS = [
    PokerCardSymbols.HEART, PokerCardSymbols.DIAMOND, PokerCardSymbols.CLUB, PokerCardSymbols.SPADE
  ]
  VALID_COLORS = [Colors.RED, Colors.BLACK]

  def __validate_value(self, value):
    if value not in PokerCard.VALID_VALUES:
      raise ValueError("Invalid value. Value must be in %s." % PokerCard.VALID_VALUES)

  def __validate_symbol(self, symbol):
    if symbol not in PokerCard.VALID_SYMBOLS:
      raise ValueError("Invalid symbol. Symbol must be in %s." % PokerCard.VALID_SYMBOLS)

  def __validate_color(self, color):
    if color not in PokerCard.VALID_COLORS:
      raise ValueError("Invalid color. Color must be in %s." % PokerCard.VALID_COLORS)
    
    if self.symbol() in [PokerCardSymbols.HEART, PokerCardSymbols.DIAMOND]:
      if color != Colors.RED:
        raise ValueError("Invalid color. Color must be RED for symbol %s" % self.symbol())
    else:
      if color != Colors.BLACK:
        raise ValueError("Invalid color. Color must be BLACK for symbol %s" % self.symbol())
    
  def validate(self):
    self.__validate_value(self.number)
    self.__validate_symbol(self.symbol)
    self.__validate_color(self.color)
