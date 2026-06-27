class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if not set(s)==set(t):
            return False

        tree_s, tree_t = {}, {}
        for letter_s in s:
            if letter_s not in tree_s:
                tree_s[letter_s] = 1
            else:
                tree_s[letter_s] +=1
        
        for letter_t in t:
            if letter_t not in tree_t:
                tree_t[letter_t] = 1
            else:
                tree_t[letter_t] += 1

        for key_s in tree_s:
            if not (tree_s[key_s]==tree_t[key_s]):
                return False
        
        return True