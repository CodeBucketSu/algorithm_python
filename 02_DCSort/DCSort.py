'''This program implement the divide and conquer sort algorithm.'''

import sys

def DCSort(arrayToSort):
	'''Divede and Conquer Sort.'''
	length = len(arrayToSort)
	#devide
	if length == 1:
		return arrayToSort
	else:
		arrLeft = arrayToSort[0:(length+1)/2]
		arrRight = arrayToSort[(length+1)/2:]  

	#conquer
	arrLeft = DCSort(arrLeft)
	arrRight = DCSort(arrRight)

	#combine
	idxL = 0
	idxR = 0
	arrSorted = []
	for i in range(length):
		if arrLeft[idxL] < arrRight[idxR]:
			arrSorted.append(arrLeft[idxL])
			idxL += 1
		else:
			arrSorted.append(arrRight[idxR])
			idxR += 1
		if idxL >= len(arrLeft):
			arrSorted.extend(arrRight[idxR:])
			break
		elif idxR >= len(arrRight):
			arrSorted.extend(arrLeft[idxL:])
			break

	return arrSorted

def main():
	arr = [1,2,65,23,76,8,43,4,8,23,78,9,34]
	arrSorted = DCSort(arr)
	print arrSorted

if __name__ == '__main__':
	main()