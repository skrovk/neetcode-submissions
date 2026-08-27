class Solution:
    NUM_CHARS = 26

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()

        for item in strs:
            item_dict = self.create_item_arr(item)

            if anagram_groups.get(item_dict) is not None:
                anagram_groups[item_dict].append(item)
                continue
            
            anagram_groups[item_dict] = [item]

        return list(anagram_groups.values())


    def create_item_arr(self, item):
        arr = [0] * self.NUM_CHARS

        for ch in item:
            arr[ord(ch) - ord('a')] += 1

        return tuple(arr)