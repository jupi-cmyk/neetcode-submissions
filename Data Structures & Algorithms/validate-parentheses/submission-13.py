class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = ['(', '[', '{']
        sequence_open_parentheses = []
        if s[0] not in open_parentheses:
            return False
        for i in range(len(s)):
            if s[i] in open_parentheses:
                sequence_open_parentheses.append(s[i])
                continue
            if len(sequence_open_parentheses) == 0:
                return False
            last_open = sequence_open_parentheses.pop()
            if (last_open == '(' and s[i] == ')') or (last_open == '[' and s[i] == ']') or (last_open == '{' and s[i] == '}'):
                continue
            return False

        return len(sequence_open_parentheses) == 0
        