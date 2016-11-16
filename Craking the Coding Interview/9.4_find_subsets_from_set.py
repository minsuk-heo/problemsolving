class find_subsets_from_set:

    def sub_sets(self, set):
        # start by adding an empty set to all possible subsets
        return self.findSubset([], set)

    def findSubset(self, current, subset):
        if subset:
            # current + (current + next item)
            return self.findSubset(current, subset[1:]) + self.findSubset(current + [subset[0]], subset[1:])
        return [current]


print(find_subsets_from_set().sub_sets([2,1,3]))