from Employee import Employee


def initialize():  #I will set the initialization at the top
    Employee1=Employee("E04","Andrea",37,"Sale",8,True)
    Employee2=Employee("E11","Bob",28,"Engineer",4,False)
    Employee3=Employee("E09","Brooke",34,"Engineer",5,True)
    Employee4=Employee("E12","Connor",27,"Engineer",4,True)
    Employee5=Employee("E16","James",25,"Accountant",3,False)
    Employee6=Employee("E24","Jenna",24,"Engineer",1,False)
    Employee7=Employee("E02","John",45,"Manager",17,True)
    Employee8=Employee("E03","Julie",37,"Engineer",10,True)
    Employee9=Employee("E01","Kate",48,"Manager",24,False)
    Employee10=Employee("E08","Keith",28,"Engineer",6,False)
    Employee11=Employee("E23","Kelly",25,"Engineer",1,False)
    Employee12=Employee("E17","Luke",33,"Sale",3,False)
    Employee13=Employee("E18","Mark",34,"Sale",3,True)
    Employee14=Employee("E22","Pat",26,"Engineer",2,True)
    Employee15=Employee("E15","Taylor",32,"Accountant",4,True)
    Employee16=Employee("E05","Tony",34,"Sale",8,False)
    EmployeeData= [Employee1, Employee2, Employee3, Employee4, Employee5, Employee6, Employee7, Employee8, Employee9, Employee10,Employee11, Employee12, Employee13, Employee14, Employee15, Employee16]

    return(EmployeeData)

def display_menu(date): #This is the given code
    print("\nMenu (Year:"+str(date)+")");
    print("================");
    print("1-List Employees\t2-General Information\t3-Employee Information");
    print("4-Filter per job\t5-Filter per #years\t6-Remove Employee")
    print("7-Add Employee\t\t8-Change Date\t\t0-Exit");


def search_employee(eList,s): #My parameters are my list, and s, which is a string I set up as a location for the input
   found=False
   count = -1
   for e in range(len(eList)):
            if s==eList[e].ID:
                found=True
                count = e #The count represents the index of the array. I used the count system in order to ensure that even if I add or remove employees later, the employee search is not affected
                break
   if found==False:
       print("Employee not found")
   return count

def job_filter(eList): #For this task, I will first set up a series of variables I intend to use
    Manager=0
    M=[]
    Sale=0
    Engineer=0
    Accountant=0
    print("ID","Name","years","job",sep="\t")
    print("--------------------------")
    for e in range(len(eList)): #I will need my loop to scan the entire list, hence the use of the len() and range() functions
        if str(eList[e].job)=="Manager":
            Manager+=1      #I have set the program to count the number of times the variable appears in the list. The program will scan the list and provide a list of the jobs I have it scanning for
            print(str(eList[e].ID),str(eList[e].Name),str(eList[e].years),"Manager",sep="\t")
    for e in range(len(eList)):
        if str(eList[e].job)=="Sale":
            Sale+=1
            print(str(eList[e].ID),str(eList[e].Name),str(eList[e].years),"Sale",sep="\t")
    for e in range(len(eList)):
        if str(eList[e].job)=="Accountant":
            Accountant+=1
            print(str(eList[e].ID),str(eList[e].Name),str(eList[e].years),"Accountant",sep="\t")
    for e in range(len(eList)):
        if str(eList[e].job)=="Engineer":
            Engineer+=1
            print(str(eList[e].ID),str(eList[e].Name),str(eList[e].years),"Engineer",sep="\t")
    #By setting up all these loops, the program will sort the jobs together and produce them in a list, with the job order I have chosen for the loops.

def years_filter(eList):
    for i in range(0,len(eList)):
        for y in range(0,len(eList)):
            if eList[i].years >= eList[y].years: #In this case, I have the program scan through my list (eList), and I use a system of arrays to sort through the years
                temp = eList[y]
                eList[y] = eList[i]
                eList[i] = temp #Temoprary variable that will serve as a "garbage collector" for when eList[i] updates
    for e in eList:
                print(e)


def remove_employee(eList,ID):
    del eList[ID]

def add_employee(elist,ID,name,age,job,years,is_from_mass): #I have set the parameters as elist,ID,name,age,job,years,is_from_mass
    Employee1=Employee(ID,name,age,job,int(years),is_from_mass) #We'll force years to be a integer for task 5
    elist.append(Employee1) #This function will add a new element to the last index of the list
                            #It will create a new array
