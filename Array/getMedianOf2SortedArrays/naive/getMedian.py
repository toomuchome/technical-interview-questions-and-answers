def getMedian(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return False

    merged = arr1 + arr2 # Space complexity: O(m + n), m is the size of arr1 and n is the size of arr2
    sortedMerged = sorted(merged) # Time complexity: O(klogk) where k is the sum of m + n, python uses timsort, worst case: o(n)

    if len(sortedMerged) % 2 == 0:
        index = len(sortedMerged) / 2
        return (sortedMerged[index] + sortedMerged[index - 1]) / float(2)
    else:
        index = (len(sortedMerged) - 1) / 2
        return sortedMerged[index]

arr1 = []
arr2 = [1,2,3]
arr3 = [1,2,3,4]
arr4 = [1,5,7,8]
arr5 = [2,9,10,11]

testCase1 = getMedian(arr1, arr2)
testCase2 = getMedian(arr1, arr3)
testCase3 = getMedian(arr2, arr3)
testCase4 = getMedian(arr4, arr5)

print 'Test cases:'
print '1.', arr2, 'Expected: 2, Result:', testCase1, '>>> TEST', 'PASSED' if testCase1 == 2 else 'FAILED'
print '2.', arr3, 'Expected: 2.5, Result:', testCase2, '>>> TEST', 'PASSED' if testCase2 == 2.5 else 'FAILED'
print '3.', sorted(arr2 + arr3), 'Expected: 2, Result:', testCase3, '>>> TEST', 'PASSED' if testCase3 == 2 else 'FAILED'
print '3.', sorted(arr4 + arr5), 'Expected: 7.5, Result:', testCase4, '>>> TEST', 'PASSED' if testCase4 == 7.5 else 'FAILED'
