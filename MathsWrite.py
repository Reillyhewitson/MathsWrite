import os
while True:
    try:
        print('Input calculation (Ctrl - C to close)')
        x = input()
        file = open(os.getcwd()+'\\Maths.txt', 'a+') #Gets the current directory and opens or creates a file there
        file.write(str(x)) #writes the calculation put in by the user to the file
        answer = round((eval(x)),2) #this does rounding as well as doing the calculation by usin pythons eval function
        file.write('='+str(answer)+'\n') #adds the anwer to the inputted calculation and starts a new line
        print (answer)
        file.close()
    except KeyboardInterrupt:
        break

