class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through list
        # create an order map
        # add words associated with the order

        hmap = defaultdict(list)
        for words in strs:
            reference = [0] * 26
            for each_letter in words:
                reference[ord(each_letter) - ord('a')] += 1
            hmap[tuple(reference)].append(words)

        return list(hmap.values())

