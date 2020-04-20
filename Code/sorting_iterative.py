#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n)
    Memory usage: O(1) because we don't allocate any new memory"""
    # Psuedo Code
    # Loop from the beginning of given n, and check to see if n value > n + 1 value
    # If n value > n + 1, return False
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Worst Case: O(n^2), the number of position switches is (n^2 - n)/2 which rounds to n^2
    Best Case: O(n), 
    Memory usage: O(1) as we don't store anything"""
    last_item = len(items) - 1
    iterations = 1
    
    for j in range(len(items)):
        # Go through each item, keeping track of where we are so we don't have to check previous numbers, and swap them if needed
        for i in range(last_item - j):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                iterations = 1
            else:
                iterations += 1
        # Break if we get to the end
        if iterations >= (last_item - j):
            break
    
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: Best and worst case: O(n^2) because we have to compare twice per placement, but it's twice as fast. 
    TODO: Memory usage: O(n) - Don't need to store anything"""
    for i in range(len(items) - 1):
        smallest = i
        for j in range(i, len(items)):
            if items[j] < items[smallest]:
                smallest = j
                
        items[i], items[smallest] = items[smallest], items[i]
    
    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2)  It uses nested loops, so we go through every item for every item
    Memory usage: O(1) Making copies of the data is not required, so the memory is already allocated"""
    for i in range(1, len(items)):
        inserting = items[i]
        j = i - 1
        
        while j >= 0 and inserting < items[j]:
            # Since the item we're looking at is greater, set it as our current
            items[j+1] = items[j]
            j -= 1
        
        # Swap it with the one above
        items[j+1] = inserting
    
    return items