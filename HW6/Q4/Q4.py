def delete_keys(key_list, dictionary):
    for key in key_list:
        if key in dictionary:
            dictionary.pop(key)

# test the output:
test_dict = {"firstName": "Mohamed", "lastName": "Farag", "birthYear": 1990, "nationality": "Egyptian"}
print(f"Test Dict: {test_dict}")
delete_keys(["lastName", "birthYear"], test_dict)
print(f"Dict after delete keys [lastName, birthYear]: {test_dict}")

test_dict = {"A": 1, "B": 2, "C": 3, "D": 4}
print(f"Test Dict: {test_dict}")
delete_keys(["A", "D"], test_dict)
print(f"Dict after delete keys [A, D]: {test_dict}")