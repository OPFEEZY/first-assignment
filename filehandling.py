# file = open("demofile.txt")
# print(file.read())
# file.close()


# with open("demofile.txt") as file:
#     print(file.read())


# with open("demofile.txt", mode="a") as file:
#     file.write("\nThis file was appended by python")

import os
with open("demofile2.txt", mode="w") as file:
    file.write("This file was created by python")

os.remove("demofile2.txt")