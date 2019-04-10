import time

start_time = time.time()
x = 1 # displays the frame rate every 1 second
counter = 0
while True:

    ########################
    # your fancy code here #
    ########################

    counter+=1
    if (time.time() - start_time) > x :
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()