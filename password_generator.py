import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)

    plen = int(input("Enter Password length\n")) #To handle gibberish
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4)) # all of this creates a total list of all characters used in the password
    #print(s)

    #random.shuffle(s)
    #print(s)
    print("Your password is: ")
    print("".join(random.sample(s,plen)))