import time


def insertion_sort(x: list):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and x[i] > key:
            x[i+1] = x[i]
            i -= 1
        x[i+1] = key
    return x


print("Starting...")
start_time = time.time()
x = [4, 3, 1, 19, 16, 33]
print(insertion_sort(x))
end_time = time.time()
time_measured = (end_time - start_time) * 1000
print(time_measured)

start_time = time.time()
y = [5, 4, 3, 19, 8, 7]
print(insertion_sort(y))
end_time = time.time()
time_measured = (end_time - start_time) * 1000
print(time_measured)

start_time = time.time()
z = [1, 2, 3, 4, 5, 6]
print(insertion_sort(z))
end_time = time.time()
time_measured = (end_time - start_time) * 1000
print(time_measured)





