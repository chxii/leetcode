#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dictionary = set([s for s in [for _ for w in wordList]])
        print(dictionary)
        # q = [(beginWord, 0)]
        # while q:
        #     word, c = q.pop(0)


# @lc code=end

