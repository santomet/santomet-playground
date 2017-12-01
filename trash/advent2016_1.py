def old_1(vstup):
    instrukcie = vstup.split(", ")
    final = [0, 0]
    navstivene = []
    smer = 0  # 0:north 1:east 2:south 3:west
    for c in instrukcie:
        c_list = list(c)
        if c_list[0] == "L":
            smer -= 1
        elif c_list[0] == "R":
            smer += 1
        else:
            print("ERRORR!!!")

        if smer > 3:
            smer = 0
        if smer < 0:
            smer = 3

        c_list = c_list[1:]

        number_str = "".join(c_list)
        number = int(number_str)

        for i in range(number):
            if (smer == 0):  # north
                final[1] += 1
            if (smer == 1):  # east
                final[0] += 1
            if (smer == 2):  # south
                final[1] -= 1
            if (smer == 3):  # west
                final[0] -= 1

            navstivene.append(final[:])
            if (navstivene.count(final) == 2):
                print(final, " sme navstivili druhykrat :O, vzdialenost: ", (abs(final[0]) + abs(final[1])))

    print("point: ", final, " and distance: ", math.sqrt((final[0] ** 2 + final[1] ** 2)), "block distance = ",
          (abs(final[0]) + abs(final[1])))
