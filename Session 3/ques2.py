n = int( input( "enter the number of terms : " ))
sum = 0
fact = 1
for i in range(1 , n+1):
    fact = fact * i 
    seriesElement =  i / fact
    sum +=  seriesElement

print(f"the sum of the series to the n terms is : {sum}")