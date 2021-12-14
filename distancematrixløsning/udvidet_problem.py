import numpy as np
from math import exp

q_min = [0, 0, 0, 4, 4, 6, 6, 4, 4, 0, 0, 0, 0]
q_max = [10, 10, 10, 10, 8, 8, 8, 8, 10, 10, 10, 10, 0]
o_max = [4, 4, 2, 2, 1, 1, 1, 1, 2, 2, 4, 4]
i_max = [4, 4, 2, 2, 1, 1, 1, 1, 2, 2, 4, 4]
T = 12
p_t = [20, 22, 25, 18, 15, 15, 20, 19, 21, 12, 22, 25]
r = 0.04
q_start = 5
q_goal = 5
alpha = 0.7
q_end = "end"


def neighbor_intvl(t, q_t):
    a = q_t - o_max[t] if q_t - o_max[t] >= q_min[t] else q_min[t]
    b = q_t + i_max[t] if q_t + i_max[t] <= q_max[t] else q_max[t]
    return a, b + 1


dist = {0: {(0, q_start): 0}}
path = {
    t: {(t, q_t): [(0, q_start)] for q_t in range(min(q_min), max(q_max) + 1)}
    for t in range(T + 1)
}
for t in range(T):
    dist[t + 1] = {(t + 1, q_t): np.inf for q_t in range(q_min[t], q_max[t] + 1)}
    for u in dist[t]:
        for v in range(*neighbor_intvl(*u)):
            alt_dist = dist[t][u] + exp(-r * ((t + 1) / T)) * (v - u[1]) * p_t[t]
            if alt_dist < dist[t + 1][t + 1, v]:
                dist[t + 1][t + 1, v] = alt_dist
                path[t + 1][t + 1, v] = path[t][u] + [(t + 1, v)]
dist[q_end] = {}
for u in dist[T]:
    dist[q_end][u] = dist[q_end][u] + (
        exp(-r) * (0 - u[1]) * p_t[T - 1]
        if u[1] == q_goal
        else exp(-r) * (0 - u[1]) * p_t[T - 1] * alpha
    )

optimal_end = min(dist[q_end], key=dist[q_end].get)
max_profit = -dist[q_end][optimal_end]
optimal_path = path[T][optimal_end]

print(
    f"Det optimale antal enheder i slutningen er {optimal_end[1]}, hvilket giver indtjeningen {round(max_profit,2)} ved at benytte vejen \n {optimal_path}."
)
