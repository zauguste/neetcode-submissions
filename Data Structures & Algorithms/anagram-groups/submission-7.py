class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # edge cases
        # user inputs a "" empty string
            # reutrn [[""]]

        # lets go through the list and collect all the matching anagrams
        # return as a list of sub lists



        # go through the list 
            # create a key for each word
        # add to sublist all the corresponding words that match the key

        # we can accomplish this by creating a key for a word
        # the position on the alphabet will dictate the position of a 1 or 0
        
        # go through the list again
        # if the letters match add to the list for that key
    
        mapp = defaultdict(list)
        # o(n)
        for eachword in strs:
            # o(26) = o(1)
            new_list = [0] * 26
            for eachltr in eachword:
                new_list[ord(eachltr) - ord("a")] += 1
            mapp[tuple(new_list)].append(eachword)

        return list(mapp.values())





