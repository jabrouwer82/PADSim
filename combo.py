from orb import OrbType
from itertools import ifilter

class Combo(object):
  def __init__(self, orbs):
    self.orbs = orbs
    self.enhanced = len(ifilter(lambda o: o.enhanced, orbs)
