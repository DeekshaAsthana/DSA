def leftSmaller(self, n, a):
        st=[]
        ans=[]
        for i in range(len(a)):
            if(len(st)==0):
                ans.append(-1)
                st.append(a[i])
            elif(a[i]>st[-1]):
                ans.append(st[-1])
                st.append(a[i])
            else:
                while(len(st)!=0 and a[i]<=st[-1]):
                    st.pop()
                if len(st)>0:
                    ans.append(st[-1])
                    st.append(a[i])
                else:
                    ans.append(-1)
                    st.append(a[i])
        return ans