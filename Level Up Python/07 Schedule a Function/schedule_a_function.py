import time


def schedule_function(result, p, text):
    print(f'Current time: {time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())}')
    print(f'Scheduled for: {time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(result))}')
    time.sleep(result - time.time())
    p(text)


# TEST CODE
schedule_function(time.time() + 10, print, 'Howdy!')
# print() scheduled for Sun Aug 14 20:39:28 2022
# Then one second later...
#
# Howdy!
