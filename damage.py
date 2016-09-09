
def multiplier(combos):
  mults = {
    OrbType.RED: 0,
    OrbType.GREEN: 0,
    OrbType.BLUE: 0,
    OrbType.LIGHT: 0,
    OrbType.DARK: 0
  }
  comboMult = 1 + .25 * (len(combos) - 1)
  for combo in combos:
    mults[combo.color] += comboMult * (1 + .25 * (len(combo) - 3))

  return mults



