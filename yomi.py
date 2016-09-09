import itertools

EDO = ("Enhanced Dark Orbs", 20.04)
ET = ("Extend Time", .5)
HASTE = ("Skill Boost", 1)
RSB = ("Resist Skill Bind", 20)
TPA = ("Two Prong Attack", 1)
RB = ("Recovery Bind", 1)
BR = ("Restistance bind", 1)
AH = ("Auto heal", 500)

OKUN = ("Okuninushi", (EDO, ET, HASTE, RSB, HASTE, TPA, TPA))
PANDA = ("Pandora", (EDO, RB, HASTE, RSB, HASTE, EDO, ET))
AKECHI = ("Akechi", (EDO, RSB, HASTE, EDO))
ANUBIS = ("Anubis", (BR, BR, ET, AH, ET, RSB, HASTE, AH))
SATSU = ("Satsuki", (TPA, RSB, HASTE, TPA, TPA))

AVAILABLE = (OKUN, PANDA, PANDA, AKECHI, ANUBIS, SATSU)

for combo in itertools.combinations(AVAILABLE, 4):
  skills = {
    EDO[0]: 60.12,
    ET[0]: 1.5,
    HASTE[0]: 1,
    RSB[0]: 20,
    TPA[0]: 0,
    RB[0]: 0,
    BR[0]: 0,
    AH[0]: 0
  }
  team = []
  for monster in combo:
    team.append(monster[0])
    for skill in monster[1]:
      skills[skill[0]] += skill[1]
  print(team)
  print(skills)
  print()


