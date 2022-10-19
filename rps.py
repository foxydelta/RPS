# Victoria Price - 06/17/2022
# Play a game of Rock Paper Scissors with a computer!

# Define the Rock Paper Scissors game as a function and initialize its variables.
def RPS():
    # Import the random module.
    import random
    # How many times rock has been chosen by the user.
    r_count = 0
    # How many times paper has been chosen by the user.
    p_count = 0
    # How many times scissors has been chosen by the user.
    s_count = 0
    # How many times the user won.
    rounds_won = 0
    # How many times the user lost.
    rounds_lost = 0
    # How many times the user tied with the computer.
    rounds_tied = 0
    # How many rounds the user has played with the computer.
    rounds_played = 0
    # Whether or not the user wants to play again.
    game_choice = ""
    # Greet the user.
    print("Hello there! Let's play Rock Paper Scissors!")

    # A rudimentary AI function that checks whether or not the user
    # has chosen a particular weapon more times than the others, and
    # determines the opposite weapon as the computer's choice.
    def check_preferred_weapon(r_count, p_count, s_count):
        # If the user has chosen rock more times than the other weapons, the 
        # computer will choose paper.
        if r_count > p_count and r_count > s_count:
            return "p"
        # If the user has chosen paper more times than the other weapons, the
        # computer will choose scissors.
        elif p_count > r_count and p_count > s_count:
            return "s"
        # If the user has chosen scissors more times than the other weapons, the
        # computer will choose rock.
        elif s_count > r_count and s_count > p_count:
            return "r"
        # If the user has not chosen a particular weapon more than others, the
        # computer will choose a random weapon.
        else:
            return random.choice(["r", "p", "s"])

    # While the user has not chosen the command to quit, continue to play rounds.
    while game_choice != "q":
        # Announce the round.
        print("\nRound " + str(rounds_played + 1) + "!")
        # Get the user's choice of weapon.
        user_choice = input("Make a choice: (R)ock, (P)aper, (S)cissors:, or (Q)uit >")
        # If the user chooses rock, increment the rock count.
        if user_choice.lower() == "r":
            r_count += 1
            rounds_played += 1
            AI_choice = check_preferred_weapon(r_count, p_count, s_count)
            # If the computer chooses rock, the round is a tie.
            if AI_choice == "r":
                print("Rock vs. rock -- It's a tie!")
                rounds_tied += 1
            # If the computer chooses paper, the user loses.
            elif AI_choice == "p":
                print("Rock is covered by paper -- You lose!")
                rounds_lost += 1
            # If the computer chooses scissors, the user wins.
            elif AI_choice == "s":
                print("Rock smashes scissors -- You win!")
                rounds_won += 1
        # If the user chooses paper, increment the paper count.
        elif user_choice.lower() == "p":
            p_count += 1
            rounds_played += 1
            AI_choice = check_preferred_weapon(r_count, p_count, s_count)
            # If the computer chooses rock, the user wins.
            if AI_choice == "r":
                print("Paper covers rock -- You win!")
                rounds_won += 1
            # If the computer chooses paper, the round is a tie.
            elif AI_choice == "p":
                print("Paper vs. paper -- It's a tie!")
                rounds_tied += 1
            # If the computer chooses scissors, the user loses.
            elif AI_choice == "s":
                print("Paper is cut by scissors -- You lose!")
                rounds_lost += 1
        # If the user chooses scissors, increment the scissors count.
        elif user_choice.lower() == "s":
            s_count += 1
            rounds_played += 1
            AI_choice = check_preferred_weapon(r_count, p_count, s_count)
            # If the computer chooses rock, the user loses.
            if AI_choice == "r":
                print("Scissors are smashed by rock -- You lose!")
                rounds_lost += 1
            # If the computer chooses paper, the user wins.
            elif AI_choice == "p":
                print("Scissors cut paper -- You win!")
                rounds_won += 1
            # If the computer chooses scissors, the round is a tie.
            elif AI_choice == "s":
                print("Scissors vs. scissors -- It's a tie!")
                rounds_tied += 1
        # If the user chooses to quit, break the loop.
        elif user_choice.lower() == "q":
            print("\nSorry to see you go. Thanks for playing!")
            break
        # If the user's choice is not one of the four options, ask them to try again.
        # This also resets the round of the game that the user was on.
        else:
            print("Invalid choice. Please try again."
            + "\nYou can only enter R, P, S, or Q.")

    # After the user has chosen to quit, print the results of the game.
    # How many times the user won (and the computer lost).
    print("\nYou won " + str(rounds_won) + " rounds."
    # How many times the user lost (and the computer won).
    + "\nYou lost " + str(rounds_lost) + " rounds."
    # How many times the user tied with the computer.
    + "\nYou tied " + str(rounds_tied) + " rounds."
    # How many rounds the user chose rock.
    + "\nYou chose rock " + str(r_count) + " times."
    # How many rounds the user chose paper.
    + "\nYou chose paper " + str(p_count) + " times."
    # How many rounds the user chose scissors.
    + "\nYou chose scissors " + str(s_count) + " times.")
    return

# Call the RPS function to play the game!
RPS()
