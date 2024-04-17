

def roll_dice(dice_list):

    min_num = len(dice_list)
    max_num = sum(dice_list)
    print(min_num, max_num)

    print(dice_list)


dice_list = [4, 6, 6]
roll_dice(dice_list)
