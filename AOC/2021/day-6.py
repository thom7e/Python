from collections import Counter, defaultdict
with open("day6.in", "r") as file:
    x = file.read().split(",")
print(x)

X = Counter([int(x) for x in open("day6.in").read().strip().split(',')])
print(X.items())
print(X.values())

def thomas_version(x,n):

    for days_ in range(0,n):
        #print(x)
        for checker in range(len(x)):
            x[checker] = int(x[checker])-1

        for true in range(len(x)):
            if x[true] < 0:
                x[true] = int(6)
                x.append(int(8))
    return len(x)

def paulson_version(S,n):
    X = S
    for days_ in range(n):
        Y = defaultdict(int)
        for checker,counter in X.items():
            if checker == 0:
                Y[6] += counter
                Y[8] += counter
            else:
                Y[checker-1] += counter
        X = Y
    return sum(X.values())


#print(thomas_version(x,80))
print(paulson_version(X,256))
