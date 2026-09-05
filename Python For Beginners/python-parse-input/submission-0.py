from typing import List

def read_integers() -> List[int]:
    inputs = input()
    list_fin = []
    final = inputs.split(",")

    for x in final:
        list_fin.append(int(x))

    return list_fin

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
