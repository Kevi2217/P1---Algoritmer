import numpy as np
from math import exp

q_min = 0
q_max = 10
o_max = 4
i_max = 4
T = 12
p_t = [20, 22, 25, 18, 15, 15, 20, 19, 21, 12, 22, 25]
r = 0.04
q_start = 5


def neighbor_intvl(q_t):
    a = q_t - o_max if q_t - o_max >= q_min else q_min
    b = q_t + i_max if q_t + i_max <= q_max else q_max
    return a, b + 1


dist = {0: {(0, q_start): 0}}
path = {
    t: {(t, q_t): [(0, q_start)] for q_t in range(q_min, q_max + 1)}
    for t in range(T + 1)
}
for t in range(T):
    dist[t + 1] = {(t + 1, q_t): np.inf for q_t in range(q_min, q_max + 1)}
    for u in dist[t]:
        for v in range(*neighbor_intvl(u[1])):
            alt_dist = dist[t][u] + exp(-r * ((t + 1) / T)) * (v - u[1]) * p_t[t]
            if alt_dist < dist[t + 1][t + 1, v]:
                dist[t + 1][t + 1, v] = alt_dist
                path[t + 1][t + 1, v] = path[t][u] + [(t + 1, v)]
for u in dist[T]:
    dist[T][u] += exp(-r) * (0 - u[1]) * p_t[T - 1]

optimal_end = min(dist[T], key=dist[T].get)
max_profit = -dist[T][optimal_end]
optimal_path = path[T][optimal_end]

print(
    f"Det optimale antal enheder i slutningen er {optimal_end[1]}, hvilket giver indtjeningen {round(max_profit,2)} ved at benytte vejen \n {optimal_path}."
)
