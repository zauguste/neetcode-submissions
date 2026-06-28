class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # loop through list
        # sort and compare
        # if in list access key and add
        # if not in list create new group
        groups = defaultdict(list)
        for eachword in strs:
            groupWord = ''.join(sorted(eachword))
            groups[groupWord].append(eachword)
        return list(groups.values())