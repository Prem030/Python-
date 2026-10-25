str = "my name is Prem Dhara"
strUpper = "MY NAME IS PREM DHARA"
strCamel = "My nAme IS prEm DhaRa"
print(str.capitalize()) # will make the frist letter of the sentence capital
print(str.title()) # This will make first letter of every wordk capital
print( strUpper.lower()) # tHIS will make upper character lower case 
print( str.upper())
print( strCamel.swapcase())


name = "Prem Dhara"
email = "premdh8@gmail.com"
age = 24
print( "hello everyone my name is {} and my contact email is {}".format( name, email))
#another method
print("hello everyone my name is {1} and my contact email is {0}".format(email,name))
 
