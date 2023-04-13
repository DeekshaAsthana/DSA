class Solution:
    def isValid(self, s: str) -> bool:
        st=[] 
        bkt={")":"(","}":"{","]":"["}
        for i in s:
            if i in bkt.values():
                st.append(i)
            elif st and bkt[i]==st[-1]:
                st.pop()
            else:
                return False
        return st==[]