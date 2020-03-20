#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 在滑动窗口类型的问题中都会有两个指针。
        # 一个用于延伸现有窗口的 right指针，
        # 和一个用于收缩窗口的left 指针。
        # 在任意时刻，只有一个指针运动，而另一个保持静止。
            
        # 1. 初始，left指针和right指针都指向S的第一个元素.
        # 2. 将 right 指针右移，扩张窗口，直到得到一个可行窗口，亦即包含T的全部字母的窗口。
        # 3. 得到可行的窗口后，将leftt指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。
        # 4. 若窗口不再可行，则跳转至 2。
        
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and co***act the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done co***acting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# @lc code=end

