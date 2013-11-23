'''This is a implementation of insertion sort.'''

import sys

def insertionSort(arrToSort):
	'''arrToSort: a list'''
	for i, itemToRank in enumerate(arrToSort[1:]):
		i+=1
		for j, itemBefore in enumerate(arrToSort[i-1::-1]):
			j = i-j-1
			if itemToRank < itemBefore:
				arrToSort[j+1] = itemBefore
				if j == 0:
					arrToSort[0] = itemToRank
			else:
				arrToSort[j+1] = itemToRank
				break


if __name__ == "__main__":
	array = [1, 2, 9, 4, 6, 3, 6, 7, 3, 5, 73]
	insertionSort(array)
	print array
