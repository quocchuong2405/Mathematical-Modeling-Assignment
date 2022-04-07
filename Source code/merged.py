weight_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# left-to-right fashion
# row-wise: wait, start, busy, change, docu, end, free, inside, done
# column-wise: wait, start, busy, change, docu, end, free, inside, done
# eg: a[0][1] == 1: wait -> start.
# eg: a[3][4] == 1: change -> docu.
# eg: a[0][2] == 0: wait -x-> busy
# place1 --x--> place2
marking = [2, 1, 1, 0, 0, 1]  # there are 6 places now


def fire(originalMarking, weight1, weight2):
    return originalMarking - weight1 + weight2


marking[0] = int(input("Enter token count of place wait: "))
marking[1] = int(input("Enter token count of place busy: "))
marking[2] = int(input("Enter token count of place inside: "))
marking[3] = int(input("Enter token count of place docu: "))
marking[4] = int(input("Enter token count of place free: "))
marking[5] = int(input("Enter token count of place done: "))
print("Original net marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
    marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
    marking[5]) + ".done" + "]")
if marking[0] > 0 and marking[4] > 0:
    start = True
    #  marking[0] and marking[4] represent places wait and free, respectively. If they both have tokens then transition start is enabled (i.e. Boolean true)
else:
    start = False

if marking[1] > 0 and marking[2] > 0:
    change = True
    #  marking[1] and marking[2] represent places busy and inside, respectively. If they both have tokens then transition start is enabled (i.e. Boolean true)
else:
    change = False

if marking[3] > 0:
    end = True
    #  marking[3] represents place docu. If it has token then transition start is enabled (i.e. Boolean true)
else:
    end = False

print("Loading examination...")
print("Loading complete!")
print("=======================")
print("Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
    marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
    marking[5]) + ".done" + "]")
premature = False  # used to track the premature end of examination, so that it prints "current marking"
# instead of "terminal marking"
while start == True or change == True or end == True:
    if start:
        print("Transition start is enabled!")
    if change:
        print("Transition change is enabled!")
    if end:
        print("Transition end is enabled")
    print("=======================")
    print(
        "Choose an option: [1] for firing start; [2] for firing change, [3] for firing end, or [4] to stop examining.")
    choice = int(input("Your choice: "))
    if choice == 1:
        if not start:
            print("Can't fire, transition start is not enabled!")
        else:
            print("Firing transition start...")
            marking[0] = fire(marking[0], weight_matrix[0][1], weight_matrix[1][0])
            marking[1] = fire(marking[1], weight_matrix[2][1], weight_matrix[1][2])
            marking[2] = fire(marking[2], weight_matrix[7][1], weight_matrix[1][7])
            marking[4] = fire(marking[4], weight_matrix[6][1], weight_matrix[1][6])
            print(
                "Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
                    marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
                    marking[5]) + ".done" + "]")
    elif choice == 2:
        if not change:
            print("Can't fire, transition change is not enabled!")
        else:
            print("Firing transition change...")
            marking[1] = fire(marking[1], weight_matrix[2][3], weight_matrix[3][2])
            marking[2] = fire(marking[2], weight_matrix[7][3], weight_matrix[3][7])
            marking[3] = fire(marking[3], weight_matrix[4][3], weight_matrix[3][4])
            marking[5] = fire(marking[5], weight_matrix[8][3], weight_matrix[3][8])
            print(
                "Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
                    marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
                    marking[5]) + ".done" + "]")
    elif choice == 3:
        if not end:
            print("Can't fire, transition end is not enabled!")
        else:
            print("Firing transition end...")
            marking[3] = fire(marking[3], weight_matrix[4][5], weight_matrix[5][4])
            marking[4] = fire(marking[4], weight_matrix[6][5], weight_matrix[5][6])
            print(
                "Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
                    marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
                    marking[5]) + ".done" + "]")
    elif choice == 4:
        premature = True
        print("Done examining the net.")
        print(
            "Current marking is: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
                marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
                marking[5]) + ".done" + "]")
        break
    else:
        print("Invalid choice!")
    if marking[0] > 0 and marking[4] > 0:
        start = True
        #  marking[0] represents place wait. If it has token then transition start is enabled (i.e. Boolean true)
    else:
        start = False

    if marking[1] > 0 and marking[2] > 0:
        change = True
        #  marking[1] represents place inside. If it has token then transition start is enabled (i.e. Boolean true)
    else:
        change = False

    if marking[3] > 0:
        end = True
        #  marking[1] represents place inside. If it has token then transition start is enabled (i.e. Boolean true)
    else:
        end = False
    print("====================")
if not premature:
    print("Done examining the net.")
    print("Terminal marking is: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".busy" + ", " + str(
        marking[2]) + ".inside" + ", " + str(marking[3]) + ".docu" + ", " + str(marking[4]) + ".free" + ", " + str(
        marking[5]) + ".done" + "]")