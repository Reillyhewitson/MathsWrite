import os
while True:
    try:
        print('Input calculation (Ctrl - C to close)')
        x = input()
        file = open(os.getcwd()+'\\Maths.txt', 'a+')
        file.write(str(x))
        answer = round((eval(x)),2)
        file.write('='+str(answer)+'\n')
        print (answer)
        file.close()
    except KeyboardInterrupt:
        break
