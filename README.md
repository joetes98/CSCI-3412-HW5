# CSCI 3412 Homework 5

## Question 1
###
a.  
Topological Sorting algorithm would be the best algorithm to patch the servers. We can use this algorithm because the graph is both connect and acyclic (the graph must be acyclic because a deadlock could arise if there were a cycle within the servers). This algorithm works for the patching task becuase for any directed edge uv, vertex u must come before vertex v. So in terms of servers, we must patch server u before server v is patched. We also know that this algorithm will give us a safe sequence because for any directed acyclic graph, there must be at least one topological ordering. The topological sort will loop through every vertex v and compute the finishing time v (the number of nodes found before during the expansion of v).

b.  
Below is the pseudo-code for a simple topological sort  

1. Call $DFS(G)$ to compute finishing times $v.f$ for each vertex $v$
2. As each vertex is finished, insert it onto the front of a linked list
3. $return$ the linked list of vertices

c.  
A potential pitfall of the topological sort is if there is a cycle in the graph. If a cycle exist then there are no servers that do not send data to another server. In this case, it would be impossible to develop a safe sequence.

d.  
