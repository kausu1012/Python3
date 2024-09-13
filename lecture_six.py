################recurrsion 

# num = int(input("enter a num: "))

# def od_ev(num):
#     if (num%2==0):
#         print("string even")
#     else:
#         print("string odd")

# od_ev(num)


# # n = int(input("enter the value of n: "))
# # def show(n):
# #     if(n==0):
# #         return
# #     print(n)
# #     show(n-1)
    
# # show(n)




# n = int(input("enter the value of n: "))
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return (fact(n-1)*n)

    
# print(fact(n))


# ###### Calcualte the sum of n natural numbers:


# n = int(input("enter the value of n: "))
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n

# sum = calc_sum(n)
# print(sum)


# ########### Recurssion to print all the elment from list.

def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx], idx)
    print_list(list,idx+1) 


fruits = ["Mango","Banana","Lichi","Watermelon"]   
print_list(fruits)
print()




