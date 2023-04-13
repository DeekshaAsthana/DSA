def nextLargerElementToLeft(arr,n):
        st=[-1]
        ans=[]
        for i in range(n):
            if(st[-1]==-1 or st[-1]>arr[i]):
                ans.append(st[-1])
                st.append(arr[i])
            else:
                while(st[-1]!=-1 and st[-1]<=arr[i]):
                    st.pop()
                ans.append(st[-1])
                st.append(arr[i])
        return ans
