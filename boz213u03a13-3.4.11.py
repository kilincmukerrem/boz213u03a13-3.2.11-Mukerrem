beatles = []
print("Step 1:", beatles)

beatles.append("john Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(2):
    while True:
        new_member = input("Please enter a member:")
        if new_member == "Stu Sutcliffe" or new_member == "Pete Best":
            beatles.append(new_member)
            break
        else:
            print("wrong input")
print("Step 3:", beatles)

del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)
