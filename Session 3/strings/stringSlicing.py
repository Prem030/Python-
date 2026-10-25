str = "A QUICK BROWN FOX JUMPS OVER THE LITTLE LAZY DOG"
#A QUICK B  R  O  W  N  F  O  X     J  U  M  P  S     O  V  E  R     T  H  E     L  I  T  T  L  E     L  A  Z  Y     D  O  G 
#012345678  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 
#string slicing
# str[ starting_index : ending_index : step_size]
print( str[ 0: 19] )
print( str[ 2 : ]) # will print element from index 2 to last element of the string
print( str[ : 20 ]) # will print element from starting of the strin to the end of the string
print( str[ : ]) # will print entire string start to finish

# step size
print( str[ : :2])# print entire string but take a leap of 2
print( str[ 45 : 3 : -1 ]) # will print string from backward

# to print reverse of a string
print( str[ : : -1])
reversed_string = str[ : : -1]
print(f"The reverse of the string : {str[ : : -1]}")
# NOTE:- Whenever working with negative indexing starting index > ending indexing
print(f"str[ -20 : -45] :{str[ -10 : -40 : -1 ]}")