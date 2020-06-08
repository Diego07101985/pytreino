from itertools import combinations, permutations, product
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia']

for grupo in combinations(pessoas, 2):
    print(grupo)

print("#"*10+"Permutation"+"#"*10)

for grupo in permutations(pessoas, 2):
    print(grupo)


print("#"*10+"Product"+"#"*10)

for grupo in product(pessoas, repeat=2):
    print(grupo)
