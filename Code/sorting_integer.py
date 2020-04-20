#!python


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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    num_range = max(numbers) - min(numbers)
    

if __name__ == "__main__":
    nums = [2, 6, 19, 2, 20, 20, 5, 11, 1, 16]
    print(counting_sort(nums))
    print(nums)