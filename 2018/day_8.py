import os
#from numpy import where, zeros
#import re
#from itertools import repeat

workPath = os.path.expanduser("~/Documents/Code/Advent_of_code")
os.chdir(workPath)

with open(os.path.join(workPath, "day_8_input.txt"),  "r") as inFile:
    lines = inFile.readlines()[0]
    data = [int(i) for i in lines.strip().split(' ')]

test = [int(i) for i in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' ')]

num_entries = len(test)
test_dict = {}
node = 0
nodes = []
st = 0
end = 2
num_child, num_meta = test[st:end]
meta_remaining = num_meta
while end < num_entries:
    #print(nodes, meta_remaining, num_entries, test_dict)
    if meta_remaining <= (num_entries - end):
        nodes.append(node)
        print(nodes)
        if num_child == 0:
            st = end
            end += num_meta
            node_to_load = nodes.pop()
            test_dict[node_to_load] = test[st:end]
            meta_remaining -= num_meta
            #print(test_dict, node, nodes, st, end, num_child, num_meta)
        else:
            test_dict[node] = num_meta
        node += 1
        #print(test_dict, node, nodes, st, end, num_child, num_meta)
        st = end
        end += 2
        num_child, num_meta = test[st:end]
        meta_remaining += num_meta
        #print(test_dict, node, nodes, st, end, num_child, num_meta)
    else:
        print(test_dict, node, nodes, st, end, num_child, num_meta)
        #st = end
        node_to_load = nodes.pop()
        num_meta = test_dict[node_to_load]
        end = st + num_meta
        test_dict[node_to_load] = test[st:end]
        meta_remaining -= num_meta




