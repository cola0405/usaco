from collections import defaultdict, deque

N = int(2e5+10)

edges = defaultdict(list)
incoming_edges = defaultdict(list)
edge_labels = defaultdict(list)

depth = [0]*N
out_degree = [0]*N
next_town = [0]*N
best_edge_label = [0]*N
rank_town = [0]*N
label_sum = [0]*N
town_ids = [0]*N

n, m = map(int, input().split())
for _ in range(m):
    u, v, l = map(int, input().split())
    edges[u].append(v)
    edge_labels[u].append(l)
    incoming_edges[v].append(u)
    out_degree[u] += 1

current_length_towns = []
next_length_towns = []

for i in range(1, n+1):
    if out_degree[i]==0:
        depth[i] = 1
        current_length_towns.append(i)
        label_sum[i] = 0

current_length = 1
while current_length_towns:
    current_length += 1
    for v in current_length_towns:
        for u in incoming_edges[v]:
            out_degree[u] -= 1
            if out_degree[u]==0:
                next_length_towns.append(u)
                depth[u] = current_length
                best_edge_label[u] = int(1e9+7)

    for u in next_length_towns:
        for i in range(len(edges[u])):
            v = edges[u][i]
            l = edge_labels[u][i]
            if depth[v]==current_length-1:
                if l<best_edge_label[u]:        # 当前label值更小可以更新当前路径 label_sum
                    best_edge_label[u] = l
                    next_town[u] = v
                    label_sum[u] = label_sum[v]+l
                elif l==best_edge_label[u] and rank_town[v]<rank_town[next_town[u]]:        # 如果只是label值相等，则看再看更小的 rank
                    next_town[u] = v
                    label_sum[u] = label_sum[v]+l

    cnt = 0
    for u in next_length_towns:
        cnt += 1
        town_ids[cnt] = u


    def cmp(a, b):
        if best_edge_label[a]!=best_edge_label[b]:
            return best_edge_label[a]-best_edge_label[b]
        return rank_town[next_town[a]]-rank_town[next_town[b]]


    town_ids_list = town_ids[1:cnt+1]
    town_ids_list.sort(key=lambda x: (best_edge_label[x], rank_town[next_town[x]]))

    for i, u in enumerate(town_ids_list, start=1):
        rank_town[u] = i

    current_length_towns, next_length_towns = next_length_towns, []

for i in range(1, n+1):
    print(depth[i]-1, label_sum[i])
