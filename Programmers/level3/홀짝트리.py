def solution_dfs(nodes, edges):
    edge_map = {i: [] for i in nodes}
    for u, v in edges:
        edge_map[u].append(v)
        edge_map[v].append(u)

    visited = set()
    right_tree_count = 0
    reverse_tree_count = 0
    for node in nodes:
        if node in visited:
            continue

        # dfs
        stack = [node]
        right_node_count = 0
        reverse_node_count = 0
        while stack:
            top = stack.pop()
            visited.add(top)
            # 이미 방문한 parent 빼고 stack에 넣어줌
            for child in edge_map[top]:
                if child not in visited:
                    stack.append(child)

            if top % 2 == len(edge_map[top]) % 2:
                # 홀짝노드
                right_node_count += 1
            else:
                # 역홀짝노드
                reverse_node_count += 1

        # 홀짝노드가 하나인 트리만 그 노드를 root로 사용해서 홀짝트리가 될 수 있음
        if right_node_count == 1:
            right_tree_count += 1
        # 역홀짝트리도 마찬가지
        if reverse_node_count == 1:
            reverse_tree_count += 1

    return [right_tree_count, reverse_tree_count]


def solution_union_find(nodes, edges):
    # Initialize parent and rank dictionaries.
    parent = {v: v for v in nodes}
    rank = {v: 0 for v in nodes}

    def find(v):
        """Find the root of v with path compression."""
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        """Union the sets that contain v1 and v2 using union by rank."""
        root1 = find(v1)
        root2 = find(v2)
        if root1 == root2:
            return  # Already in the same group.
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

    # Process each edge to union the connected vertices.
    for u, v in edges:
        union(u, v)

    # Group vertices by their root.
    groups = {}
    for v in nodes:
        root = find(v)
        groups.setdefault(root, []).append(v)

    num_incident_edges = {i: 0 for i in nodes}
    for u, v in edges:
        num_incident_edges[u] += 1
        num_incident_edges[v] += 1

    right_tree_count = 0
    reverse_tree_count = 0
    for group in groups.values():
        right_node_count = 0
        reverse_node_count = 0
        for node in group:
            if node % 2 == num_incident_edges[node] % 2:
                right_node_count += 1
            else:
                reverse_node_count += 1

        if right_node_count == 1:
            right_tree_count += 1
        if reverse_node_count == 1:
            reverse_tree_count += 1

    return [right_tree_count, reverse_tree_count]


def solution(nodes, edges):
    # return solution_union_find(nodes, edges)
    return solution_dfs(nodes, edges)


if __name__ == '__main__':
    print(solution([11, 9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]]))
    print(solution([2, 1], [[1, 2]]))
