class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None
 
def aho_create_forest(patterns):
    root = AhoNode()
 
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root
 
 
def aho_create_statemachine(patterns):
    root = aho_create_forest(patterns)
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
 
 
def aho_find_all(s, root, callback, pdict):
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
            #callback(i - len(pattern) + 1, pattern, pdict[pattern])
            r.append((i - len(pattern) + 1, pdict[pattern]))

    return r

############################
# Demonstration of work
def on_occurence(pos, patterns, pnum):
  print "At pos %s found pattern: %s:%s" % (pos, patterns, pnum)

# patterns = ['aabba', 'aaabb', 'ababa']
# s = "aabbaaabba"
# root = aho_create_statemachine(patterns)
# aho_find_all(s, root, on_occurence)
