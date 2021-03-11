'''
Question -> https://leetcode.com/contest/weekly-contest-112/problems/bag-of-tokens/
@Author -> Taklemariam Alazar
'''
class Solution:
    def bagOfTokensScore(self, tokens, P):
        score = 0
        tokens.sort()
        while tokens:
            if tokens[0] <= P:
                P -= tokens[0]
                score += 1
                tokens.pop(0)
            else:
                if score and len(tokens)>2:
                    score -= 1
                    P += tokens.pop()
                else:
                    tokens.pop()
        return score