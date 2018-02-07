# f = open("mycool_manifesto.txt", "w")
# f.write("A spectre is haunting ITP\n")
# f.write("The Spectre of Brooklyn")
# f.close()
#
# with open("somecool_file.txt", "w") as outfile:
#     outfile.write("some lines of text")


f = open("mycool_manifesto.txt", "r")
# data = f.read()
# print data

lines = f.readlines()
print lines
f.close()
