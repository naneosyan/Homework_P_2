# # 1. x can be either 1(heads) or 0(tails)
# n=int(input('n='))
# count = 0
# for i in range(n):
#     x=int(input('x='))
#     if x == 1:
#         count += 1    
# print(count if count<n/2 else n-count)

# # 2 The sum of two numbers (x and y) is s; the product of the same two numbers (x and y) is p. Find x and y.
# s=int(input())
# p=int(input())
# for x in range (s):
#     for y in range (p):
#         if s==x+y and p==x*y:
#             print (x,y)


# # 3
# n=int(input('n='))
# i=0
# res=2**i
# for i in range(n):
#     res*=2
#     print(res)
