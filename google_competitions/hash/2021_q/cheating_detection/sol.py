from collections import Counter
import statistics

if __name__ == '__main__':
    cases = int(input())
    limit = int(input())
    for case in range(cases):
        player = 0
        q_s = []
        p_s = []

        for p in range(100):
            p_ans = [int(c) for c in input().strip()]
            p_s.append(sum(p_ans))
            q_s.append(p_ans)

        q_diff = []
        for i in range(10_000):
            q_diff.append((i, sum([x[i] for x in q_s])))

        s_qs = sorted(q_diff, key = lambda x: x[1])

        b_pl = {}
        b_pl_list = []
        for q_id, q in enumerate(s_qs[:2000]):
            for pidx, p in enumerate(q_s):
                if p[q[0]] == 1:
                    if pidx not in b_pl:
                        b_pl[pidx] = [q_id]
                    else:
                        b_pl[pidx].append(q_id)

        pl_std = {k: statistics.stdev(v) for k, v in b_pl.items()}
        s = sorted(pl_std.items(), key = lambda x: x[1])
        #print(b_pl[s[-1][0]])


        print(f"Case #{case + 1}: {s[-1][0] + 1}")