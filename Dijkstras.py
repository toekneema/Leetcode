# dijkstra's implementation python
# bestDists gets constantly overwritten/updated
    # need to initialize it with a 0 for the startPt, inf for everything else
# instead of a BFS with q/deque, use a heap for greedily choosing smallest dist to process next
    # and instead of doing layer-by-layer, i can just instantly pop after the while loop line
# so i dont even need a visited set, the optimizations guarantee that i dont repeat in a cycle
    # first optimization is that i will just skip to next iteration if the currDistToThisNode is 
    # worse than the currBestDist for it
    # sec optimization happens inside the for loop, guaranteeting that i dont append anything useless 
    # to the heap, bc i check to make sure the newDist (currDist + weight[node,neigh]) is smaller
    # than the currBest, so this prevents cycles bc if there was a cycle then it would obv have a larger dist

bestDists = {i:float('inf') for i in range(1,n+1)}
bestDists[n] = 0
heap = [(0,start)]
while heap:
    distFromStart, node = heapq.heappop(heap)
    if bestDists[node] < distFromStart:
        continue
                    
    neighbors = adjMap[node]
    for neigh in neighbors:
        newDist = distFromStart + weights[node,neigh]
        if newDist < bestDists[neigh]:
            bestDists[neigh] = newDist
            heapq.heappush(heap, (bestDists[neigh], neigh))