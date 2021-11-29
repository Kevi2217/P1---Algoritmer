import numpy as np
import matplotlib.pyplot as plt
from math import exp

q_min = 0
q_max = 10
o_max = 4
i_max = 4
T = 12
p_t = [20, 22, 25, 18, 15, 15, 20, 19, 21, 12, 22, 25]
r = 0.04
q_start = 5

add = max(p_t) * o_max

graph = {(0, q_start): {}}


def neighbor_intvl(q_t):
    a = q_min if q_t - o_max < q_min else q_t - o_max
    b = q_max if q_t + i_max > q_max else q_t + i_max
    return a, b + 1


for q_1 in range(*neighbor_intvl(q_start)):
    graph[0, q_start][1, q_1] = exp(-r * (1 / T)) * (q_1 - q_start) * p_t[0] + add

for t in range(1, T):
    for q_t in range(q_min, q_max + 1):
        graph[t, q_t] = {}
        for q_tp1 in range(*neighbor_intvl(q_t)):
            graph[t, q_t][t + 1, q_tp1] = (
                exp(-r * ((t + 1) / T)) * (q_tp1 - q_t) * p_t[t] + add
            )

graph[("end", 0)] = {}

for q_T in range(q_min, q_max + 1):
    graph[T, q_T] = {}
    graph[T, q_T]["end", 0] = exp(-r) * q_T * p_t[T - 1] - 1200


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
    for q_T in range(q_min, q_max + 1)
}

optimal_end = max(profit, key=profit.get)
max_profit = profit[optimal_end]
optimal_path = path[optimal_end] + [optimal_end]

print(
    f"Det optimale antal enheder i slutningen er {optimal_end[1]}, hvilket giver indtjeningen {round(max_profit,2)} ved at benytte vejen \n {optimal_path}."
)

cash_flow = []
for t in optimal_path:
    cash_flow.append(-1 * (dist[t] - add * t[0]))
cash_flow.append(exp(-r) * optimal_end[1] * p_t[T - 1] + cash_flow[-1])

plt.plot(np.linspace(0, T + 1, T + 2), cash_flow, label="Pengestrøm")
plt.legend()
plt.xlabel("$t$")
plt.ylabel("Indtjening")
plt.xlim(-1, T + 2)
plt.grid(axis="y")
plt.show()
