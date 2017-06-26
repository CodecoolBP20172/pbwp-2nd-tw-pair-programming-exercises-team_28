import random
import string

def passwordgen():
    password = []
    abc = list(string.ascii_lowercase)
    ABC = list(string.ascii_uppercase)
    symbol = ["!","@","#","$","%","^","&","*","(",")","?"]

    for i in range(8,50):
        password.append(random.choice(abc))
        password.append(random.choice(ABC))
        password.append(random.randint(0,9))
        password.append(random.choice(symbol))
        
    password = str(password)
    print(password)
    return password



def main():
    return


if __name__ == '__main__':
    main()

passwordgen()