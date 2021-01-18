
class Employee: #To begin, I must create a class, and use this class to later create a list of employees for the database
    def __init__(self,ID,Name,Age,job,years,is_from_mass): #Basic project requirements
        self.ID=ID
        self.Name=Name
        self.Age=Age
        self.job=job
        self.years=years 
        self.is_from_mass=is_from_mass
    def __str__(self):
        return(self.ID+"\t"+self.Name+"\t"+str(self.years)+"\t"+self.job)
