
def greeting():
    username = input("Enter your username: ")
    print(f"Hello {username}, welcome to this terminal")
def check_prime(thenumber):
    if thenumber % 

def prime_numbers():
    useranswer = input("Do you know anything about prime numbers? yes/no ")
    if "yes" in useranswer:
        useranswerprimecheck = int(input("can you say one? "))
        if useranswerprimecheck == "":
            check_prime(useranswerprimecheck)
    if "no" in useranswer:
        print("you should say one. ")
    else:
        print("you should say one. ")

def section_1():
    greeting()
    print("y")
     
section_1()