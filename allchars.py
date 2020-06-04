data = ["\\x{}".format(hex(i)[2:]) for i in range(0,256)]

data = "".join(data)
print(data)
