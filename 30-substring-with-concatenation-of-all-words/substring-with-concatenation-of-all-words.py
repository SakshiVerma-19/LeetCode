from collections import *
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_len=  word_len *len(words)
        word_count =Counter(words)
        result =[]

        for i in range(len(s)-total_len +1):
            seen ={}
            for j in range (0, total_len, word_len):
                word = s[i+j:i+j+word_len]
                if word in word_count:
                    seen[word] = seen.get(word, 0)+1
                    if seen[word]> word_count[word]:
                        break
                else:
                    break
            if seen == word_count:
                result.append(i)
        return result
