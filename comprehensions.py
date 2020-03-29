# 1) Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.

print([x for x in range(1, 1001) if '7' in str(x)])

# 2) Взять предложение Would it save you a lot of time if I just gave up and went mad now?
# и сделать его без гласных.

not_so_mad = 'Would it save you a lot of time if I just gave up and went mad now?'
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
pretty_mad = [letter for letter in not_so_mad if letter not in vowels]
print(''.join(map(str, pretty_mad)))

# 3) Для предложения The ships hung in the sky in much the same way that bricks don't
# составить словарь, где слову соответствует его длина.

ships = "The ships hung in the sky in much the same way that bricks don't"
print({word: len(word) for word in ships.split()})

# 4) Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).

print([max([y for y in range(1, 10) if x % y == 0]) for x in range(1, 1001)])

# 5) Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.

print([x for x in range(1, 1001) if not [y for y in range(2, 10) if x % y == 0]])
