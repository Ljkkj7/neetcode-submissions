class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for i in operations:
            if i.isnumeric() or i.startswith('-'):
                score_stack.append(int(i))
            elif i == '+':
                sum_score = score_stack[len(score_stack)-1] + score_stack[len(score_stack)-2]
                score_stack.append(sum_score)
            elif i == 'C':
                score_stack.pop()
            else:
                sum_score = score_stack[len(score_stack)-1]*2
                score_stack.append(sum_score)
        
        return sum(score_stack)
