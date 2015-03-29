import time
import webbrowser

total_loops = 3
current_loop = 0
print("Code \"Take a Break\" has commenced.")
print("In two hours we will initialize a video to signify that you should take a break. :)")
while current_loop < 1:
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=DfaCkVDi_bo")
    current_loop = current_loop + 1
    print ("Commencing iteration %d." % current_loop)
print("Shutting down program after %d iterations." % current_loop)
