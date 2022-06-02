# Group Anagrams
class Solution(object):
    def createDict(self, str):
        dict = {}
        for s in str:
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
        return dict
    
    def groupAnagrams(self, strs):
        anagramDict = {}
        for str in strs:
            dict = sorted(self.createDict(str).items())
            dictNew = ",".join([x[0] for x in dict]) + ",".join("%s" %x[1] for x in dict)
            if dictNew not in anagramDict:
                anagramDict[dictNew] = []
            anagramDict[dictNew].append(str)
        
        return anagramDict.values()
ob1=Solution()
print(ob1.createDict(str = ["eat","tea","tan","ate","nat","bat"]))