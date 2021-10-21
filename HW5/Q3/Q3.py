def one_way(string_a,string_b):
    if len(string_a) == len(string_b):     # replace or 0 edits
        r = 0
        for i in range(len(string_a)):
            if string_a[i] != string_b[i]:
                r = r+1 
        if r <= 1:
            return True
    elif len(string_a) == len(string_b) + 1:        # insert
        for i in range(len(string_a)):
            if string_b == string_a[:i] + string_a[i+1:]:
                return True
    elif len(string_a) == len(string_b) - 1:      # delete
        return one_way(string_b,string_a)
    return False

# test the output
print(one_way("pale","ple"))
print(one_way("pales","pale"))
print(one_way("pale","bale"))
print(one_way("pale","bake"))

# Edge cases:
print(one_way("pale","pale"))
