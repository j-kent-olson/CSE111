import random

def main():
    number_list = []

    append_random_numbers(number_list)
    print(number_list)
    append_random_numbers(number_list, 4)
    print(number_list)

def append_random_numbers(numbers_list, quantity = 1):
    for i in range(quantity):
        numbers_list.append(random.randint(1, 100))

def append_random_words():
    pass

if __name__ == "__main__":
    main()