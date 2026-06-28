class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we have a group of anagrams a string that contains the same 
        # characters as the other, 
        # but the characters can be different

        # so we need to need track of the
        # amount of characters for each word
        # so, go through each element and append it to the list
        # if it matches the key for that word
        from collections import defaultdict
        list_dict = defaultdict(list)
        # go through the list and 
        #   take the order of each word
        #   append the order of the word that matches same ones in 
        #   the list. How do we match keys?
        #   list_dict[ord(strs)] == ord(eachword):
        #       list_dict[ord(strs)].append(ord(eachword))
        #   else:
        #       create the word in the dictionary and add to it
            
        for each_word in strs:
            if tuple(sorted(each_word)) in list_dict:
                # do something
                list_dict[tuple(sorted(each_word))].append(each_word)
            else:
                list_dict[tuple(sorted(each_word))].append(each_word)
        return list(list_dict.values())
