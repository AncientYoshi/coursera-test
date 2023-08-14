def sum_count(*args, **kwargs):
    sum = 0

    for k, v in kwargs.items():
        sum += v
    return sum


print(sum_count(s=23, j=33, k=6.9))

nums = 34
for i in nums:
    print(i)
