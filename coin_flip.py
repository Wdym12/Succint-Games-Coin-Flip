import random
import time

def display_coin(result):
    if result == 'Heads':
        print("""
    ╭──────────╮
    │  HEADS  │
    │    🪙    │
    ╰──────────╯
        """)
    else:
        print("""
    ╭──────────╮
    │  TAILS  │
    │    🪙    │
    ╰──────────╯
        """)

def coin_flip():
    print("Welcome to the Coin Flip Game!")
    print("Type 'flip' to toss the coin or 'exit' to end the game.")
    
    while True:
        choice = input("\nWhat would you like to do? ").lower()
        
        if choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        elif choice == 'flip':
            print("\nFlipping the coin...")
            for _ in range(3):
                print("🪙", end='\r')
                time.sleep(0.5)
            result = random.choice(['Heads', 'Tails'])
            print("\nResult:", result)
            display_coin(result)
        else:
            print("Invalid command. Please type 'flip' or 'exit'.")

if __name__ == "__main__":
    coin_flip() 