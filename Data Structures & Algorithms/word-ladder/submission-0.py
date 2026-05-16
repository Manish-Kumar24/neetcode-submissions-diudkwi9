class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            wordArr = list(word)
            for i in range(len(wordArr)):
                original = wordArr[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    wordArr[i] = ch
                    newWord = "".join(wordArr)
                    if newWord in wordSet:
                        q.append((newWord, steps + 1))
                        wordSet.remove(newWord)
                wordArr[i] = original
        return 0