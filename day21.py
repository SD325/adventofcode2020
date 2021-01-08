with open("inputs/day21.txt") as f:
    all_ingredients, alg_ing = [], {}
    for line in f.readlines():
        ing, alg = line.strip()[:-1].split(' (contains ')
        ingredients, allergens = set(ing.split()), alg.split(', ') if ',' in alg else [alg]
        all_ingredients += ingredients
        for aa in allergens:
            alg_ing[aa] = ingredients if aa not in alg_ing else alg_ing[aa] & ingredients
    # Part 1
    print(sum(not any(ii in v for v in alg_ing.values()) for ii in all_ingredients))
    # Part 2
    finished = {}
    while not all(l in finished for l in alg_ing):
        new_finished = {aa: list(ii)[0] for aa, ii in alg_ing.items() if len(ii) == 1 and aa not in finished}
        for aa, ii in new_finished.items():
            for aa2 in alg_ing:
                if aa != aa2 and ii in alg_ing[aa2]:
                    alg_ing[aa2].remove(ii)
        finished.update(new_finished)
    print(','.join([finished[aa] for aa in sorted(finished)]))
