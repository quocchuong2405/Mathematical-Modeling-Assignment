weight_matrix = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0]
]
# left-to-right fashion
# row-wise: free, start, busy, change, docu, end
# column-wise: free, start, busy, change, docu, end
# eg: a[0][1] == 1: free -> start.
# eg: a[3][4] == 1: change -> docu.
# eg: a[0][2] == 0: free --x--> busy
# place1 --x--> place2

marking = [0, 0, 0]


def fire(originalMarking, weight1, weight2):
    return originalMarking - weight1 + weight2


marking[0] = int(input("Enter token count of place free: "))
marking[1] = int(input("Enter token count of place inside: "))
marking[2] = int(input("Enter token count of place docu: "))
print("Original net marking: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
    marking[2]) + ".docu" + "]")

#  we move on to set the initial enabledness
if marking[0] > 0:
    start = True
    #  marking[0] represents place free. If it has token then transition start is enabled (i.e. Boolean true)
else:
    start = False

if marking[1] > 0:
    change = True
    #  marking[1] represents place busy. If it has token then transition change is enabled (i.e. Boolean true)

else:
    change = False

if marking[2] > 0:
    end = True
    #  marking[2] represents place docu. If it has token then transition end is enabled (i.e. Boolean true)
else:
    end = False
print("Loading examination...")
print("Loading complete!")
print("=======================")
print("Current marking: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
    marking[2]) + ".docu" + "]")
premature = False
while start == True or change == True or end == True:
    if start:
        print("Transition start is enabled!")
    if change:
        print("Transition change is enabled!")
    if end:
        print("Transition end is enabled!")

    print("Choose an option: [1] for firing start; [2] for firing change, [3] for firing end, or [4] for stop.")
    choice = int(input("Your choice: "))
    if choice == 1:
        if not start:
            print("Can't fire, transition start is not enabled")
        else:
            print("Firing transition start...")
            marking[0] = fire(marking[0], weight_matrix[0][1], weight_matrix[1][0])
            marking[1] = fire(marking[1], weight_matrix[2][1], weight_matrix[1][2])
            print("Current marking: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
                marking[2]) + ".docu" + "]")
    elif choice == 2:
        if not change:
            print("Can't fire, transition change is not enabled")
        else:
            print("Firing transition change...")
            marking[1] = fire(marking[1], weight_matrix[2][3], weight_matrix[3][2])
            marking[2] = fire(marking[2], weight_matrix[4][3], weight_matrix[3][4])
            print("Current marking: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
                marking[2]) + ".docu" + "]")
    elif choice == 3:
        if not end:
            print("Can't fire, transition end is not enabled")
        else:
            print("Firing transition end...")
            marking[2] = fire(marking[2], weight_matrix[3][4], weight_matrix[4][3])
            marking[0] = fire(marking[0], weight_matrix[0][5], weight_matrix[5][0])
            print("Current marking: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
                marking[2]) + ".docu" + "]")
    elif choice == 4:
        premature = True
        print("Done examining the net.")
        print("Current marking is: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
            marking[2]) + ".docu" + "]")
        break
    else:
        print("Invalid choice!")
    if marking[0] > 0:
        start = True
    else:
        start = False
    # ====
    if marking[1] > 0:
        change = True
    else:
        change = False
    if marking[2] > 0:
        end = True
    else:
        end = False
    print("====================")
if not premature:
    print("Done.")
    print("Terminal marking is: " + "[" + str(marking[0]) + ".free" + ", " + str(marking[1]) + ".busy" + ", " + str(
        marking[2]) + ".docu" + "]")