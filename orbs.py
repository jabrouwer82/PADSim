from enum import Enum

class OrbType(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3
  LIGHT = 4
  DARK = 5
  HEART = 6
  POISEN = 7
  BLOCK = 8

ORB_ATTRS = {
    OrbType.RED:    {'char': 'r', 'color': 'red'},
    OrbType.GREEN:  {'char': 'g', 'color': 'blue'},
    OrbType.BLUE:   {'char': 'b', 'color': 'green'},
    OrbType.LIGHT:  {'char': 'l', 'color': 'light'},
    OrbType.DARK:   {'char': 'd', 'color': 'dark'},
    OrbType.POISEN: {'char': 'p', 'color': 'poisen'},
    OrbType.BLOCK:  {'char': 'x', 'color': 'block'}
}

class Orb(object):
  def __init__(self, otype, enhanced=False):
    self.otype = otype
    self.enhanced = enhanced

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.otype == other.otype
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    enhanced = ''
    if self.enhanced:
      enhanced = 'n enhanced'
    return 'A{enhanced} {color} orb'.format(
        enhanced=enhanced,
        color=ORB_ATTRS[self.otype]['color'])
