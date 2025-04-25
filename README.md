# CSCI 3412 Homework 5

## Question 1
###
a.  
Topological Sorting algorithm would be the best algorithm to patch the servers. We can use this algorithm because the graph is both connect and acyclic (the graph must be acyclic because a deadlock could arise if there were a cycle within the servers). This algorithm works for the patching task because for any directed edge uv, vertex u must come before vertex v. So in terms of servers, we must patch server u before server v is patched. We also know that this algorithm will give us a safe sequence because for any directed acyclic graph, there must be at least one topological ordering.

b.  
Below is the pseudo-code for a simple topological sort
   
define topologicalSort(graph):

    list safeSequence  
    for node in graph:  
        if node has successor is false:  
            append node to beginning of safeSequence  
    
    return safeSequence  

The logic in the function is that we find a node that has no successor. Any node without a successor has no other depending on it, so it was safe to remove. This node is then appended to the beginning of the list. We do this for every node until there are no more nodes in the graph.

c.  
A potential pitfall of the topological sort is if there is a cycle in the graph. If a cycle exist then there are no servers that do not send data to another server. In this case, it would be impossible to develop a safe sequence.

d.

Adjust the algorithm to use $DFS$ instead of the simple topological sort. By using $DFS$, we can check if there is a cycle in the graph, and stop the patching if found. Pick a starting node to run the DFS. Every time visit a node, we mark it as visited. When a node is encountered that only leads to visit nodes, we back track to the previous node and run the $DFS$ again. When we find a node that does lead to another node, back track and run $DFS$. A possible challenge of this algorithm is if we cannot find a node that has no successor. In this case, it would be impossible to determine a safe sequence, and the algorithm would be stuck in an infinite loop, so we would need to halt patching.

**Pseudo-code**

define DFS(graph):

    **initialize lists**

    list safeSequence
    list visited

    **algorithm**

    pick root node for DFS (graph[0])
    traverse path from root node
    if nextNode in visited:
        backtrack
    if currentNode has no nextNode:
        safeSequence.append(currentNode)
    
    return safeSequence


e.  
In the case that we want to only patch servers that a have a load below a certain threshold, we modify the $DFS$ algorithm to check the current load before adding it to the safe sequence. The challenge of adding this condition is that if there are no servers under the threshold, we would have another case where an infinite loop could occur until the server loads decrease.

define DFS_modified(graph, threshold):

    **initialize lists**

    list safeSequence
    list visited

    **algorithm**

    pick root node for DFS (graph[0])
    traverse path from root node
    if nextNode in visited:
        backtrack
    if currentNode has no nextNode:
        if currentNode <= threshold:
            safeSequence.append(currentNode)
        else:
            backtrack
    
    return safeSequence


## Question 2
###
Submited as question2.pdf

## Question 3
###
The below command runs the spell check with arguments numberOfSuggestions = 7, maxEditDistance = 7, minWordLength = 4  
**python question3.py 7 7 4**

Output:  
```
Suggestions for 'homan': {'woman': (1, 323), 'human': (1, 170), 'coman': (1, 17), 'roman': (1, 8), 'women': (2, 385), 'home': (2, 294), 'domain': (2, 62)}
Suggestions for 'spote': {'spoke': (1, 218), 'spite': (1, 117), 'spot': (1, 76), 'spots': (1, 12), 'smote': (1, 4), 'spore': (1, 3), 'some': (2, 1536)}
Suggestions for 'belst': {'best': (1, 268), 'beast': (1, 26), 'belt': (1, 11), 'felt': (2, 697), 'west': (2, 280), 'rest': (2, 206), 'else': (2, 201)}
Suggestions for 'effrts': {'efforts': (1, 103), 'effort': (2, 130), 'effects': (2, 82), 'forts': (2, 8), 'exerts': (2, 3), 'effete': (2, 1), 'parts': (3, 295)}
Suggestions for 'speling': {'spelling': (1, 4), 'feeling': (2, 362), 'seeing': (2, 207), 'speaking': (2, 185), 'swelling': (2, 164), 'smiling': (2, 161), 'opening': (2, 146)}
Suggestions for 'perrfect': {'perfect': (1, 39), 'prefect': (2, 2), 'project': (3, 288), 'effect': (3, 187), 'perfectly': (3, 45), 'protect': (3, 41), 'correct': (3, 38)}
Suggestions for 'avorage': {'average': (1, 18), 'voyage': (2, 12), 'forage': (2, 7), 'storage': (2, 3), 'averages': (2, 1), 'averaged': (2, 1), 'george': (3, 150)}
Suggestions for 'typo': {'type': (1, 84), 'types': (2, 33), 'tips': (2, 16), 'teno': (2, 10), 'tops': (2, 3), 'type_': (2, 3), 'tape': (2, 2)}
Suggestions for 'misspeling': {'missing': (3, 28), 'misspelled': (3, 1), 'listening': (4, 89), 'kissing': (4, 38), 'whispering': (4, 19), 'disputing': (4, 12), 'mingling': (4, 11)}
Suggestions for 'mlch': {'much': (1, 671), 'such': (2, 1436), 'each': (2, 411), 'march': (2, 134), 'rich': (2, 92), 'match': (2, 41), 'mack': (2, 22)}
Suggestions for 'mistkes': {'mistakes': (1, 15), 'mistaken': (2, 59), 'mistake': (2, 39), 'mistress': (2, 24), 'mister': (2, 2), 'misses': (2, 2), 'mists': (2, 1)}
Suggestions for 'hauunt': {'haunt': (1, 2), 'aunt': (2, 52), 'hunt': (2, 31), 'gaunt': (2, 5), 'taunt': (2, 1), 'hand': (3, 834), 'count': (3, 748)}
Suggestions for 'odoor': {'door': (1, 498), 'odour': (1, 19), 'odor': (1, 6), 'poor': (2, 128), 'floor': (2, 105), 'doors': (2, 47), 'doom': (2, 6)}
Suggestions for 'colone': {'colonel': (1, 143), 'colony': (1, 57), 'colon': (1, 9), 'cologne': (1, 3), 'alone': (2, 337), 'close': (2, 219), 'colonies': (2, 202)}
```