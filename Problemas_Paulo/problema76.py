class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        map_t = {}
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1

        required = len(map_t) 
        left = 0
        right = 0
        formed = 0 
        window_map = {} 

        min_len = float('inf')
        ans_start_index = -1

        while right < len(s):
            char_right = s[right]
            window_map[char_right] = window_map.get(char_right, 0) + 1

            if char_right in map_t and window_map[char_right] == map_t[char_right]:
                formed += 1

            while left <= right and formed == required:
                char_left = s[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans_start_index = left

                window_map[char_left] -= 1
                if char_left in map_t and window_map[char_left] < map_t[char_left]:
                    formed -= 1

                left += 1

            right += 1

        if ans_start_index == -1:
            return ""
        
        return s[ans_start_index : ans_start_index + min_len]