from enum import Enum

class ComboShapes(Enum):
  ROW = 1
  TPA = 2

class combo():
  def __init__(self, color, numOrbs=3, shape=None, numEnhanced=0):
    self.color = color
    assert numOrbs >= 3
    self.numOrbs = numOrbs
    self.shape = shape
    self.numEnhanced = numEnhanced

  def __len__(self):
    return self.numOrbs
