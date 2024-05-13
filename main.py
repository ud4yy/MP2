from Utils import Utilities
from Algos import Algos
from Brain import Brain

maze = [
        ['O', 'O', 'O', '*'],
        ['O', '*', '*', 'O'],
        ['O', '*', '*', 'O'],
        ['*', 'O', 'O', 'O']
    ]

n = len(maze)
m = len(maze[0])
vis = [[False] * m for _ in range(n)]

brain = Brain()
util = Utilities()

i,j=Algos.Algorithm(brain,util,maze,n,m)

know = brain.knowledge[i][j]
print(know)