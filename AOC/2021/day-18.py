snailfisch = [[[[[9,8],1],2],3],4]

print(snailfisch)

def reduce(snailfish):
    reduced = []
    try:
        for liste1 in snailfish:
            reduced.append([liste1])
            print(f"ich bin liste1 {liste1}")
            for liste2 in liste1:
                reduced.append([liste2])
                for liste3 in liste2:
                    reduced.append([liste3])
                    for liste4 in liste3:
                        reduced.append([liste4])
                        print(f"ich bin liste4 {liste4}")

                        for liste5 in liste4:
                            reduced.append([liste5])
    except:
        reduced.append(snailfish[-1])

    print(reduced[-1])







reduce(snailfisch)