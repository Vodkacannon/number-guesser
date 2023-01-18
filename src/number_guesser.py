current_steps = 0
target_steps = 10
target_number = 0

def get_number_guess():
    return input("Enter a number to guess: ")


def get_number_range():
    low = input("Enter a lower bound: ")
    high = input("Enter an upper bound: ")
    return (low, high)


def increment_steps():
    global current_steps
    current_steps += 1


def are_steps_less_than_target():
    global current_steps
    global target_steps
    return current_steps < target_steps


def is_number_guess_correct(number_guess):
    return number_guess == target_number


def print_number_steps():
    print("Step " + str(current_steps) + ".")


def print_number_guess_correct():
    print("You got it right in " + str(current_steps) + ".")
