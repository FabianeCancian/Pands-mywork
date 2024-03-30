def displayMenu ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input ("Type one letter a/v/q: ").strip ()
    return choice

def doAdd (students):
    currentStudent = {}
    currentStudent ["name"]=input ("enter :")
    currentStudent ["modules"]= readModules()
    students.append(currentStudent)

def readModules ():
    modules = []
    moduleName = input("\tEnter the first Module name(blank to quit):").strip ()
    while moduleName != "":
        module = {}
        module ["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name(blank to quit):").strip()
    return modules

def doView(students):
    print (students)

students = []
choice = displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print ("\n\n please select either a,v or q")
    choice=displayMenu()
