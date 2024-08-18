from collections import deque
import numpy as np
from sklearn.metrics import hamming_loss

class Utilities:
    @staticmethod
    def NormalizedH(x1, y1, x2, y2, n, m):
        M = abs(x1 - x2) + abs(y1 - y2)
        normM = M / (n + m)
        E = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        normE = E / ((n + m) ** 0.5)
        return normM * normE

    @staticmethod
    def maze_to_vector(maze):
      return [1 if cell == 'O' else 0 for row in maze for cell in row]

    @staticmethod
    def calculate_similarity(maze1, maze2):
        #vec1 = Utilities.maze_to_vector(maze1)
        #vec2 = Utilities.maze_to_vector(maze2)
        return 1 - hamming_loss(maze1, maze2)

    @staticmethod
    def R(maze, x, y, n, m, vis, ind, knowledge):
      action, rule = knowledge[0, ind]
      nr = x + action[0]
      nc = y + action[1]
      if rule(maze,nr,nc,n,m) and not vis[nr][nc]:
        vis[nr][nc] = True
        return nr, nc, action
      else:
        return -1, -1, None

    @staticmethod
    def F(maze, x, y, n, m, vis,knowledge):
        maxscore = -999
        xd, yd, best_action = 0, 0, None
        for i in range(6):
            action, rule = knowledge[0,i]
            nr = x + action[0]
            nc = y + action[1]
            if rule(maze,nr,nc,n,m) and not vis[nr][nc]:
                score = Utilities.NormalizedH(x, y, nr, nc, n, m)
                if score > maxscore:
                    maxscore = score
                    xd, yd, best_action = nr, nc, action
        return xd, yd, best_action
