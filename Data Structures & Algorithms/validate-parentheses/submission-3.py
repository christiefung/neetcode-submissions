class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        new_list = []
        n = len(s)

        mapping = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in "[({":
                new_list.append(i)
            
            else:
                if len(new_list) == 0:
                    return False
                top = new_list.pop()

                if top != mapping[i]:
                    return False

                
        return len(new_list) == 0

  #      while i < n:

  #          if s[i] in "[({":
  #              new_list.append(s[i])

  #          else:
  #              if len(new_list) == 0:
  #                  return False
  #              top = new_list.pop()

   #             if s[i] == "]" and top != "[":
   #                 return False

    #            elif s[i] == ")" and top != "(":
    #                return False
          
           
    #            elif s[i] == "}" and top != "{":

     #               return False

            
            
     #       i+=1    

      #  return len(new_list) == 0

#        if len(new_list) == 0:
#            return True
#        else:
#            return False
            
        