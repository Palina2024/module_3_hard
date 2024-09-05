def calculate_structure_sum(data_):
    total_sum = 0

    if isinstance(data_, (int, float)):
        return data_
    elif isinstance(data_, str):
        return len(data_)
    elif isinstance(data_, (list, tuple, set)):
        for element in data_:
            total_sum += calculate_structure_sum(element)
    elif isinstance(data_, dict):
        for key, value in data_.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
