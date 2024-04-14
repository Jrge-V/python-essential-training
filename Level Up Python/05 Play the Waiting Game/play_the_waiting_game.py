import random
import time


def waiting_game(elapsed_t, difference_t):
    ran_number = random.randint(2, 4)
    print(f'Your target time is {ran_number} seconds')
    input('--Press Enter to Begin--')
    start_time = time.time()
    input(f'Press Enter again after {ran_number} seconds...')
    end_time = time.time()

    elapsed_t = round(end_time - start_time, 3)

    if elapsed_t == ran_number:
        return f'Elapsed time {elapsed_t}\nCONGRATS!'
    elif elapsed_t > ran_number:
        difference_t = round(elapsed_t - ran_number, 3)
        return f'Elapsed time {elapsed_t}\n({difference_t} seconds too slow)'
    else:
        difference_t = round(ran_number - elapsed_t, 3)
        return f'Elapsed time {elapsed_t}\n({difference_t} seconds too fast)'


elapsed_time, difference_time = 0, 0
print(waiting_game(elapsed_time, difference_time))
