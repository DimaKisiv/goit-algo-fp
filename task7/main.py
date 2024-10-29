from montecarlo import calculate_dice_percentages, run_multiple_simulations
from printer import pretty_print_percentages, print_average_percentages, compare_and_display_results
from graph import plot_comparison

def calculate_theoretical_percentages():
    total_combinations = 36
    theoretical_percentages = {
        2: 1 / total_combinations * 100,
        3: 2 / total_combinations * 100,
        4: 3 / total_combinations * 100,
        5: 4 / total_combinations * 100,
        6: 5 / total_combinations * 100,
        7: 6 / total_combinations * 100,
        8: 5 / total_combinations * 100,
        9: 4 / total_combinations * 100,
        10: 3 / total_combinations * 100,
        11: 2 / total_combinations * 100,
        12: 1 / total_combinations * 100
    }
    return {amount: round(percentage, 2) for amount, percentage in theoretical_percentages.items()}

def main():
    simulations = 1000  
    throws = 36  

    # однієїс симуляції з 36 кидків недостатньо щоб завжди випадали всі суми
    print("\nРезультат однієї симуляції:")
    percentages = calculate_dice_percentages(throws)
    pretty_print_percentages(percentages, 36)

    # результат середніх значень при виокнанні багатьох симуляцій
    print(f"\nСередній результат {simulations} симуляцій:")
    average_percentages = run_multiple_simulations(simulations, throws)
    print_average_percentages(average_percentages, throws, simulations)
    
    #порівняння аналітичних та Монте-Карло результатів
    print(f"\nПорівнюємо аналітичні результати і результат Монте-Карло {simulations} симуляцій:")
    theoretical_percentages = calculate_theoretical_percentages()
    compare_and_display_results(average_percentages, theoretical_percentages, throws, simulations)

    # малюємо графік де видно результати обох варіантів
    plot_comparison(average_percentages, theoretical_percentages)


if __name__ == "__main__":
    main()