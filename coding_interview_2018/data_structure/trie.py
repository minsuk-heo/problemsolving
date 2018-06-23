"""
store word in dictionary
search word in dictionary return True if exist
"""

class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # item denotes the Trie has this word as item
        # if item key doesn't exist Trie doesn't have this word but as path to longer word
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hel"))
print(dictionary.search("hey"))