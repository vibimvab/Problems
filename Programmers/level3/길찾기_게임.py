from sys import setrecursionlimit


def build_graph(root_index, node_x_sorted, left, right, graph, point_to_index, point_to_node_num, pre_order, post_order):
    root_node_num = point_to_node_num[tuple(node_x_sorted[root_index])]
    if root_index >= 1:
        left_child = max(node_x_sorted[left: root_index], key=lambda p: p[1], default=[-1, -1])
    else:
        left_child = (-1, -1)
    if right >= 0:
        right_child = max(node_x_sorted[root_index+1: right+1], key=lambda p: p[1], default=[-1, -1])
    else:
        right_child = (-1, -1)
    graph[root_node_num] = [point_to_node_num[tuple(left_child)], point_to_node_num[tuple(right_child)]]

    pre_order.append(root_node_num+1)

    if graph[root_node_num][0] != -1:
        build_graph(point_to_index[tuple(left_child)], node_x_sorted, left, root_index-1, graph, point_to_index, point_to_node_num, pre_order, post_order)

    if graph[root_node_num][1] != -1:
        build_graph(point_to_index[tuple(right_child)], node_x_sorted, root_index+1, right, graph, point_to_index, point_to_node_num, pre_order, post_order)

    post_order.append(root_node_num+1)


def solution(nodeinfo):
    point_to_node_num = {(-1, -1): -1}
    for i, node in enumerate(nodeinfo):
        point_to_node_num[tuple(node)] = i

    node_x_sorted = sorted(nodeinfo, key=lambda p: p[0])
    point_to_index = {tuple(node): i for i, node in enumerate(node_x_sorted)}
    print(node_x_sorted)

    graph = {}
    root = max(nodeinfo, key=lambda p: p[1])
    pre_order = []
    post_order = []
    setrecursionlimit(max(len(nodeinfo) + 10, 1000))
    build_graph(point_to_index[tuple(root)], node_x_sorted, 0, len(nodeinfo)-1, graph, point_to_index, point_to_node_num, pre_order, post_order)
    setrecursionlimit(1000)

    return [pre_order, post_order]


if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
