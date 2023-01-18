current_guess = 0
current_steps = 0
is_correct_guess = False
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


def is_guess_lower(current_guess):
    if current_guess < target_number:
        return True
    else:
        return False
    

def is_guess_higher(current_guess):
        if current_guess > target_number:
        return True
    else:
        return False


def print_guess_is_lower():
    return print("Your guess is low.")


def print_guess_is_higher():
    return print("Your guess is high.")

    
def main_game_loop():
    while not is_correct_guess:
        global current_guess
        current_guess = get_number_guess()
        increment_steps()
        
        if is_number_guess_correct(current_guess):
            print_number_guess_correct()
        else:
            print_number_steps()
            
        if is_guess_lower():
            print_guess_is_low()
        elif is_guess_higher():
            print_guess_is_high()
            
