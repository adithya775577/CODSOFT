list=[]
def delItem(list, ind):
	del list[ind-1]

def printList(list):
	print("The tasks")
	i = 0
	for x in list:
		i+=1
		print( f"{i})  {x}" )
	print("\n")
		
def addItem(list):
	list.append(input("\nEnter the task: "))
	
while(True):
	printList(list)
	print("1) Add")
	print("2) Done")
	opt = int(input("\nSelect a option: ")) 
	if (opt == 1):
	    addItem(list)
	elif (opt == 2):
	    delItem(list, int(input("Enter the task number to mark as done")))
	print("\n\n")