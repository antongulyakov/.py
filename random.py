def randomlist(n):
	s = [0] * n
	for i in range(n):
		s[i] = random.random()
	return s


def inBucket(list, low, high):
	count = 0
	for num in list:
		if low < num < high:
			count += 1
	return count


def rng(num_buckets):
	buckets = [0] * num_buckets
	bucket_width = 1.0/num_buckets
	high = low = 0.0
	lst = randomlist(1000)
	for i in range(num_buckets):
		low = high
		high += bucket_width
		buckets[i] = inBucket(lst, low, high)
	print(buckets)


def rng2(num_buckets):
	buckets = [0] * num_buckets
	lst = randomlist(1000)
	for i in lst:
		index = int(i * num_buckets)
		buckets[index] = buckets[index] + 1
	print(buckets)
