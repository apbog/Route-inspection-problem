from munkres import Munkres, print_matrix

matrix = [[100000, 1, 1, 1], [1, 100000, 2, 2], [1, 2, 100000, 2], [1, 2, 2, 100000]]
m = Munkres()
indexes = m.compute(matrix)
print_matrix(matrix, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print '(%d, %d) -> %d' % (row, column, value)
print 'total cost: %d' % (total/2)
print indexes
