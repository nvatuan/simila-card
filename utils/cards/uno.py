from ..interfaces import AbstractCard
from ..constants import Colors

class UnoCardValues:
  UNIVERSAL = 'Universal'
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
  DRAW_TWO = 'Draw Two'
  SKIP = 'Skip'
  WILD = 'Wild'
  WILD_DRAW_FOUR = 'Wild Draw Four'

class UnoCard(AbstractCard):
  VALID_VALUES = [
    UnoCardValues.UNIVERSAL, UnoCardValues.ONE, UnoCardValues.TWO, UnoCardValues.THREE,
    UnoCardValues.FOUR, UnoCardValues.FIVE, UnoCardValues.SIX, UnoCardValues.SEVEN, 
    UnoCardValues.EIGHT, UnoCardValues.NINE, UnoCardValues.TEN, UnoCardValues.DRAW_TWO, 
    UnoCardValues.SKIP, UnoCardValues.WILD, UnoCardValues.WILD_DRAW_FOUR]
  VALID_SYMBOLS=VALID_VALUES
  VALID_COLORS = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.BLACK]

  def __validate_value(self, value):
    if self.value() != self.symbols():
      raise ValueError("Value and symbol must be the same.")
    
    if value not in UnoCard.VALID_VALUES:
      raise ValueError("Invalid value. Value must be in %s." % UnoCard.VALID_VALUES)

  def __validate_symbol(self, symbol):
    if self.value() != self.symbols():
      raise ValueError("Value and symbol must be the same.")

    if symbol not in UnoCard.VALID_SYMBOLS:
      raise ValueError("Invalid symbol. Symbol must be in %s." % UnoCard.VALID_SYMBOLS)

  def __validate_color(self, color):
    if color not in UnoCard.VALID_COLORS:
      raise ValueError("Invalid color. Color must be in %s." % UnoCard.VALID_COLORS)

    if self.symbol() not in [UnoCardValues.WILD, UnoCardValues.WILD_DRAW_FOUR]:
      if color != Colors.BLACK: # Universal here may be useful
        raise ValueError("Invalid color. Color must be BLACK")
    
  def validate(self):
    self.__validate_value(self.number)
    self.__validate_symbol(self.symbol)
    self.__validate_color(self.color)
