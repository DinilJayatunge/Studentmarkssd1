progress_students = 0                                  #variables for progress,trailer,retriever and exclude
trailer_students = 0
retriever_students = 0
exclude_students = 0
Pass = 0                                                #variables for Pass,Defer and Fail
Defer = 0
Fail = 0
Valid = 0,20,40,60,80,100,120
Question =' '                                            #variable to ask user wheather to continue or exit
while True:
    try:
        Pass = int(input("Enter pass credits obtained: "))                        #User inputs Pass,Defer and Fail credits
        Defer = int(input("Enter defer credits obtained: "))
        Fail = int(input("Enter fail credits obtained: "))
        while (Pass or Defer or Fail)not in Valid:                        #Checking wheather the credits entered are in range
            print("Out of range")
            break
        while (Pass + Defer + Fail)== 120:                                        #Checking the progression outcome
            
            if Pass == 120:
                print("Progress")
                progress_students = progress_students + 1
                break
            elif Pass == 100:
                print("Progress-module trailer")
                trailer_students = trailer_students + 1
                break
            elif(Pass + Defer)>= Fail:
                print("Do not progress-module retriever")
                retriever_students = retriever_students + 1
                break
            else:
                print("Exclude")
                exclude_students = exclude_students + 1
                break
            
                
        while True:                                                                 
            Question = input("would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")        #Checking wheather the user wants to exit or enter another set of data
            if Question == 'q':
                continue
            elif Question == 'y':
                break
            else:
                print("Incorrect option selected")
    except ValueError:
          print("Integer required")                                                                                                #If the input is in the incorrect dta type a message will be printed to enter an integer
  


for i in range(len(Row1)) :
   print(Row1[i]+ ":" +(row[i] * '*' ))




    
   
            


  


