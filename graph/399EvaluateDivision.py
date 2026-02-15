from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(list)
        for i in range(len(equations)):
            k = equations[i][0]
            u = equations[i][1]
            val = values[i]
            dic[k].append((u,val))
            dic[u].append((k,1/val))  
        def dfs(st,en,val,vis):
            
        
            for i,v in dic[st]:
                if st == en :
                    return val
                if i not in vis:
                    vis.add(i)
                    
                    k = dfs(i,en,val*v,vis)
                    if k != -1:
                        return k
            return -1         
        ans = []
        for st,en in queries:
            vis = set()
            vis.add(st)
            val = dfs(st,en,1.0,vis)
            ans.append(val)
        return ans


if __name__ == "__main__":
    equations = [["x1","x2"]]
    values = [3.0]
    queries = [["x9","x2"],["x9","x9"]]

    sol = Solution()
    result = sol.calcEquation(equations, values, queries)
    print("Result:", result)