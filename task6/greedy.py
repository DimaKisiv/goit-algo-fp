def greedy_algorithm(items, budget, single_item = False):
    food_sorted_by_efficiency = [{
        "name": name, 
        "cost": data['cost'],
        "calories": data['calories'], 
        "efficiency":  data['calories'] / data['cost']
    } for name, data in items.items()]
    
    food_sorted_by_efficiency.sort(key=lambda food: food["efficiency"], reverse=True)
    print(F"Страви посортовані по співвідношенню ціна/калорійність:\n")
    for f in food_sorted_by_efficiency:
        print(f)
    
    total_price = 0
    total_calories = 0
    selected_food = {}

    for food_eff_item in food_sorted_by_efficiency:
        while total_price + food_eff_item["cost"] <= budget:
            if food_eff_item["name"] in selected_food:
                selected_food[food_eff_item["name"]] += 1
                total_price += food_eff_item["cost"]
                total_calories += food_eff_item["calories"]
            else:
                selected_food[food_eff_item["name"]] = 1
                total_price += food_eff_item["cost"]
                total_calories += food_eff_item["calories"]
                if single_item:
                    break
    return selected_food, total_price, total_calories


