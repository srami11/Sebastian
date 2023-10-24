from operations import (add, sub, multi, div, pote, module)

def game():
    score = 0
    while True:
        print("====== MENU ======"
              "\n1. Add"
              "\n2. Substract"
              "\n3. Multiplicate"
              "\n4. Divide"
              "\n5. Power"
              "\n6. Module"
              "\n0. Exit")
        option = int(input("\nChoice an option: "))

        if option == 0:
            break
        num_1 = input("Enter first number: ")
        num_2 = input("Enter Second number: ")
        answer = int(input("Enter your answer: "))

        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print("Correct!!")
            else:
                print("Incorrect")
        elif option == 2:
            result = sub(num_1, num_2)
            if result == answer:
                score += 1
                print("Correct!!")
            else:
                print("Incorrect")
        elif option == 3:
            result = multi(num_1, num_2)
            if result == answer:
                score += 2
                print("Correct!!")
            else:
                print("Incorrect")
        elif option == 4:
            result = div(num_1, num_2)
            if result == answer:
                score += 2
                print("Correct!!")
            else:
                print("Incorrect")
        elif option == 5:
            result = pote(num_1, num_2)
            if result == answer:
                score += 4
                print("Correct!!")
            else:
                print("Incorrect")
        elif option == 6:
            result = module(num_1, num_2)
            if result == answer:
                score += 4
                print("Correct!!")
            else:
                print("Incorrect")

    print(f"==== GAME OVER ===="
          f"\nYour score is {score}"
          f"\nKeep going!!!")
game()
