from typing import Optional, List

class AbstractCard:
  """
    Abstract class for a card in the game.
    Multiple types of cards can be created by extending this class.
    Some types have a value, some don't. So return None if the card doesn't have a value. 
  """

  def __init__(self, symbol: Optional[str], color: Optional[str], value: Optional[str]) -> None:
    self.symbol = symbol
    self.color = color
    self.value = value
  
  def __str__(self) -> Optional[str]:
    return f"{self.value} of {self.symbol}"
  
  def symbol(self) -> Optional[str]:
    return self.symbol
  
  def color(self) -> Optional[str]:
    return self.color
  
  def value(self) -> Optional[str]:
    return self.value

  def validate(self):
    pass
