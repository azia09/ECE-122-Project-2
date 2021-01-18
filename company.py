    ### Import Modules
import database


'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''             
   
def main():
    eList=database.initialize()
    

if __name__ == '__main__':
    main()
    x=999 #This is an arbritrary value in order to use the while loop
    eList=database.initialize() #By setting the program to initialize before the loop, we can make sure the list is able to remove employees if necessary
    while (x != 0): #eList will represent the initialized database
        # If the initialization was inside the loop, all of the employees would be shown even if I try to adjust the list
        database.display_menu(2020)
        print("-------------------------------")
        print("")
        x=int(input("Enter command:"))
            
        if x==1:
            print("ID","Name","years","job",sep="\t") #Basic project formatting
            print("--------------------------")
            for e in eList: #This will print the database, which I earlier represented via eList
                print(e)
                
        if x==2:
            print("\n"+"#Employee 16")
            Sale=0  #I have set the program to count the number of times the variable appears in the list. 
            Engineer=0
            Manager=0
            Accountant=0
            years=0
            Age=0
            for e in eList:
                if e.job=="Manager":
                    Manager+=1 #By incrementing in this way, the program will have an accurate count of each job in this system
                    
                if e.job=="Sale":
                    Sale+=1
                                   
                if e.job=="Engineer":
                    Engineer+=1
                    
                if e.job=="Accountant":
                    Accountant+=1
                Age+=e.Age
                years+=e.years
                Age_Mean = "Age Mean:"+str(Age/len(eList)) #I will have all of my calculations reflect the incremented values, using the len() function
                Years_Mean = "#Years Mean:"+str(years/len(eList))
                    
            print(str("Manager:"),((Manager)/16)*100,"%") #These next four equations represent the job ratios
            print(str("Sale:"),((Sale)/16)*100,"%") 
            print(str("Engineer:"),((Engineer)/16)*100,"%")
            print(str("Accountant:"),((Accountant)/16)*100,"%")
            print("\n"+Age_Mean) #Age mean
            print(Years_Mean) #Year mean
            print("\n"+"Menu (Year: 2020)")

         
        if x==3:
            s=str(input("Enter employee ID: ")) #This will be the input location
            d = database.search_employee(eList,s);
            if d != -1: #This if statement and its parameters ensure that even if we add or remove employees, the database search will also update
                print(str(eList[d].Name),"is ",str(eList[d].Age)," years old and has a ",str(eList[d].job)," position.")
                print(str(eList[d].Name),"is from Massachussetts.")     #I used the variable d, to represent the index of the list

        if x==4:
            database.job_filter(eList) #For 4 and 5, I simply needed to callback my code from database

        if x==5:
            database.years_filter(eList)

        if x==6:
            s=str(input("Enter employee ID: "))
            ID = database.search_employee(eList,s)
            database.remove_employee(eList,ID)

        if x==7: #In this case, I need to set a variable for each parameter I have defined in the add_employee statement, which is located in the database file
            I=str(input("Enter employee ID: "))
            N=str(input("Enter Name: "))
            a=(input("Enter employee Age: "))
            j=str(input("Enter employee job: "))
            y=(input("Enter employee years: "))
            m=(input("Enter employee is from Mass?: "))
            database.add_employee(eList,I,N,a,j,y,m)

    print("Goodbye!")
        
