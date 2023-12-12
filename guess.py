import random

def main():
    smaller = int(input("Enter the smaller number:"))
    larger = int(input("Enter the larger numbe:"))

    myNumber = random.randint(smaller, larger)
    count = 0
    while True:
        count +=1
        userNumber = int(input("Enter your guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too Large")
        else:
            print("you got it in ", count, "tries")
            break
print("change 1")

if __name__ == "__main__":
    main()