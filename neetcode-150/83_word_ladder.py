# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#
# Constraints:
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

class Solution:
    min_length = float("inf")
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        wordList.insert(0, beginWord) #insert begin word at 0th position
        graph = {}
        for word in wordList:
            graph[word] = []
            for pos in range(len(word)):
                pre = word[0:pos]
                post = word[pos+1:len(word)]
                for ascii_val in range(ord('a'), ord('z') + 1):
                    new_str = pre + chr(ascii_val) + post
                    if new_str != word and new_str in wordList:
                        graph[word].append(new_str)

        return self.dfs(beginWord, endWord, graph)

    def dfs(self, curr_word, end_word, graph):
        queue = []
        visited = set()
        queue.append(curr_word)
        visited.add(curr_word)
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                popped_node = queue.pop(0)
                if popped_node == end_word:
                    return length
                for neighbour in graph[popped_node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
        return 0