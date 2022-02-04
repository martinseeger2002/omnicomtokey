import keyboard
import time

omnicomstxt = open("omnicommands.dat","r")
omnicoms = omnicomstxt.readlines()
omnicomstxt.close

line_number = 0

last_line_number = len(omnicoms)
print("You have 5 seconds before commands are sent to keyboard")
time.sleep(3)


while line_number <= last_line_number:
    if line_number == last_line_number-1:
        com = omnicoms[line_number]
        time.sleep(6)
        keyboard.write(com)
        keyboard.send('enter')
        print(com)
        exit()
    elif line_number < last_line_number-1:
        com = omnicoms[line_number]
        time.sleep(6)
        print(com)
        keyboard.write(com)
        keyboard.send('enter')
        line_number = line_number+1