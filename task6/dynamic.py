def dynamic_programming(items, budget, single_item=False):
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        for j in range(budget + 1):
            if cost <= j:
                if single_item:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_food = {}
    used_budget = 0
    total_calories = dp[n][budget]
    remaining_budget = budget

    i = n
    while i > 0 and remaining_budget > 0:
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        
        if single_item:
            if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
                selected_food[item_name] = 1
                used_budget += cost
                remaining_budget -= cost
        else:
            while remaining_budget >= cost and dp[i][remaining_budget] == dp[i][remaining_budget - cost] + calories:
                if item_name in selected_food:
                    selected_food[item_name] += 1
                else:
                    selected_food[item_name] = 1
                used_budget += cost
                remaining_budget -= cost

        i -= 1

    return selected_food, used_budget, total_calories


