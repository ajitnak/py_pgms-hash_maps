#[12,3,4,6,7,9,10,3, 6,4,4], 3 => [3,6]
import collections

def max_freq_items(arr, n):
	count_dict = collections.defaultdict(int)
	for i in arr:
		count_dict[i] += 1
	print count_dict
	# allocate an arr of size len(dict)	
	freq_list = [None]*(len(arr)+1)
	for i in range(len(arr)):
		freq_list[i] = []
	for k,v in count_dict.items():
		freq_list[v].append(k)
	print freq_list

	result = []
	for i in  range(len(freq_list)-1, -1, -1):
		items= freq_list[i]
		if items:
			if n - len(result) > len(items):
				result.extend(items)
			else:
				result.extend(items[:n - len(result)])
	return result

print max_freq_items([12,3,4,6,7,9,10,3, 6,4,4], 2)
