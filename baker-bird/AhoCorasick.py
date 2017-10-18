# Aho-Corasick TRIE class
class TrieNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None

# make TRIE with multiple patterns
def make_trie(patterns):
    root = TrieNode()
 
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, TrieNode())
        node.out.append(path)
    return root

# calculate failure function & add fail info to TRIE
def add_trie_ff(patterns):
    root = make_trie(patterns)
    queue = []
    for node in root.goto.itervalues():
        queue.append(node)
        node.fail = root
 
    while len(queue) > 0:
        rnode = queue.pop(0)
 
        for key, unode in rnode.goto.iteritems():
            queue.append(unode)
            fnode = rnode.fail
            while fnode != None and not fnode.goto.has_key(key):
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out
 
    return root
  
# main procedure for pattern matching in Aho-Corasick algorithm
def find_pattern(s, root, pdict):
    node = root
    r = list()

    for i in xrange(len(s)):
        while node != None and not node.goto.has_key(s[i]):
            node = node.fail
        if node == None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            r.append((i - len(pattern) + 1, pdict[pattern]))

    return r
