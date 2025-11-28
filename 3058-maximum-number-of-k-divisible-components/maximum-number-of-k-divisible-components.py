class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node: int, parent: int) -> int:
            subtree_sum = values[node]
            
            # Visit all adjacent nodes except the parent
            for neighbor in adjacency_list[node]:
                if neighbor != parent:
                    # Add the sum of child subtree to current subtree sum
                    subtree_sum += dfs(neighbor, node)
            
            # If subtree sum is divisible by k, we can cut this as a separate component
            if subtree_sum % k == 0:
                nonlocal component_count
                component_count += 1
            
            return subtree_sum
        
        # Build adjacency list representation of the tree
        adjacency_list = [[] for _ in range(n)]
        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)
        
        # Initialize counter for valid components
        component_count = 0
        
        # Start DFS from node 0 with -1 as parent (indicating no parent)
        dfs(0, -1)
        
        return component_count        