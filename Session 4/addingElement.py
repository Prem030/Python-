listItem = [ "Goku" , 12 , 3.45 , 'a']
# item = input("enter what you want to add in the list : ")
# listItem.append( item )
# print(f"afterr addition : {listItem}")

listItem2 = {"Dragon ball z " ,  "Naturo" , 1 ,23 ,434 , -10 , 2.34 , 4 + 5j }
print(listItem)

#append :- will add only one element in the list

listItem.append( 10 )
listItem.append("string1")
listItem.append('b')
listItem.append(4.55)
listItem.append(9 + 6j)

print(f"after adding element in list : {listItem}")
print("\n")

# difference between append and extend
listItem.append( [ 4 , 10 , 9 ] ) # this will add the whole element as one item 
print(listItem) 
print("\n")
listItem.extend( "String" ) # this will separate string as list and add into list
print(listItem)

#Insert 
# list.insert(index , element)
listItem.insert(200 , 2)
print(listItem)
listItem.insert( 8 , "string2" )
print(listItem)