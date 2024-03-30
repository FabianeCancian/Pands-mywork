def readModules ():
    modules = []
    moduleName = input("\tEnter the first Module name(blank to:").strip ()
    while moduleName != "":
        module = {}
        module ["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name(blank to:").strip()
        return modules