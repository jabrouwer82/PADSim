from enum import Enum

class OrbType(Enum):
  RED = ('red', 'R')
  BLUE = ('blue', 'B')
  GREEN = ('green', 'G')
  LIGHT = ('light', 'L')
  DARK = ('dark', 'D')
  HEART = ('heart', 'H')
  POISON = ('poison', 'P')
  JAMMER = ('jammer', 'J')

  def __init__(self, string, letter):
    self.string = string
    self.letter = letter

class Orb():
  def __init__(color, enhanced=False, locked=False):
    self.color = color
    self.enhanced = enhanced
    self.locked = locked

  def __str__(self):
    ret = "A {color} "
    if self.enhanced;
      ret += "+"
    if self.locked:
      ret += "locked "
    return ret.format(color=self.color.string)

class OrbGenerator():
  @staticmethod
  def generate():
    return new Orb(OrbType(random.randrange(6)))
