def stringsplit(x):
    x = x.replace('_', ' ') 
    name, domain, regNo = x.split() 
    myDict = {"Name": name, "Domain": domain, "Registration Number": regNo}
    return myDict

encode_string = input("Enter 'Name', 'Domain', 'Registration No.' with any number of underscores in between: ")
newDict = stringsplit(encode_string)
print(newDict)