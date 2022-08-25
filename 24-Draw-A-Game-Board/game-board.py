boardsize = 3
gameboard1 = []
gameboard2 = []

for i in range(boardsize*4+1):
    if i % 4:
        gameboard1.append('-')
    else:
        gameboard1.append(' ')

for i in range(boardsize*4+1):
    if not i % 4:
        gameboard2.append('|')
    else:
        gameboard2.append(' ')

for i in range(boardsize):
    print(''.join(gameboard1))
    print(''.join(gameboard2))
print(''.join(gameboard1))


