import math
import sys

def greeting():
    """Prompts the user for their name and greets them."""
    username = input("Enter your username: ")
    print(f"Hello {username}, welcome to this terminal!")
    
    
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def check_user_prime(number):
    """Informs the user whether the provided number is prime or not."""
    if is_prime(number):
        print("Great! That's a prime number.")
    else:
        print("This is not a prime number.")

def ask_about_primes():
    """Asks the user for input regarding prime numbers and validates it."""
    while True:
        useranswer = input("Do you know anything about prime numbers? yes/no (or type 'quit' to exit): ").strip().lower()
        if useranswer == "quit":
            print("Goodbye!")
            sys.exit()
        elif useranswer in ("yes", "no"):
            break
        print("Please answer 'yes' or 'no'.")
    while True:
        try:
            user_number = int(input("You Should provide a prime number: ")) 
            break
        except ValueError:
            print('please enter a number')
    check_user_prime(user_number)

def main():
    """Main function to run the game."""
    greeting()
    ask_about_primes()

if __name__ == "__main__":
    main()
