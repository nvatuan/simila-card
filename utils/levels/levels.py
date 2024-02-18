from typing import List
from .abstract import AbstractDimension, AbstractLevel, AbstractRule

class Dimension1D(AbstractDimension):
  """
    Class for a 1D dimension in the game.
  """
  def validate(self):
    if len(self.dimension) != 1:
      raise ValueError("Dimension must be a list of length 1")

class Rules1D(AbstractRule):
  """
    Class for a 1D rule in the game.
  """
  pass

class Level1D(AbstractLevel):
  def validate(self):
    if len(self.dimensions) != 1:
      raise ValueError("Dimensions must be a list of length 1")
    if len(self.layout) != self.dimensions[0]:
      raise ValueError("Layout must be the same length as the dimension")
