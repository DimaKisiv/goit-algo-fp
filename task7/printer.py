def pretty_print_percentages(percentages, total_throws):
    print("Сума  Ймовірність")
    print("-----------------------")

    for amount, percentage in percentages.items():
        print(f"{amount}   |   {percentage['percentage']}% ({percentage['count']}/{total_throws})")

def print_average_percentages(average_percentages, total_throws, simulations):
    print("Сума     Середня ймовірність (%)")
    print("----------------------------------")
    for amount, data in sorted(average_percentages.items()):
        print(f"{amount}   |   {data['average_percentage']}% ({data['total_count']/simulations}/{total_throws})")

def compare_and_display_results(average_percentages, theoretical_percentages, total_throws, simulations):
    print("\nСума | Аналітичначна ймовірність (%) | Результат Монте-Карло (%)")
    print("---------------------------------------------------------------")
    for amount in sorted(theoretical_percentages.keys()):
        theoretical = theoretical_percentages[amount]
        experimental = average_percentages.get(amount, {}).get("average_percentage", 0)
        total_count = average_percentages.get(amount, {}).get("total_count", 0)
        print(f"{amount} | {theoretical}% | {experimental}% | ({total_count/simulations}/{total_throws})")