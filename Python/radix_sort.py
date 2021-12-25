def countingSort(arr, exp1):

	n = len(arr)
	output = [0] * (n)
	count = [0] * (10)

	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]

def radixSort(arr):
	max1 = max(arr)
	exp = 1
	while max1 / exp > 1:
		countingSort(arr, exp)
		exp *= 10

def read_integers(filename):
    with open(filename) as f:
        for index, line in enumerate(f.readlines()):
            if index == 1:
                return [int(x) for x in line.split()]
    return []
def main():
    arr = read_integers('../data/radix_sort_data.txt')
    radixSort(arr)
    for i in range(len(arr)):
        print(arr[i])
if __name__ == '__main__':
    main()


# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher
