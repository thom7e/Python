import numpy as np
inp = 265149

def part_1(number_to_check):
    arr_0 = [[0] * 1000] * 1000
    arr = np.array(arr_0, dtype=int)
    start = (25, 25)
    col, row = start

    arr[col, row] = 1
    row += 1
    arr[col, row] = 2
    x = 3
    while True:
        while True:

            col -= 1
            arr[col,row] = str(x)
            x+=1

            if arr[col-1,row-1] == 0:
                break
            else:
                col -= 1
                arr[col,row] = x
                x += 1

        # LEFT
        while True:

            row -= 1
            arr[col, row] = x
            x += 1

            if arr[col + 1, row - 1] == 0:
                row -= 1
                arr[col, row] = x
                x += 1
                break
            else:
                row -= 1
                arr[col, row] = x
                x += 1
        #DOWN
        while True:

            #row -= 1
            col += 1
            arr[col,row] = x
            x+=1

            if arr[col+1,row+1] == 0:
                col += 1
                arr[col, row] = x
                x += 1
                break
            else:
                col += 1
                arr[col, row] = x
                x += 1
        # RIGHT
        while True:

            row += 1
            arr[col, row] = x
            x += 1

            if arr[col - 1, row + 1] == 0:
                break
            else:
                row += 1
                arr[col, row] = x
                x += 1
        if x >= number_to_check:
            answer = (abs(np.where(arr == number_to_check)[0][0]-25)+abs(np.where(arr == number_to_check)[1][0]-25))
            return answer

print(part_1(inp))

def check_values(arr,col,row):
    checks = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
    summe = []

    for x,y in checks:
        if summe != 0:
            summe.append(arr[col+x,row+y])

    return sum(summe)


def part_2(number_to_check):
    arr_0 = [[0] * 1000] * 1000
    arr = np.array(arr_0, dtype=int)

    start = (25, 25)
    col, row = start

    arr[col, row] = 1
    row += 1
    arr[col, row] = 1
    while True:
        while True:
            col -= 1
            arr[col, row] = check_values(arr,col,row)
            if check_values(arr, col, row) >= number_to_check:
                return check_values(arr, col, row)

            if arr[col - 1, row - 1] == 0:
                break
            else:
                col -= 1
                arr[col, row] = check_values(arr,col,row)
                if check_values(arr,col,row) >= number_to_check:
                    print(arr[21:33, 21:33])
                    return check_values(arr,col,row)

        # LEFT
        while True:

            row -= 1
            arr[col, row] = check_values(arr,col,row)
            if check_values(arr, col, row) >= number_to_check:
                return check_values(arr, col, row)


            if arr[col + 1, row - 1] == 0:
                row -= 1
                arr[col, row] = check_values(arr,col,row)

                break
            else:
                row -= 1
                arr[col, row] = check_values(arr,col,row)

                if check_values(arr,col,row) >= number_to_check:
                    return check_values(arr,col,row)
            # DOWN
        while True:

            col += 1
            arr[col, row] = check_values(arr,col,row)
            if check_values(arr, col, row) >= number_to_check:
                return check_values(arr, col, row)
            if arr[col + 1, row + 1] == 0:
                col += 1
                arr[col, row] = check_values(arr,col,row)
                if check_values(arr,col,row) >= number_to_check:
                    return check_values(arr,col,row)
                break
            else:
                col += 1
                arr[col, row] = check_values(arr,col,row)
                if check_values(arr,col,row) >= number_to_check:
                    return check_values(arr,col,row)
        # RIGHT
        while True:

            row += 1
            arr[col, row] = check_values(arr,col,row)
            if check_values(arr, col, row) >= number_to_check:
                return check_values(arr, col, row)
            if arr[col - 1, row + 1] == 0:
                break
            else:
                row += 1
                arr[col, row] = check_values(arr,col,row)
                if check_values(arr,col,row) >= number_to_check:
                    return check_values(arr,col,row)

print(part_2(inp))
