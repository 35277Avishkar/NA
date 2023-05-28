n=int(input())

cols=set()
positiveDiag=set()
negativeDiag=set()

sols=[]
board=[['_']*n for i in range(n)]

def backtrack(row,count):
    if row==n:
        copy=[' '.join(row) for row in board]
        sols.append(copy)
        return 

    for col in range(n):
        if col in cols or (row+col) in positiveDiag or (row-col) in negativeDiag:
            continue
        
        cols.add(col)
        positiveDiag.add(row+col)
        negativeDiag.add(row-col)
        board[row][col]='Q'

        backtrack(row+1,count)
        
        cols.remove(col)
        positiveDiag.remove(row+col)
        negativeDiag.remove(row-col)
        board[row][col]='_'
    return 
backtrack(0,0)    
print(len(sols))
for i in sols:
    for j in i:
        print(j)
    print('\n')