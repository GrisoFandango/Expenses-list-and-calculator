expenses = []
cost= []
#index list start refering from 0
index=(0)
#need a variable to increment everytime and expense is added
index2 = (-1) 
total = (0)
#Function to recall everytime the user want to add an expenses
def adding():
    name_exp = input ("Name of expensis: ")
    amount = input ("How much? ")
    #need to add exception if amount is different from a number
#append allow me to add to the list what is inside the ()
    expenses.append (name_exp)
    cost.append (int(amount))
    #need to add global to refer to the variable at the beginning
    global index2
    index2 += 1

counter = (1)
counter2 = counter+1
#loop that repeat the question to add and exepense or not
while counter != counter2:
    request = input ("Add an expenses? (y/n)")
# check the user answer (need to add exception if something else is typed)
    if request is ("y"):
        adding()    
    else:
#this loop print in different lines the corrispettive expenses and value
#increasing the index value each time 
        while index <= index2:           
            print (expenses[index] +": "+ str(cost[index]))            
            total = (total+cost[index])
            index += 1
        #this stop the loop at the beginnig
        counter = counter2
        
        print(total)
        
