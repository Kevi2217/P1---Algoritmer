import numpy as np
from math import exp 

T = 12
p_t = [20, 22, 25, 18, 15, 15, 20, 19, 21, 12, 22, 25]
q_max = 10
q_min = 0
q_start = 5
i_max = 4
u_max = 4
q_0 = 5
r = 0.04
disc = [exp(-r*t/T) for t in range(1, T+1)]
p_disc = [round(p_t[i]*disc[i],2) for i in range(T)]
plus = 250

graph = {}

graph[(q_start,0)] = {}

for e in range(q_start - u_max if q_start - u_max >= q_min else q_min, q_start + i_max + 1 if q_start + i_max +1 <= q_max + 1 else q_max + 1):
    graph[(q_start,0)][(e,1)] = np.exp(r * (-1/T)) * (e-q_start) * p_t[0] + plus

for t in range(1,T):
    for e in range(0,10 + 1):
        graph[(e,t)] = {}
        for i in range(e - u_max if e - u_max >= q_min else q_min, e + i_max + 1 if e + i_max + 1 <= 10 +1 else 11):
            graph[(e,t)][(i,t+1)] = (np.exp(r * (-(t+1)/T)) * (i-e) * p_t[t]) + plus

for e in range(0, 10 + 1):
    graph[(e,T)] = {}

print(graph)

