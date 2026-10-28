class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create hashmap and store with key and value as freq and number
        mp = {}
        for val in nums:
            mp[val] = mp.get(val, 0) + 1

        #make a min-heap and then for the stuff in the mini heap
        pq = []
        for key, freq in mp.items():
            heapq.heappush(pq, [freq, key]) #push into the min-heap

            # pop out of the heap if the leng of the heap is k or greater
            if len(pq) > k:
                heapq.heappop(pq)

        res = []
        temp = [0] * len(pq)
        index = len(pq) - 1
        while pq:
            temp[index] = heapq.heappop(pq)[1]
            index -= 1
        for val in temp:
            res.append(val)

        return res