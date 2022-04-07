weight_matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

# left-to-right fashion
# row-wise: wait, start, inside, change, done
# column-wise: wait, start, inside, change, done
# eg: a[0][1] == 1: wait -> start.
# eg: a[3][4] == 1: change -> done.
# eg: a[0][2] == 0: wait -x-> inside
# place1 --x--> place2
marking = [0, 0, 0]


def fire(originalMarking, weight1, weight2):
    return originalMarking - weight1 + weight2


marking[0] = int(input("Enter token count of place wait: "))
marking[1] = int(input("Enter token count of place inside: "))
marking[2] = int(input("Enter token count of place done: "))
print("Original net marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".inside" + ", " + str(
    marking[2]) + ".done" + "]")
if marking[0] > 0:
    start = True
    #  marking[0] represents place wait. If it has token then transition start is enabled (i.e. Boolean true)
else:
    start = False
# ====
if marking[1] > 0:
    change = True
    #  marking[1] represents place inside. If it has token then transition start is enabled (i.e. Boolean true)
else:
    change = False
print("Loading examination...")
print("Loading complete!")
print("=======================")
print("Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".inside" + ", " + str(
    marking[2]) + ".done" + "]")
premature = False  # used to track the premature end of examination, so that it prints "current marking"
# instead of "terminal marking"
while start == True or change == True:
    if start:
        print("Transition start is enabled!")
    if change:
        print("Transition change is enabled!")
    print("=======================")
    print("Choose an option: [1] for firing start; [2] for firing change, or [3] to stop examining.")
    choice = int(input("Your choice: "))
    if choice == 1:
        if not start:
            print("Can't fire, transition start is not enabled!")
        else:
            print("Firing transition start...")
            marking[0] = fire(marking[0], weight_matrix[0][1], weight_matrix[1][0])
            marking[1] = fire(marking[1], weight_matrix[2][1], weight_matrix[1][2])
            print(
                "Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".inside" + ", " + str(
                    marking[2]) + ".done" + "]")
    elif choice == 2:
        if not change:
            print("Can't fire, transition change is not enabled!")
        else:
            print("Firing transition change...")
            marking[1] = fire(marking[1], weight_matrix[2][3], weight_matrix[3][2])
            marking[2] = fire(marking[2], weight_matrix[4][3], weight_matrix[3][4])
            print(
                "Current marking: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".inside" + ", " + str(
                    marking[2]) + ".done" + "]")
    elif choice == 3:
        premature = True
        print("Done examining the net.")
        print(
            "Current marking is: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".inside" + ", " + str(
                marking[2]) + ".done" + "]")
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
    print("====================")
if not premature:
    print("Done examining the net.")
    print("Terminal marking is: " + "[" + str(marking[0]) + ".wait" + ", " + str(marking[1]) + ".inside" + ", " + str(
        marking[2]) + ".done" + "]")