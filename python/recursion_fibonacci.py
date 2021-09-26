class Solution(object):
    def fib(self, n):
        cache = {}
        def recursion_fib(n):
            if n in cache:
                result = cache[n]
            if n < 2:
                result = n
            #relation recurrence
            else:
                result = recursion_fib(n-1) + recursion_fib(n-2)
            #put the result in cache for later reference
            cache[n] = result
            return result
        return recursion_fib(n)

solution =Solution()
print (solution.fib(4))
