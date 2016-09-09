
# Boards are numbered from bottom left to top right
class Board():
  def __init__(self, width=6, height=5, orbString="", orbTuple=()):
    self._width = width
    self._height = height
    
    self.board = []

    if not orbString and not orbTuple:
      for x in range(width * height):
        board.append(OrbGenereator.generate())

    if orbString:
      self.checkOrbStringValid()
      for char in orbString:
        board.append(new Orb(char))

    if orbTuple:
      self.checkOrbTupleValid():
      for orb in orbTuple:
        board.append(orb)


  def checkOrbStringValid(self):
    if len(orbString) != width * height:
      raise BoardStateException(constants.ORB_STRING_LENGTH_MISMATCH
          .format(strlen=len(orbString), w=width, h=height))

  def checkOrbTupleValid(self):
    pass # TODO

  def eval(self):
     pass # TODO
