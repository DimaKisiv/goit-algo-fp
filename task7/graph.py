import matplotlib.pyplot as plt

def plot_comparison(average_percentages, theoretical_percentages):
    # Витягуємо значення для осей X і Y
    sums = sorted(theoretical_percentages.keys())
    theoretical_values = [theoretical_percentages[amount] for amount in sums]
    experimental_values = [average_percentages.get(amount, {}).get('average_percentage', 0) for amount in sums]

    # Зсув для розташування стовпців поруч
    bar_width = 0.35
    x_positions = range(len(sums))

    # Створюємо графік
    plt.figure(figsize=(12, 7))
    
    # Теоретичні значення
    plt.bar([p - bar_width/2 for p in x_positions], theoretical_values, width=bar_width, color='red', alpha=0.7, label='Теоретичні ймовірності', edgecolor='black')
    
    # Експериментальні значення
    plt.bar([p + bar_width/2 for p in x_positions], experimental_values, width=bar_width, color='skyblue', alpha=0.7, label='Експериментальні ймовірності', edgecolor='black')
    
    # Підписуємо графік
    plt.xlabel('Сума чисел на двох кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння теоретичних та експериментальних ймовірностей')
    plt.xticks(x_positions, sums)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Додаємо підписи до стовпців, розділяючи їх по висоті
    for i, (theo, exp) in enumerate(zip(theoretical_values, experimental_values)):
        # Підпис для теоретичних значень трохи вище
        plt.text(i - bar_width/2, theo + 0.3, f'{theo:.2f}%', ha='center', color='red')
        # Підпис для експериментальних значень трохи нижче
        plt.text(i + bar_width/2, exp + 0.1, f'{exp:.2f}%', ha='center', color='blue')

    plt.show()