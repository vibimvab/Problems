'''
class Person:
    def __init__(self, id_num, sale):
        self.id_num: int = id_num
        self.sale: int = sale
        self.parent: Optional[Person] = None
        self.children: [Person] = []

    def is_leader(self):
        return self.children and self.parent


class Team:
    def __init__(self, leader: Person):
        self.parent = None
        self.leader = leader
        self.teammates: [Person] = leader.children
        self.child_teams: [Team] = []

    def get_min_sales(self):
        min_sales = self.leader.sale
        for teammate in self.teammates:
            if not teammate.is_leader():
                min_sales = min(min_sales, teammate.sale)

        return min_sales


def find_min_cost_children(root):
    cost = 0
    for child_team in root.child_teams:
        cost += find_min_cost(child_team)

    return cost


def find_min_cost(root):
    candidates = []
    cost = root.get_min_sales()
    for child_team in root.child_teams:
        cost += find_min_cost(child_team)
    candidates.append(cost)

    for i, target_child_team in enumerate(root.child_teams):
        cost = target_child_team.leader.sale + find_min_cost_children(target_child_team)
        for j, other_child_team in enumerate(root.child_teams):
            if i == j:
                continue
            cost += find_min_cost(other_child_team)
        candidates.append(cost)

    return min(candidates)


def graph_creating_solution(sales, links):
    # I have to be faster than this!
    # constructing the people tree
    people: [Person] = []
    for i, sale in enumerate(sales):
        people.append(Person(i+1, sale))
    people_root = people[0]

    for link in links:
        people[link[0]-1].children.append(people[link[1]-1])
        people[link[0]-1].children[-1].parent = people[link[0]-1]

    # construct team tree
    teams_root = Team(people_root)
    team_q = Queue()
    team_q.put(teams_root)
    while not team_q.empty():
        current: Team = team_q.get()
        for teammate in current.teammates:
            if teammate.is_leader():
                child = Team(teammate)
                current.child_teams.append(child)
                team_q.put(child)

    # find the minimum cost
    answer = find_min_cost(teams_root)
    return answer
'''


def get_min_sales(leader, teammates, sales, is_leader):
    min_sales = sales[leader-1]
    for teammate in teammates:
        if not is_leader[teammate-1]:
            min_sales = min(min_sales, sales[teammate-1])

    return min_sales


def find_min_cost_children(root, sales, is_leader, people_graph, teams_graph, memoization) -> int:
    cost = 0
    try:
        for child_team in teams_graph[root]:
            cost += find_min_cost(child_team, sales, is_leader, people_graph, teams_graph, memoization)
    except KeyError:
        pass

    return cost


def find_min_cost(root, sales, is_leader, people_graph, teams_graph, memoization) -> int:
    try:
        return memoization[root]
    except KeyError:
        pass

    candidates = []
    cost = get_min_sales(root, people_graph[root], sales, is_leader)
    try:
        for child_team in teams_graph[root]:
            cost += find_min_cost(child_team, sales, is_leader, people_graph, teams_graph, memoization)
    except KeyError:
        pass
    candidates.append(cost)

    try:
        for i, target_child_team in enumerate(teams_graph[root]):
            cost = sales[target_child_team-1] + find_min_cost_children(target_child_team, sales, is_leader, people_graph, teams_graph, memoization)
            for j, other_child_team in enumerate(teams_graph[root]):
                if i == j:
                    continue
                cost += find_min_cost(other_child_team, sales, is_leader, people_graph, teams_graph, memoization)
            candidates.append(cost)
    except KeyError:
        pass

    cost = min(candidates)
    memoization[root] = min(candidates)
    return cost


def solution(sales, links):
    # construct people graph
    is_leader = [False] * len(sales)
    is_leader[0] = True

    people_graph: dict[int, [int]] = {}
    for link in links:
        is_leader[link[0]-1] = True
        try:
            people_graph[link[0]].append(link[1])
        except KeyError:
            people_graph[link[0]] = [link[1]]

    # construct team graph
    teams_graph: dict[int, [int]] = {}
    for link in links:
        if is_leader[link[1]-1]:
            try:
                teams_graph[link[0]].append(link[1])
            except KeyError:
                teams_graph[link[0]] = [link[1]]

    # find the minimum cost
    memoization: dict[int, int] = {}
    answer = find_min_cost(1, sales, is_leader, people_graph, teams_graph, memoization)
    return answer


if __name__ == '__main__':
    print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))