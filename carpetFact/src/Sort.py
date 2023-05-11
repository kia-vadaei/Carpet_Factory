

class QuickSort :

    @staticmethod
    # Function to find the partition position
    def partition( array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1

    # function to perform quicksort
    @staticmethod
    def quickSort( array, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = QuickSort.partition(array, low, high)

            # Recursive call on the left of pivot
            QuickSort.quickSort(array, low, pi - 1)

            # Recursive call on the right of pivot
            QuickSort.quickSort(array, pi + 1, high)

