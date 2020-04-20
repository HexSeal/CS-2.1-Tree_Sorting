#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(m + n) because we add whichever array is smaller and then the difference, and then mutate the original array
    Memory usage: O(m + n), the lengths of items1 and items2"""
    # Final list
    merged = []
    
    # Different variables for different arrays
    x, y = 0, 0
    
    # Loop until one array ends
    while x < len(items1) and y < len(items2):
        if items1[x] <= items2[y]:
            # Add an item from array one and go next
            merged.append(items1[x])
            x += 1
        else:
            # Otherwise append the item to the second array and go next
            merged.append(items2[x])
            y += 1
    
    # Clever way @github.com/tempor1s came up with to add the last items of the bigger array. Could also use if statements because one will always be empty
    merged.extend(items1[x:])
    merged.extend(items2[y:])

    # return the merged array :)
    return merged

def half(items):
    """Divide a list into two ~equal halves"""
    split = len(items) // 2
    return items[:half], items[half:]
            
            
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n + n log n) Merging is O(n), and sorting both sides takes O(n * log n)?
    Memory usage: O(n^2 because merging creates a temporary variable to contain the merge before it's put into items"""
    l1, l2 = half(items)
    
    # Sort the halves
    l1.sort()
    l2.sort()
    
    # Mutate items with the merge list
    items[:] = merge(l1, l2)

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n logn) Merge which is O(n) plus splitting which is O(log n)?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if items > 1:
        l1, l2 = half(items)
    
        merge_sort(l1)
        merge_sort(l2)
        
        items[:] = merge(l1, l2)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (The first item) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time:
        - Best case: O(n) if the pivot is always the next starting index
        - Average: O(n * log n) if the pivot is sometimes the next starting index
        - Worst: O(n^2) if we pick the highest/lowest possible pivot
    Memory usage: O(1) items is mutated and no new memory need allocated"""
    # Get the index of the pivot, the first item and reassign the low as the index after
    # Originally had the pivot at the middle index but it wasn't efficient
    pivot = low
    
    for i in range(low, high):
        # Move items less than the pivot behind it, then start again with the pivot at the next first index
        if items[i] <= items[pivot]:
            items[pivot], items[i] = items[i], items[pivot]
            i += 1
            
    # Return 'p'
    return pivot
        

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n) Always pivot on the optimal item
    Worst case running time: O(n^2)
    Memory usage: O(log n) The call stack takes memory, but we don't actually allocate new memory"""
    # Make sure high is set
    if high is None:
        high = len(items)
    
    # Make sure low is set
    if low is None:
        low = 0
        
    if low < high:
        recur = partition(items, low, high)
        
        # Recurssively loop 
        quick_sort(items, low, recur-1)
        quick_sort(items, recur+1, high)
    
    return items
