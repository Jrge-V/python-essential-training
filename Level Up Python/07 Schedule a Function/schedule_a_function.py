import time


def schedule_function(result, p, *args):
    print(f'Current time: {time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())}')
    print(f'Scheduled for: {time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(result))}')
    time.sleep(result - time.time())
    p(*args)


# TEST CODE
schedule_function(time.time() + 1, print, 'Howdy!', 'BEEP!')
# print() scheduled for Sun Aug 14 20:39:28 2022
# Then one second later...
#
# Howdy!
