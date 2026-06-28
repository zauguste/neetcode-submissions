class Solution:
    def climbStairs(self, n: int) -> int:
    #     n = 5


    #     n = 0 current step is 0 add 1 left , current step is 0 add 2 right ...since the most steps we can take is 1 or 2
    #        / \
    #       1   2 
    #      /\   / \
    #     2  3 3    4
    #    /\  /\/ \  /\
    #          4  {5} {5} n
    #       4 {5}/\
    #   3 4 /\{5}  n
    #   /\ /\{5} n 
    #   4{5} {5}n
    #   /\
    # [5] n
    # total is 8
        # redundant work
        # []dp
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
