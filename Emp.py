DataBase = dict()

while(1):
	print("|************************************************|")
	print("| To Add New Empolyee Press 1    :               |")
	print("| To Print Employee Data press 2 :               |")
	print("| To Delete Employee Press 3     :               |")
	print("|************************************************|")
	
	choice = int(input("Please Select Your Operation : "))
	if(choice == 1):
		ID = int(input("Please enter employee ID: "))
		while ID in DataBase:
			ID = input("ID already exist, please try another one: ")
		name   = input("Please Enter Employee Name: ")
		job    = input("Please Enter Employee Job : ")
		salary = int(input("Please Enter Employee Salary : "))
		DataBase[(ID)] = dict(Name = name, Job = job ,Salary = salary)
		
	elif (choice == 2):
		ID = int(input("Please enter employee ID: "))
		if ID in DataBase:
			print("Employee Name : " , DataBase[ID]["Name"])
			print("Employee Job : "  , DataBase[ID]["Job"])
			print("Employee Salary :" , DataBase[ID]["Salary"])
		else:
			print("Employee Not Found")
			
	elif (choice == 3):
		ID = int(input("Please enter employee ID: "))
		if ID in DataBase:
			del(DataBase[ID])
			print("Employee Deleted")
		else :	
			print("Employee Not Found")
	else:
		print("Wrong Choice, Please try again")		