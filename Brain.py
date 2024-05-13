from collections import deque
import numpy as np
from sklearn.metrics import hamming_loss

class Brain:
    def __init__(self):
        self.knowledge = np.empty((100, 100), dtype=object)
        self.move_up = (np.array([-1, 0]), self.movup)
        self.move_down = (np.array([1, 0]), self.movdo)
        self.move_left = (np.array([0, -1]), self.movleft)
        self.move_right = (np.array([0, 1]), self.movright)
        self.move_ur = (np.array([-1, 1]), self.movur)
        self.move_ul = (np.array([-1, -1]), self.movul)
        self.move_dr = (np.array([1, 1]), self.movdr)
        self.move_dl = (np.array([1, -1]), self.movdl)

        self.knowledge[0, 0] = self.move_up
        self.knowledge[0, 1] = self.move_down
        self.knowledge[0, 2] = self.move_left
        self.knowledge[0, 3] = self.move_right
        self.knowledge[0, 4] = self.move_ur
        self.knowledge[0, 5] = self.move_ul
        self.knowledge[0, 6] = self.move_dr
        self.knowledge[0, 7] = self.move_dl

    def movup(self, maze, x, y, n, m):
        return 0<=x<n and 0<=y<m and maze[x][y]!='*'

    def movdo(self, maze, x, y, n, m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def movleft(self, maze, x, y, n, m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def movright(self, maze, x, y, n, m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def movur(self, maze, x, y, n, m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def movul(self,maze,x,y,n,m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def movdr(selfmaze, x, y, n, m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def movdl(self,maze,x,y,n,m):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != '*'

    def update_knowledge(self,i,j,knowledge):
        self.knowledge[i][j] = knowledge
