n=int(input())
a=[input().split() for _ in range(n)]
a.sort(key=lambda z:(int(z[0]),int(z[1])))

p={}
g={}

for u,v,d in a:
    u,v=int(u),int(v)

    if u not in p:
        p[u]=(0,0)
        g[(0,0)]=u

    x,y=p[u]
    dx,dy={'top':(0,1),'down':(0,-1),
           'left':(-1,0),'right':(1,0)}[d]
    q=(x+dx,y+dy)

    if v in p:
        del g[p[v]]

    if q in g:
        del p[g[q]]

    p[v]=q
    g[q]=v

t=int(input())
x,y=p[t]

print(g.get((x,y+1),-1),
      g.get((x,y-1),-1),
      g.get((x-1,y),-1),
      g.get((x+1,y),-1))