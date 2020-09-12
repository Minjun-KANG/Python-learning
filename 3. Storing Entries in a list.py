def get_names(num):
    names=[]
    for i in range(num):
        name = input("Enter name " + str(i+1)+":")
        names.append(name)
    return names

furry = get_names(3)
