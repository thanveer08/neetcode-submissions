class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}  #empty dictionary
        for i in range(len(strs)):
            sorted_value = "".join(sorted(strs[i]))
            if sorted_value in mydict:
                 mydict[sorted_value].append(strs[i])  
            else:
                mydict[sorted_value]= [strs[i]]   
        return list(mydict.values())            