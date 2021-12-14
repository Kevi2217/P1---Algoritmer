q_min = [0, 0, 0, 4, 4, 6, 6, 4, 4, 0, 0, 0]
q_max = [10, 10, 10, 10, 8, 8, 8, 8, 10, 10, 10, 10]
o_max = [4, 4, 2, 2, 1, 1, 1, 1, 2, 2, 4, 4]
i_max = [4, 4, 2, 2, 1, 1, 1, 1, 2, 2, 4, 4]
q_start = 5
T = 12


def neighbor_intvl(t, q_t):
    a = q_t - o_max[t] if q_t - o_max[t] >= q_min[t] else q_min[t]
    b = q_t + i_max[t] if q_t + i_max[t] <= q_max[t] else q_max[t]
    return a, b + 1


def paths(q_start, T):
    paths_count = {0: {(0, q_start): 1}}
    for t in range(T):
        paths_count[t + 1] = {(t + 1, q_t): 0 for q_t in range(q_min[t], q_max[t] + 1)}
        for end_vertex in paths_count[t]:
            repeats = paths_count[t][end_vertex]
            for q in range(*neighbor_intvl(*end_vertex)):
                paths_count[t + 1][(t + 1, q)] += repeats
    return sum(paths_count[T].values())


print(f"Der er {paths(q_start, T)} veje gennem grafen for det udvidede problem.")
