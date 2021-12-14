import numpy as np
from math import exp

q_min = [0, 0, 0, 4, 4, 6, 6, 4, 4, 0, 0, 0]
q_max = [10, 10, 10, 10, 8, 8, 8, 8, 10, 10, 10, 10]
o_max = [4, 4, 2, 2, 1, 1, 1, 1, 2, 2, 4, 4]
i_max = [4, 4, 2, 2, 1, 1, 1, 1, 2, 2, 4, 4]
T = 12
p_t = [20, 22, 25, 18, 15, 15, 20, 19, 21, 12, 22, 25]
r = 0.04
alpha = 0.7
q_start = 5
q_goal = 5


add = max(p_t) * max(o_max)

graph = {(0, q_start): {}}


def neighbor_intvl(t, q):
    a = q_min[t] if q - o_max[t] < q_min[t] else q - o_max[t]
    b = q_max[t] if q + i_max[t] > q_max[t] else q + i_max[t]
    return a, b + 1


for q_0 in range(*neighbor_intvl(0, q_start)):
    if q_0 > q_start + i_max[0] or q_0 < q_start - o_max[1]:
        continue
    graph[0, q_start][1, q_0] = exp(-r * (1 / T)) * (q_0 - q_start) * p_t[0] + add

for t in range(1, T):
    for q_t in range(q_min[t - 1], q_max[t - 1] + 1):
        graph[t, q_t] = {}
        for i in range(*neighbor_intvl(t, q_t)):
            if i > q_t + i_max[t] or i < q_t - o_max[t]:
                continue
            graph[t, q_t][t + 1, i] = exp(-r * ((t + 1) / T)) * (i - q_t) * p_t[t] + add


for q_T in range(q_min[T - 1], q_max[T - 1] + 1):
    graph[T, q_T] = {}

dist = {v: np.inf for v in graph.keys()}
path = {v: [] for v in graph.keys()}

start = (0, q_start)
dist[start] = 0

unvisited = [v for v in graph.keys()]

while unvisited:
    u = min(unvisited, key=dist.get)
    unvisited.remove(u)
    for v in graph[u]:
        alt_dist = dist[u] + graph[u][v]
        if alt_dist < dist[v]:
            dist[v] = alt_dist
            path[v] = path[u] + [u]

profit = {
    (T, q_T): -1 * (dist[(T, q_T)] - add * T) + exp(-r) * q_T * p_t[T - 1]
    if q_T == q_goal
    else -1 * (dist[(T, q_T)] - add * T) + exp(-r) * q_T * p_t[T - 1] * (1 - alpha)
    for q_T in range(q_min[T - 1], q_max[T - 1] + 1)
}

optimal_end = max(profit, key=profit.get)
max_profit = profit[optimal_end]
optimal_path = path[optimal_end] + [optimal_end]

print(
    f"Det optimale antal enheder i slutningen er {optimal_end[1]}, hvilket giver indtjeningen {round(max_profit,2)} ved at benytte vejen \n {optimal_path}."
)
