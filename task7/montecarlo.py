import random

def throw_dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def thow_dices_n_times(total_throws):
    amounts = []
    for _ in range(total_throws):
        amounts.append(throw_dices())
    amounts.sort()
    return amounts

def calculate_amounts_count(amounts):
    amounts_count = {}
    for amount in amounts:
        if amount in amounts_count:
            amounts_count[amount] += 1
        else: 
            amounts_count[amount] = 1
    return amounts_count

def calculate_dice_percentages(total_throws):
    amounts = thow_dices_n_times(total_throws)
    amounts_count = calculate_amounts_count(amounts)
    percentages = {}
    for amount, count in amounts_count.items():
        percentage = round((count/total_throws)*100, 2)
        percentages[amount] = {"percentage": percentage, "count": count}
    return percentages

def run_multiple_simulations(simulations, total_throws):
    aggregate_counts = {i: 0 for i in range(2, 13)}
    aggregate_percentages = {i: 0 for i in range(2, 13)}

    for _ in range(simulations):
        percentages = calculate_dice_percentages(total_throws)
        for amount in range(2, 13):
            if amount in percentages:
                aggregate_counts[amount] += percentages[amount]['count']
                aggregate_percentages[amount] += percentages[amount]['percentage']
            else:
                aggregate_counts[amount] += 0
                aggregate_percentages[amount] += 0

    # Обчислення середнього значення
    average_percentages = {
        amount: {
            "average_percentage": round(aggregate_percentages[amount] / simulations, 2),
            "total_count": aggregate_counts[amount]
        } 
        for amount in aggregate_counts
    }
    return average_percentages