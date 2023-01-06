import hashlib

input = "ugkcyxxp"
def part_1():
    pwd = []
    counter = 0
    for number in range(0,99999999):
        string = f"{input}{number}"
        result = hashlib.md5(string.encode())
        if result.hexdigest()[0:5] == "00000":
            pwd.append(result.hexdigest()[5])
            counter += 1
            if counter == 8:
                return "".join(pwd)

def part_2():
    pwd = []
    already_filled = []
    for number in range(0,99999999):
        string = f"{input}{number}"
        result = hashlib.md5(string.encode())
        if result.hexdigest()[0:5] == "00000":
            if result.hexdigest()[5] in ["0","1","2","3","4","5","6","7"]:

                if not result.hexdigest()[5] in already_filled:
                    already_filled.append(result.hexdigest()[5])
                    pwd.append((int(result.hexdigest()[5]),result.hexdigest()[6]))
                    if len(already_filled) == 8:
                        pwd_clear = []
                        for x,y in sorted(pwd):
                            pwd_clear.append(y)
                        return "".join(pwd_clear)

print("PART I:",part_1())
print("PART II:",part_2())
