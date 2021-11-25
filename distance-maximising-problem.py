# Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
# Distance maximising problem
array = [ 34, 8, 10, 3, 2, 80, 30, 33, 1 ]
max_diff = 0
ans = []
for i in range ( 0 , len ( array ) ) :
    for j in range ( i + 1 , len ( array ) ) :
        if array [ j ] > array [ i ] :
            if j - i > max_diff :
                max_diff = j - i
                ans = []
                ans.append ( i )
                ans.append ( j )
print ( max_diff , ans )