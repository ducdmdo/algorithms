class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def recursive_climbStairs(n):
            if n in cache:
                result = cache[n]
            if n <= 3:
                result = n
            else:
                result = recursive_climbStairs(n-1) + recursive_climbStairs(n-2)
            # put the result in cache for later reference
            cache[n] = result
            return result
        return recursive_climbStairs(n)

solution = Solution()
print (solution.climbStairs(38))
