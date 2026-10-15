class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = defaultdict(int)
        distinct = deque()
        for i in hand:
            count[i]+=1
        hand.sort()
        for i in hand:
            if i not in distinct:
                distinct.append(i)
        for i in distinct:
            if count[i] == 0:
                continue
            for j in range(1,groupSize):
                count[i+j] -= count[i]
                if count[i+j] < 0:
                    return False
            count[i] = 0
        return True
