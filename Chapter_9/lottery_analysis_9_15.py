# 9-15 Lottery analysis

import random

def generate_ticket(pool, ticket_size=4):
    """
    Generate a random lottery ticket from the given pool.
    Ensures no duplicate elements in a ticket.
    """
    return tuple(random.sample(pool, ticket_size))

def lottery_analysis():
    # Pool of possible lottery items (numbers and letters)
    pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            'a', 'b', 'c', 'd', 'e']

    # Your fixed ticket
    my_ticket = generate_ticket(pool)
    print(f"My ticket: {my_ticket}")

    # Counter for number of draws
    draws = 0

    # Keep drawing until we match the ticket
    while True:
        draws += 1
        winning_ticket = generate_ticket(pool)

        if winning_ticket == my_ticket:
            print(f"Winning ticket: {winning_ticket}")
            print(f"It took {draws:,} draws to win!")
            break

        # Optional: safety stop to avoid infinite loops in testing
        if draws % 1_000_000 == 0:
            print(f"Still trying... {draws:,} draws so far.")

if __name__ == "__main__":
    lottery_analysis()
