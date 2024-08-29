
# TASK 1
# import_file = "allow_list.txt"
# remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
#
# with open(import_file, "r") as file:
#     print(file.read())
# print(remove_list)

# TASK 2
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
with open(import_file, "r") as file:
    # TASK 3
    ip_addresses = file.read()
print(ip_addresses)
