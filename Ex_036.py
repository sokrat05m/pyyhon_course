def cakes(recipe, available):
    if len(recipe) > len(available):
        return 0
    for k in recipe.keys():
        if k not in available.keys():
            return 0
    result = {}
    for k, v in available.items():
        for i, j in recipe.items():
            if k == i:
                result[i] = v / j
    return int(min(result.values()))


a = cakes({'cocoa': 10, 'cream': 94, 'crumbles': 30}, {'cream': 1105, 'butter': 6843, 'pears':
    8085, 'eggs': 807, 'cocoa': 8402, 'milk': 2007, 'flour': 112, 'apples': 6489, 'sugar': 7025, 'nuts': 6396})
print(a)
