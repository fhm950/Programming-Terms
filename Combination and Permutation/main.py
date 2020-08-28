import itertools

my_list = [1, 2, 3, 4, 5, 6]

# Example 1
combinations = itertools.combinations(my_list, 2)

for c in combinations:
    print(c)

permutations = itertools.permutations(my_list, 2)

for p in permutations:
    print(p)


# Example 2
combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

print([result for result in permutations if sum(result) == 10])


# Example 3
word = 'sample'
my_letter = 'plesam'

combinations = itertools.combinations(my_letter, 6)
permutations = itertools.permutations(my_letter, 6)

for p in permutations:
    print(p)
    if ''.join(p) == word:
        print('Match')
        break
else:
    print('No Match')