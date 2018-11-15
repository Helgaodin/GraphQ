# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:41:48 2018

@author: Olga
"""
import random as rn
import networkx as nx
import numpy as np
import math
import copy
import matplotlib.pyplot as plt
q = 0.1
N = 1024
p = 0.1
t = 0
Tmin=100

G = nx.erdos_renyi_graph(N, p) 
MatAdj = nx.to_numpy_matrix(G)#ìàòðèöà ñìåæíîñòè 256x256
dura = np.asarray(MatAdj)
MatAdj = copy.deepcopy(dura)

fileName = 'result'+'.txt'
fileMatrixName = 'matrix'+'.txt'

k_all = nx.number_of_edges(G) 
k_for_nodes = np.sum(MatAdj, axis=1)
upper_one=k_for_nodes+1
consti = np.sum(upper_one)
#k_dict=FillDictionary(k_for_nodes)
k_average = np.sum(k_for_nodes)/N
print(N/k_average)

# заполним словарь с валентнотсью вершин
def FillDictionary(k_for_nodes):
    p={}
    for i in range(N):
        print(str(k_for_nodes[i]))
        print(p.get(str(k_for_nodes[i])))
        if (p.get(k_for_nodes[i])): #ключ уже есть
            p[k_for_nodes[i]].append(i)
        else:
            p[k_for_nodes[i]]=[]
            p[k_for_nodes[i]].append(i)
    return p
        
def SwitchEdges(G, Adj, p):
    K = G.edges() 
    noe = G.number_of_edges() 
    k_for_nodes = np.sum(MatAdj, axis=1)
    p=FillDictionary(k_for_nodes)
    random_edges = rn.randint(0,noe-1) 
    A = K[random_edges][0] 
    B = K[random_edges][1] # номера вершин
    q_random=rn.random()
    winner = -1
    l_k=upper_one/consti
    if (q_random > q):
        #higher degree cut
        winner=min(k_for_nodes[A],k_for_nodes[B])
    else:
        #lower degree cut
        winner=max(k_for_nodes[A],k_for_nodes[B])
    while True:
        answer = np.random.choice(k_for_nodes, 1, p=l_k)
        num=rn.randint(0,len(p[answer[0]])-1)
        nodes_link=p[answer[0]][num]
        #теперь линкуемся
        if ((A != nodes_link) and (B != nodes_link) and (G.has_edge(winner,nodes_link)==False)):
            break
    Adj[A][B] = Adj[A][B]-1
    Adj[B][A] = Adj[A][B]
    G.remove_edge(A,B)
    
    Adj[winner][nodes_link] = Adj[winner][nodes_link]+1
    Adj[nodes_link][winner] = Adj[winner][nodes_link]
    G.add_edge(winner, nodes_link)
    return G, Adj, p      

p=FillDictionary(k_for_nodes)
while(t<Tmin):
    G, MAdj, p = SwitchEdges(G, MatAdj, p) 
    t=t+1
    '''
    MatAdj = copy.deepcopy(MAdj)
    if (t%2000 == 0):
        #print(t)
        f = open(fileName, 'a')
        text = str(t) + '\t' + str(Ntrip) +'\t'+ str(Nbw) + '\n'
        f.write(text)
        f.close()
        f = open(fileMatrixName,'w')
        for i in range (N):
            for j in range (N):
                f.write(str(MatAdj[i][j])+'\t')
            f.write('\n')
        f.close()
        if(t%1000000==0):
            fileMil = '2mu'+str(mu)+'step'+str(t)+'.txt'
            f = open(fileMil,'w')
            for i in range (N):
                for j in range (N):
                    f.write(str(MatAdj[i][j])+'\t')
                f.write('\n')
            f.close()'''
