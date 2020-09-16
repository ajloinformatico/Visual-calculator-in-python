import random


def random_color():
    number = "#"
    for n in range(6):
        number += str(random.randint(0, 9))
    return number


if __name__ == "__main__":
    print(type(random_color()))
