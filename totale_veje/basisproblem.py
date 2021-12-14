T = 12
q_min = 0
q_max = 10
o_max = 4
i_max = 4
q_start = 5


def neighbor_intvl(q_t):
    a = q_t - o_max if q_t - o_max >= q_min else q_min
    b = q_t + i_max if q_t + i_max <= q_max else q_max
    return a, b + 1


def paths(q_start, T):
    paths_count = {0: {(0, q_start): 1}}
    for t in range(T):
        paths_count[t + 1] = {(t + 1, q_t): 0 for q_t in range(q_min, q_max + 1)}
        for end_vertex in paths_count[t]:
            repeats = paths_count[t][end_vertex]
            for q in range(*neighbor_intvl(end_vertex[1])):
                paths_count[t + 1][(t + 1, q)] += repeats
    return sum(paths_count[T].values())


print(paths(q_start, T))
