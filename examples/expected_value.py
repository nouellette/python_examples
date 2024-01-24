def expected_value(outcomes):
    total = 0
    probability = 1/len(outcomes)

    for outcome in outcomes:
        product = outcome * probability

        total += product
    return total

# Example: Expected value of a fair six-sided dice roll
dice_outcomes = [1, 2, 3, 4, 5, 6]
ev = expected_value(dice_outcomes)
print("Expected Value:", ev)