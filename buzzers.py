import os
import hid
import time
import buzzController
from playsound import playsound


print(" ____")
print("/\  _`\ ")
print("\ \ \L\ \   __  __   ____     ____       __    _ __    ____")
print(" \ \  _ <' /\ \/\ \ /\_ ,`\  /\_ ,`\   /'__`\ /\`'__\ /',__\ ")
print("  \ \ \L\ \\\ \ \_\ \\\/_/  /_ \/_/  /_ /\  __/ \ \ \/ /\__, `\ ")
print("   \ \____/ \ \____/  /\____\  /\____\\\ \____\ \ \_\ \/\____/")
print("    \/___/   \/___/   \/____/  \/____/ \/____/  \/_/  \/___/ ")
print()
print("by Joan Rios i Pla @_joanrios")
print()
print("Special thanks to https://pimylifeup.com/raspberry-pi-quiz-game-buzz-controllers/ for a guide on how to use the buzz controllers with python")
print()
print("Press CTRL+C to exit")
print("_____________________________________________________________")



file_path = os.path.abspath('./buzz2.mp3')

controller = buzzController.BuzzController()
controller.light_blinking = True
prev = 0

if controller:
    while True:
        try:
            first = controller.controller_get_first_pressed("red")
            if time.time() - prev > 0:
                if first != None:
                    print("First controller to press red: %d" % first)
                    controller.light_set(first, True)
                    playsound(file_path)
                    time.sleep(0)
                    controller.light_set(first, False)
                    prev = time.time()
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
