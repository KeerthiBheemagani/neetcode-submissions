class Solution:
    def isValid(self, s: str) -> bool:
        matching = { ')':'(', '}' :'{', ']':'['}
        val_arr = []
        for c in s:
            if c not in matching:
                val_arr.append(c)
            else:
                if not val_arr or val_arr[-1]!= matching[c]:
                    return False
                val_arr.pop()
        return not val_arr

        