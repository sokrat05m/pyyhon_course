var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'
var1 = var1.split()
var2 = var2.split()
var3 = var3.split()
set_1 = set (var2)
set_2 = set (var3)
set_3 = set_1.intersection(set_2)
list_print = list (set_3)
result = [int(item) for item in list_print]
result.sort()
result_1 = [str(item) for item in result]
result = ' '.join(result_1)
print(result)


