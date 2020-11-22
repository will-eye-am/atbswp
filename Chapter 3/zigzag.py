import time, sys

indent = 0 
indent_increasing = True
iteration = 1 # added this myself to change up the zig zag a bit

try:
    while True:
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.075) # Pause in seconds
        if indent_increasing and iteration == 1:
            indent = indent + 1
            if indent == 5:
                indent_increasing = False
        
        elif indent_increasing and iteration == 2:
            indent = indent + 1
            if indent == 8:
                indent_increasing = False
        
        elif indent_increasing and iteration == 3:
            indent = indent + 1
            if indent == 3:
                indent_increasing = False
        
        elif indent_increasing and iteration == 4:
            indent = indent + 1
            if indent == 10:
                indent_increasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indent_increasing = True
                if iteration == 1:
                    iteration = 2
                elif iteration == 2:
                    iteration = 3
                elif iteration == 3:
                    iteration = 4
                else:
                    iteration = 1

except KeyboardInterrupt:
    sys.exit()            