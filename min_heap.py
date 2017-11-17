
#heap sort

import heapq

i =[ 4,67,2,0,98]

heapq.heapify(i)

print "min heap :", i

heapq.heappush(i,0.2)

print "after pushing 0.2 :", i

# pops out the root or the smallest element
heapq.heappop(i)


print "after poping out root or min :" ,i
