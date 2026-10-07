class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        new_arr = []
        for x in operations:
            if x == '+':
                new_arr.append(new_arr[-1]+new_arr[-2])
            elif x == 'D':
                new_arr.append(2*new_arr[-1])
            elif x == 'C':
                new_arr.pop()
            else:
                new_arr.append(int(x))
        return sum(new_arr)


