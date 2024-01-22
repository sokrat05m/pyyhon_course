data = [{"V": "S001", "V": "S002", "VI": "S001",
        "VI": "S005", "VII": "S005", "V": "S009", "VIII": "S007"}]
print(data[0])
result = set()  # = {} dictionary
for d in data:
    for key in d:
        result.add(d[key])
print(result)

