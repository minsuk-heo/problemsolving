class find_subsets_from_set:

    def sub_sets(self, set):
        # start by adding an empty set to all possible subsets
        return self.findSubset([], set)

    def findSubset(self, prev, subset):
        if subset:
            cur = subset[0]
            # findSubset(prev, next items) + findSubset(prev + current, next items)
            return self.findSubset(prev, subset[1:]) + self.findSubset(prev + [cur], subset[1:])
        return [prev]


print(find_subsets_from_set().sub_sets([2,1,3]))