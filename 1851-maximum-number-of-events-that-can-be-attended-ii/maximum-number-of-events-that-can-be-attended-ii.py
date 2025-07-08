class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        def next_event(current_end, start):
            left, right = start,len(events)
            while left<right:
                mid= (left+right)//2
                if events[mid][0] >current_end:
                    right = mid
                else:
                    left = mid+1
            return left
        @lru_cache(None)
        def dfs(index, remaining):
            if index == len(events) or remaining == 0:
                return 0
            skip = dfs(index +1, remaining)

            next_index = next_event(events[index][1], index+1)
            take = events[index][2] + dfs(next_index, remaining -1)

            return max(skip, take)
            
        return dfs(0, k)