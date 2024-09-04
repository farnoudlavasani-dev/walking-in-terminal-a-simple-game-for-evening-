import math

def greeting():
    """Prompts the user for their name and greets them."""
    username = input("Enter your username: ")
    while username == "":
        print("you sould enter a username")
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
    print("Great! That's a prime number." if is_prime(number) else "This is not a prime number.")

def ask_about_primes():
    """Asks the user for input regarding prime numbers and validates it."""
    while True:
        useranswer = input("Do you know anything about prime numbers? yes/no").strip().lower()
        while useranswer == "":
            print("Please answer 'yes' or 'no'")
            useranswer = input("Do you know anything about prime numbers? yes/no").strip().lower()
        if useranswer == "yes":
            while True:
                try:
                    user_number = int(input("You Should provide a prime number: ")) 
                    break
                except ValueError:
                    print('please enter a number')
            check_user_prime(user_number)
        elif useranswer == "no":
            secretnumber = 0
            guessnumber = input('so, you should guess a number between 0 - 9: ') 
            while guessnumber != secretnumber:
                print("hint: it's a binary number: ")
            print("you win")

        else:
            print("Please answer 'yes' or 'no'")
            useranswer = input("Do you know anything about prime numbers? yes/no").strip().lower()
        



def main():
    """Main function to run the game."""
    greeting()
    ask_about_primes()

if __name__ == "__main__":
    main()