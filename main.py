
def greeting():
    username = input("Enter your username: ")
    print(f"Hello {username}, welcome to this terminal")
    
    
def check_prime(thenumber):
    is_prime = True
    for i in range(2,thenumber):
        if thenumber % i == 0:
            is_prime = False
    return is_prime

def checking_prime_user(useranswerprimecheck):
    if check_prime(useranswerprimecheck) == True:
        print("great")
    elif check_prime(useranswerprimecheck) == False:
        print("this is not prime")

def prime_numbers():
    try:
        useranswer = input("Do you know anything about prime numbers? yes/no ")
        if "yes" in useranswer:
            useranswerprimecheck = int(input("can you say one? "))
            checking_prime_user(useranswerprimecheck)
        elif "no" in useranswer:
            useranswerprimecheck = int(input("you should say one. "))
            checking_prime_user(useranswerprimecheck)    
        else:
            useranswerprimecheck = int(input("you should say one. "))
            checking_prime_user(useranswerprimecheck)
    except ValueError:
        print('please enter a number')

while True:
    greeting()
    prime_numbers()
    break