# # 1. x can be either 1(heads) or 0(tails)
# n=int(input('n='))
# count = 0
# for i in range(n):
#     x=int(input('x='))
#     if x == 1:
#         count += 1    
# print(count if count<n/2 else n-count)

# # 2
# x=int(input())
# y=int(input())
# for i in range (x):
#     for j in range (y):
#         if x==i+j and y==i*j:
#             print (i,j)


# # 3
# n=int(input('n='))
# i=0
# res=2**i
# for i in range(n):
#     res*=2
#     print(res)
