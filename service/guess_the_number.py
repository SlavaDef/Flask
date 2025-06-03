from random import randint


def guess_number(user_number,user_number2,user_number3):

    number = randint(1, 10)
    if number == user_number:
        if number != user_number:
            return "Try again!"
        return "You win! the number is "  + str(user_number)
    elif number == user_number2:
        if number != user_number2:
            return "Try again!"
        return "You win! the number is " + str(user_number2)
    elif number == user_number3:
        if number != user_number3:
            return "it s was last chance!"
        return "You win! the number is " + str(user_number3)
    return "You lose my number is " + str(number)



print(guess_number(2,4,6))
#print(guess_number(1))
#print(guess_number(3))
#print(guess_number(8))