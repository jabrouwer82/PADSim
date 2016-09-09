import itertools

TPA = ("Two Prong Attack", 1)
HASTE = ("Skill Boost", 1)
EGO = ("Enhanced Green Orbs", 20.04)
RSB = ("Resist Skill Bind", 20)
ET = ("Extend Time", .5)
EHO = ("Enhanced Heart Orbs", 20.04)
RP = ("Resist Poison", 20)
RB = ("Recovery Bind", 1)
BR = ("Restistance bind", 1)

VERD = ("Verdandi", (TPA, HASTE, EGO, RSB, EGO, HASTE, EGO, ET))
VALK = ("Valkyrie", (TPA, EGO, EHO, HASTE, TPA))
MEIMEI = ("MeiMei", (EGO, EGO, TPA, RSB, TPA, HASTE, HASTE, ET))
CUCHU = ("Cu Chu", (EGO, TPA))
WEEJAS = ("Wee Jas", (BR, BR, ET, ET, RB))

AVAILABLE = (VERD, VALK, MEIMEI, CUCHU, WEEJAS)

for combo in itertools.combinations(AVAILABLE, 4):
  skills = {
    EGO[0]: 20.04,
    ET[0]: 1.0,
    HASTE[0]: 1,
    RSB[0]: 20,
    TPA[0]: 1,
    RB[0]: 0,
    RP[0]: 40,
    BR[0]: 0,
    EHO[0]: 0
  }
  team = []
  for monster in combo:
    team.append(monster[0])
    for skill in monster[1]:
      skills[skill[0]] += skill[1]
  print(team)
  print(skills)
  print()


