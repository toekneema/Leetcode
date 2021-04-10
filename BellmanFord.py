edges = []
dic = defaultdict(int)
allCurrs = set()
for s,t,r in zip(sources,targets,rates):
    dic[s,t] = r
    edges.append([s,t,r])
    allCurrs.add(s)
    allCurrs.add(t)

bestAmts = {curr : float('-inf') for curr in allCurrs}
bestAmts[source] = 1
        
for i in range(len(allCurrs)-1):
    for s,t,r in edges: # source/target
	newAmt = bestAmts[s] * r
        if newAmt > bestAmts[t]:
            bestAmts[t] = newAmt

for s,t,r in edges:
    newAmt = bestAmts[s] * r
    if newAmt > bestAmts[t]:
	return -1
