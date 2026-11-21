seq = (["A", "B", "C"], "Hello", ["D", "E", "F"], 5, ["G", "D", "E"])
def check_target_elem(seq, target):
    for i in seq:
        if isinstance(i, list) and target in i:
            print("Found")
            return True

check_target_elem(seq, "G")
