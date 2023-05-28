n=int(input("Enter No. of Nodes::::"))
graph=[[0 for i in range(n)] for j in range(n)]
while (ch:=input("Enter Edges (N to stop)="))!='N':
    x,y=(map(int,ch.split()))
    graph[x][y]=graph[y][x]=1
    
queue=[]
visited=[0 for i in range(n)]
def bfs(node):
    visited[queue.pop(0)]=1
    print(node)
    for i in range(n):
        if graph[node][i]==1 and not visited[i] and i not in queue:
            queue.append(i)
    if not queue:
        return 
    bfs(queue[0])
queue.append(0)
bfs(queue[0])