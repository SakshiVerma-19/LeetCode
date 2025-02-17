class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
    
        def dfs(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    total += 1
                    counter[tile] -= 1
                    total += dfs(counter)
                    counter[tile] += 1
            return total
        
        return dfs(count)
            