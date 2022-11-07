start_numbers = [14,8,16,0,1,17]

for i in range(5,2019):
    if start_numbers[i] not in start_numbers[:i]:
        next_number = 0
        start_numbers.append(next_number)


    elif start_numbers[i] in start_numbers[:i] and start_numbers[i] not in start_numbers[i-1:i]:
        x = [k for k, j in enumerate(start_numbers) if j == start_numbers[i]]
        if len(x) > 1:
             start_numbers.append(x[-1]-x[-2])
        else:
            start_numbers.append(start_numbers[i] - x[-1]+1)
    else:
        start_numbers.append(1)

print(start_numbers[-1])
print(len(start_numbers))

def memory(nums, turns):
    num_dict = {num: counter + 1 for counter, num in enumerate(nums[:-1])}
    last = nums[-1]
    for i in range(len(nums), turns):
        if last in num_dict:
            new = i - num_dict[last]
        else:
            new = 0
        num_dict[last] = i
        last = new
    return last



nums = [14,8,16,0,1,17]
import timeit
print(timeit.timeit("memory(nums, 1000)", number=1000, globals=locals())*30000000/(1000*1000))
print(memory(nums, 2020))
print(memory(nums, 30000000))
