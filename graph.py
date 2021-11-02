from math import exp

T = 12
q_min = 0
q_max = 10
i_max = 4
u_max = 4
p_t = [20, 22, 25, 18, 15, 15, 20, 19, 21, 12, 22, 25]
r = 0.04
add = max(p_t) * u_max + 1
q_start = 5

graph = {}
graph[0, q_start] = {}


def determine_neighbors(e):
    if e - u_max <= q_min:
        a = q_min
    else:
        a = e - u_max
    if e + i_max >= q_max:
        b = q_max
    else:
        b = e + i_max
    return a, b


for e in range(
        determine_neighbors(q_start)[0],
        determine_neighbors(q_start)[1] + 1):
    graph[0, q_start][1, e] = exp(r * (-1 / T)) * (e - q_start) * p_t[0] + add

for t in range(1, T):
    for e in range(q_min, q_max + 1):
        graph[(t, e)] = {}
        a, b = determine_neighbors(e)
        for i in range(a, b + 1):
            graph[t, e][t + 1, i] = exp(r * (-(t + 1) / T)) * \
                (i - e) * p_t[t] + add

for e in range(0, 11):
    graph[(T, e)] = {}

print(graph)
