#!python
from collections import deque

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(range + n) It goes through for each item in the array, creates another array and goes through that for the range between max and min
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(numbers) == 0:
        return
    # Find the min and max values
    max_val = max(numbers)
    min_val = min(numbers)
    
    # Create the list of counts that we'll use, at the exact length needed
    counts = [0] * (max_val - min_val + 1)

    # Increment each number's count
    for number in numbers:
        counts[number - min_val] += 1
        
    # Append the numbers in sorted order to the output list
    output = []
    for i, count in enumerate(counts):
        if count != 0:
            # numbers[count] = counts[count] + min_val
            output.extend([min_val + i] * count)
            
    numbers[:] = output


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: Average time is O(n + k) where n is the items and k is number of buckets
    Memory usage: O(n * k) because we have to allocate a full list for every bucket"""
    
    # Edge case: len of numbers if 1
    if len(numbers) <= 1:
        return
    
    # Set the max and min values
    max_val, min_val = min(numbers), min(numbers)
    
    # Base Case: All the numbers are the same
    if max_val == min_val:
        return
    
    # Create a list with placeholders for the length of numbers
    buckets = [0] * num_buckets
    for num in numbers:
        if buckets[(num * max_val) % num_buckets] == 0:
            bucket = deque()
            bucket.append(num)
            # print(bucket)
            buckets[(num * max_val) % num_buckets] = bucket
        
            

if __name__ == "__main__":
    nums = [2, 6, 19, 2, 20, 20, 5, 11, 1, 16]
    print(counting_sort(nums))
    print(nums)