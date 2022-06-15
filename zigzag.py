import time
import sys

count = 0
try:
    while True:
        print(' '*count, end='')
        print('******')
        count += 1
        time.sleep(0.1)
except KeyboardInterrupt:
    while count != 0:
        print(' '*count, end='')
        print('******')
        count -= 1
        time.sleep(0.1)
    sys.exit()
