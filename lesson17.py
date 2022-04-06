# with open("text.txt", "w", encoding="UTF-8") as file:
#     password = input("Enter password --->  ")
#     file.write(password)
# f = open("text.txt", "rt")
# print(f.read())

# f.close()

# N1
# with open("text.txt", "a", encoding="UTF-8") as file:
#     login = input("Enter login ---> ")
#     file.write(login)
# f = open("text.txt", "rt")
# print(f.read())

# # f = open("text.txt", "r")
# # print(f.readline())

# f.close()


# N2
# with open("text.txt", "rt", encoding="UTF-8") as file:
#     file.read()

# f = open("text.txt", "rt")
# res = f.read()
# res = res.split("\n")
# for i in range(0, len(res) - 1):
#     if i < 3:
#         print(res[i])

# f.close()



# 4
# with open("text.txt", "rt", encoding="UTF-8") as file:
#     file.read()
# f = open("text.txt", "rt")
# res = f.read()
# res = res.split("\n")
# res.sort(key=len)
# print(res[-1])
# f.close()


# N5
# with open("text.txt", "rt", encoding="UTF-8") as file:
#     file.read()
# f = open("text.txt", "rt")
# res = f.read()
# for i in res:
#     if i.isdigit():
#         print(i)
# f.close()


# N6
# with open("password.txt", "w", encoding="UTF-8") as file:
#     file.write("login - Name1, password - 1234")
#     file.write("\nlogin - Name2, password - 2345")
#     file.write("\nlogin - Name3, password - 3456")
#     file.write("\nlogin - Name4, password - 4567")
#     file.write("\nlogin - Name5, password - 5678")

# f = open("password.txt", "rt")
# res = f.read()
# res = res.split("\n")
# userLogin = input("Enter login ---- ").title()
# userPassword = input("Enter password ---- ")

# for i in res:
#     if "login - " + userLogin + ", password - " + userPassword == i:
#         print(True)
#         break
# else:
#     print(False)

# f.close()
# file.close()
