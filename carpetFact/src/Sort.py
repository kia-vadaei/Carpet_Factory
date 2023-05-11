
from MyMap import MyMap

class QuickSort :

    @staticmethod
    # Function to find the partition position
    def partition(map =list , low = int, high = int):

        # choose the rightmost element as pivot
        if isinstance(map[high] ,MyMap) :
            pivot = MyMap(map[high]).value


        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if MyMap(map[j]).value <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (map[i], map[j]) = (map[j], map[i])

        # Swap the pivot element with the greater element specified by i
        (map[i + 1], map[high]) = (map[high], map[i + 1])

        # Return the position from where partition is done
        return i + 1

    # function to perform quicksort
    @staticmethod
    def quickSort(map, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = QuickSort.partition(map, low, high)

            # Recursive call on the left of pivot
            QuickSort.quickSort(map, low, pi - 1)

            # Recursive call on the right of pivot
            QuickSort.quickSort(map, pi + 1, high)

