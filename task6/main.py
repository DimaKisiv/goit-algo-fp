from dynamic import dynamic_programming
from greedy import greedy_algorithm

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100



def main():
    # 2 варіанти реалізаціЇ, якщо ми можемо брати багато раз той самий продукт для максимізації калорій, тоді single_item = False
    selected_food_doublicating, total_price_doub, total_calories_doub = greedy_algorithm(items, 100, False) # в даному випадку ми беремо одну колу і тільки коли не вистачає коштів тоді пепсі
    # якщо ми беремо кожен продукт тільки по одному разу
    selected_food_single_item, total_price_single, total_calories_single = greedy_algorithm(items, 100, True) # тоді жадібний алгоритм бере послідовно всі продукти починаючи від найкалорійнішого

    print(F"\n\nЖадібний алгоритм")
    print(F"\nВибрані страви дублюючи самі калорійні продукти: {selected_food_doublicating}")
    print(F"Витрачено бєджету: {total_price_doub}, Кількість калорій: {total_calories_doub}")
    print(F"\nВибрані страви використовуючи всі по одному разу: {selected_food_single_item}")
    print(F"Витрачено бєджету: {total_price_single}, Кількість калорій: {total_calories_single}")

    # 2 варіанти реалізаціЇ, якщо ми можемо брати багато раз той самий продукт для максимізації калорій, тоді single_item = False
    selected_food_dp_multi, used_budget_multi, total_calories_multi = dynamic_programming(items, budget, False)# в даному випадку ми беремо одну колу і тільки коли не вистачає коштів бере картоплю
    # якщо ми беремо кожен продукт тільки по одному разу
    selected_food_dp_single, used_budget_single, total_calories_single = dynamic_programming(items, budget, True)# тоді алгоритм динамічного програмування комбінує так щоб вписатись у весь бєджет і отримати максимум калорій

    print(F"\n\nАлгоритм динамічного програмування")
    print(f"\nВибрані страви дублюючи самі калорійні продукти: {selected_food_dp_multi}")
    print(f"Витрачено бєджету: {used_budget_multi}, Кількість калорій: {total_calories_multi}")
    print(f"\nВибрані страви використовуючи всі по одному разу: {selected_food_dp_single}")
    print(f"Витрачено бєджету: {used_budget_single}, Кількість калорій: {total_calories_single}")

if __name__ == "__main__":
    main()