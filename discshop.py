def mainStuff():
    n = input()
    lowest = None
    n_list = [int(c) for c in str(n)]
    for x in range(0, len(n_list)):
        mod_list = [jhagsf for jhagsf in n_list]
        new_int = ""
        # print(mod_list)
        mod_list.pop(x)
        for l in mod_list:
            new_int += str(l)
        if lowest is not None:
            if int(new_int) < int(lowest):
                lowest = new_int
        else:
            lowest = new_int
    lowest = int(lowest)
    print(lowest)


t = int(input())
for x in range(0, t):
    mainStuff()
