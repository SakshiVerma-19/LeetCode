from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)
        sorted_words=sorted(freq.keys(), key =lambda word: (-freq[word], word))
        return sorted_words[:k]