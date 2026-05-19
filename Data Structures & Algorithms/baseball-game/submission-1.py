class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i = 0
        n = len(operations)
        new_list = []
        while i < n:
            if operations[i] == "+":
                new_list.append(int(new_list[-2]) + int(new_list[-1]))
            elif operations[i] == "D":
                new_list.append((int(new_list[-1])) * 2)

            elif operations[i] == "C":
                new_list.pop()    


            else:
                new_list.append(int(operations[i]))    
            
            i += 1

        return sum(new_list)
            