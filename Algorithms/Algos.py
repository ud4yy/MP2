from collections import deque
import numpy as np
from sklearn.metrics import hamming_loss
from Brain import Brain
from Utils import Utilities

class Algos:
  @staticmethod
  def T(brain: Brain, util: Utilities,maze,i,j,n,m,vis,exp):
          exp=[]
          q = deque()
          cost = 0
          q.append(((i, j), None, cost))
          vis[i][j] = True
          while q:
              (row, col), move, cost = q.popleft()
              if row == 0 and col == 0:
                  return exp
              if np.random.rand() < 0.1: #p = 0.1
                  random_ind = np.random.randint(0, 7)
                  nr, nc, action = util.R(maze, row, col, n, m, vis,random_ind, brain.knowledge)
                  if nr != -1 and nc != -1:
                      q.append(((nr, nc), action, cost))
                      exp.append((nr, nc, action))  # Include the action in the tuple
                  else:
                      q.append(((row, col), move, cost))
              # exploitation
              else:
                  xd, yd, action = util.F(maze, row, col, n, m, vis, brain.knowledge)
                  vis[xd][yd] = True
                  q.append(((xd, yd), action, cost + 1))
                  exp.append((xd, yd, action))  # Include the action in the tuple
          return exp

  @staticmethod
  def Traverse(brain, maze, exp_i, exp_j, vis, n, m):
      trans = []
      x, y = n - 1, m - 1
      actions = brain.knowledge[exp_i][exp_j][1]
      for nx,ny,action in actions:
          nr = x + action[0]
          nc = y + action[1]
          #print(action)
          if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != '*' and not vis[nr][nc]:
              trans.append((nr, nc, action))
              x, y = nr, nc
              vis[nr][nc] = True
          else:
              return nr, nc, trans
      return nr, nc, trans


  @staticmethod
  def Algorithm(brain: Brain, util: Utilities, maze, n, m):
    encoded_maze = util.maze_to_vector(maze)
    exp = []
    score = -99
    exp_i=0
    exp_j =0
    vis = [[False] * m for _ in range(n)]
    for i in range(0, 100): 
        start_col = 8 if i == 0 else 0  
        for j in range(start_col, 100):  
            if brain.knowledge[i][j] is None:
                break
            else:
                knowledge_item = brain.knowledge[i][j]
                prevmaze, trans = knowledge_item
                #print(prevmaze)
                calc_score = util.calculate_similarity(encoded_maze, prevmaze)
                if score < calc_score:
                    score = calc_score
                    exp_i = i
                    exp_j = j
    if exp_i != 0 or exp_j!=0:
        nr, nc, trans = Algos.Traverse(brain,maze,exp_i,exp_j,vis,n,m)
        if (nr, nc) == (0, 0):
            brain.update_knowledge(exp_i+1,exp_j+1,(encoded_maze, trans))
            return exp_i+1,exp_j+1
        else:
            transs = Algos.T(brain, util, maze, nr, nc, n, m, vis, trans)
            brain.update_knowledge(exp_i+1,exp_j+1,(encoded_maze, transs))
            return exp_i+1,exp_j+1
    else:
        trans = Algos.T(brain, util, maze, n - 1, m - 1, n, m, vis, exp)
        #print(trans)
        brain.update_knowledge(0,8,(encoded_maze, trans))
        return 0,8

