contacts = [[], []]

def addCon(name, num):
	contacts[0].append(name)
	contacts[1].append(num)
	
def search(cred,opt):
    if opt == 0:
        for x in range (0, len(contacts[0])):
            if cred == contacts[0][x]:
                print(f"{contacts[0][x]} - {contacts[1][x]}")
    else:
         for x in range (0, len(contacts[1])):
            if cred == contacts[1][x]:
                print(f"{contacts[0][x]} - {contacts[1][x]}")
    

def listCon():
	print("\n\n")
	for x in range(0, len(contacts[0])):
		print(f"{contacts[0][x]} - {contacts[1][x]}")
	print("\n\n")

while(True):
	print("1) Add Contact")
	print("2) List Contact")
	print("3) Search by Name")
	print("4) Search by Number")
	opt = int(input("Enter your choice: "))
	if(opt == 1):
		addCon(input("Enter Name: ").lower(), int(input("Enter the number: ")))
	elif (opt == 2):
		listCon()
	elif(opt == 3):
		search(input("\nEnter the Name: ").lower(),0)
	elif(opt == 4):
		search(int(input("\nEnter thr Number: ")),1)