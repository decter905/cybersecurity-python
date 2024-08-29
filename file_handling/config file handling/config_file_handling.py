
# TASK 1
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
#
# with open(import_file, "r") as file:
#     print(file.read())
# print(remove_list)

# TASK 2
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# with open(import_file, "r") as file:
#     # TASK 3
#     ip_addresses = file.read()
# print(ip_addresses)

# TASK 4
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# with open(import_file, "r") as file:
#     ip_addresses = file.read()
#
# ip_addresses = ip_addresses.split()
# print(ip_addresses)

# TASK 5
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# with open(import_file, "r") as file:
#     ip_addresses = file.read()
#
# ip_addresses = ip_addresses.split()
#
# for element in ip_addresses:
#     print(element)

# TASK 6
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# with open(import_file, "r") as file:
#     ip_addresses = file.read()
#
# ip_addresses = ip_addresses.split()
#
# for element in ip_addresses:
#     if element in remove_list:
#         ip_addresses.remove(element)
#
# print(ip_addresses)

# TASK 7
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# with open(import_file, "r") as file:
#     ip_addresses = file.read()
#
# ip_addresses = ip_addresses.split()
#
# for element in ip_addresses:
#     if element in remove_list:
#         ip_addresses.remove(element)
#
# ip_addresses = " ".join(ip_addresses)
# with open(import_file, "w") as file:
#     file.write(ip_addresses)
#
# print(ip_addresses)

# TASK 8
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# with open(import_file, "r") as file:
#     ip_addresses = file.read()
#
# ip_addresses = ip_addresses.split()
#
# for element in ip_addresses:
#     if element in remove_list:
#         ip_addresses.remove(element)
#
# ip_addresses = " ".join(ip_addresses)
# with open(import_file, "w") as file:
#     file.write(ip_addresses)
#
# with open(import_file, "r") as file:
#     text = file.read()
#     print(text)

# TASK 9
# def update_file(import_file, remove_list):
#     with open(import_file, "r") as file:
#         ip_addresses = file.read()
#
#     ip_addresses = ip_addresses.split()
#
#     for element in ip_addresses:
#         if element in remove_list:
#             ip_addresses.remove(element)
#
#     ip_addresses = " ".join(ip_addresses)
#     with open(import_file, "w") as file:
#         file.write(ip_addresses)
#
#     with open(import_file, "r") as file:
#         text = file.read()
#     return text


# TASK 10
# allow = "allow_list.txt"
# remove = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
#
# update_file(allow, remove)
#
# with open("allow_list.txt", "r") as file:
#     text = file.read()
#
# print(text)
