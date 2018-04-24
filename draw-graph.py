#Algorithm: choose two distinct elements a,b from Z_n and find a non-negative integer m(<n) such that m*a=b or m*b=a (modulo n)  
import networkx as nx
import matplotlib.pyplot as plt

n=int(raw_input('Enter an integer n= '))
L=range(n)
V=[]

for i in L:
    #print i
    for j in L:
        if (j!=i):
	    for m in range(n):
                if(i==(j*m)%n) or (j==(i*m)%n):
                    V.append((i,j))
#print len(V),len(set(V))
print V

#========= Adjacency matrix create============
A=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i,j) in V or (j,i) in V:
            A[i][j]=1
        else:
            A[i][j]=0
print A
#========= Adjacency matrix create============

# ++++++++eigen value and eigen vector ++++++
import numpy as NP
from scipy import linalg as LA
e_vals, e_vecs = LA.eig(A)

print "Eigen Values are ", e_vals
print "Eigen vectors are ", e_vecs

# ++++++++eigen value and eigen vector +++++


#---------creating graph----------------

G=nx.path_graph(1)
G.add_edges_from(V)
nx.draw(G,with_labels=True)
plt.savefig("join_edges_path.png") # save as png
plt.show() # display

#---------creating graph----------------

