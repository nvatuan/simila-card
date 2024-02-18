from typing import Optional, List

class AbstractDimension:
  """
    Abstract class for a dimension in the game.
  """

  def __init__(self, dimarray: List[int]) -> None:
    self.dimension_constraints_msg = "Dimension must be a list of integers"

    self.dimension = dimarray
    self.validate()
  
  def validate(self):
    if self.dimension is None:
      raise ValueError("Dimension cannot be None")
    
    if len(self.dimension) == 0:
      raise ValueError("Dimension cannot be empty")

class AbstractRule:
  """
    Abstract class for a rule in the game.
  """

  def __init__(self, rules: str) -> None:
    self.match_color = False
    self.match_numer = False
    self.match_symbol = False

    for token in rules.split('|'):
      if token == 'color':
        self.match_color = True
      elif token == 'number':
        self.match_number = True
      elif token == 'symbol':
        self.match_symbol = True
      else:
        raise ValueError(f"Invalid rule token: {token}")
  
  def __set_field(self, field: str, value: bool) -> 'AbstractRule':
    setattr(self, field, value)
    return self
  
  def set_match_color(self, value: bool) -> 'AbstractRule':
    return self.__set_field('match_color', value)

  def set_match_number(self, value: bool) -> 'AbstractRule':
    return self.__set_field('match_number', value)

  def set_match_symbol(self, value: bool) -> 'AbstractRule':
    return self.__set_field('match_symbol', value)

class AbstractLevel:
  """
    Abstract class for a level in the game.
  """

  def __init__(self, dimension: List[int], rules: AbstractRule) -> None:
    self.dimensions = dimension 
    self.rules = rules
    self.layout = []
  
  def validate(self):
    pass

  def parse_layout(self, data) -> None:
    pass