from typing import List


class Solution:
    # time complexity = num_recipes * ingredients[k].length + num_supplies * num_recipes
    # used_by dictionary is technically a graph and num_ingredients is the number of outgoing edges from a node
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        used_by = {}  # key: ingredient names, value: names of the recipes using it as a list
        num_ingredients = {}  # key: recipie names, value: number of ingredients required
        solution = []
        for recipie_num in range(len(recipes)):
            num_ingredients[recipes[recipie_num]] = len(ingredients[recipie_num])
            for ingredient in ingredients[recipie_num]:
                try:
                    used_by[ingredient].append(recipes[recipie_num])
                except KeyError:
                    used_by[ingredient] = [recipes[recipie_num]]  # note that the value is a list

        for supply in supplies:
            self.handle_ingredients_decrement(num_ingredients, used_by, supply, solution)

        return solution

    def handle_ingredients_decrement(self, num_ingredients, used_by, supply, solution):
        # technically this is a dfs in the graph, or topological ordering!
        # I realized what I made is actually that after finishing my code
        try:
            for recipie in used_by[supply]:
                num_ingredients[recipie] -= 1
                if num_ingredients[recipie] == 0:  # when the recipie can be completed
                    solution.append(recipie)
                    # treat the recipie as another supply
                    self.handle_ingredients_decrement(num_ingredients, used_by, recipie, solution)

        except KeyError:
            # if the supply is not used
            pass


if __name__ == '__main__':
    s = Solution()
    print(s.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]))
