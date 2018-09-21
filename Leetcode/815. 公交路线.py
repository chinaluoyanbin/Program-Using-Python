class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        from collections import defaultdict

        self.routes = routes
        self.start = S
        self.end = T

        self.stationInfo = {}
        for idx, route in enumerate(self.routes):
            for stn in route:
                if stn not in self.stationInfo:
                    self.stationInfo[stn] = [idx]
                else:
                    self.stationInfo[stn].append(idx)

        def bfs(idx, route):
            pass

        for route in self.stationInfo[self.start]:
            if not route:
                return -1
            return 1 + bfs(route.index(self.start), )

ins = Solution()
ins.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)
print(1)
            
