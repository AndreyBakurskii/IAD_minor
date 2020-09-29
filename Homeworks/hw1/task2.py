def to_1_with_rule(n):

    counter = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1

        counter += 1

    return counter


dict_of_numbers_and_counter = dict()

for number in range(1, 1000):
    dict_of_numbers_and_counter[number] = to_1_with_rule(number)

number_with_max_counter = 1
max_counter = 0

for number, counter in dict_of_numbers_and_counter.items():

    if counter > max_counter:
        number_with_max_counter = number
        max_counter = counter

print(f'Number: {number_with_max_counter}, counter: {max_counter}')
