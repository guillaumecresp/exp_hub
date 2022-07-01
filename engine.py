class Jeu:

  def __init__(self):
    self.plateau = [
      [0,0,0],
      [0,0,0],
      [0,0,0],
    ]
    self.joueur = 1
    self.fin = (False, 0)

  def maj(self, c, l):
    if self.plateau[l][c]!=0:
      return
    else:
      self.plateau[l][c] = self.joueur

    self.fin = self.victoire()
    self.joueur= 2 - (self.joueur-1)

  def victoire(self):
        p  = self.plateau
        for i in range(3):
            if p[i][0]!=0 and p[i][0]==p[i][1]==p[i][2]:
                return (True, p[i][0])
            if p[0][i]!=0 and p[0][i]==p[1][i]==p[2][i]:
                return (True, p[0][i])

        if p[0][0]!=0 and p[0][0]==p[1][1]==p[2][2]:
            return (True, p[0][0])
        if p[2][0]!=0 and p[2][0]==p[1][1]==p[0][2]:
            return (True, p[2][0])
        return (False, 0)