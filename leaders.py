class leader():
  @staticmethod
  def multiplier(combos):
    raise NotImplementedError("A leader must have a multiplier defined")

class pandora(leader):
  @staticmethod
  def multiplier(combos):
    mult = 1.25
    longestDarkCombo = 0
    for combo in combos:
      if combo.orbType == OrbType.dark and len(combo) > longestDarkCombo:
         longestDarkCombo = len(combo)
     if longestDarkCombo == 4:
       multi *=2
     if longestDarkCombo == 5:
       multi *= 2.5
     if longestDarkCombo == 6:
       multi *= 3
     if longestDarkCombo == 7:
       multi *= 3.5
     if longestDarkCombo == 8:
       multi *= 4

     return mult

class bastet(leader):
  @staticmethod
  def multiplier(combos):
    if len(combos) == 5:
      return 3
    if len(combos) == 6:
      return 3.5
    if len(combos) == 7:
      return 4

class verdandi(leader):
  @staticmethod
  def multiplier(combos):
    return 3.3
