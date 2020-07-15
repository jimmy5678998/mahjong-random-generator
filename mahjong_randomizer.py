import random


def build_mountain():
    # building empty lists
    pinzi_list = []
    souzi_list = []
    manzi_list = []
    honor_tile_list = []
    mountain = []
    # filling the empty tile list with tiles
    # first for loop is for filling the 1~9 number tiles
    # the second for loop(inner one) is for generating 4 tiles for each number
    for i in range(1, 10):
        for a in range(0, 4):
            pinzi_list.append(i)
            souzi_list.append(i)
            manzi_list.append(i)
    # same idea, but this is specially make for honor tile, as it only has 7 types of tiles
    for i in range(1,8):
        for a in range(0,4):
            honor_tile_list.append(i)

    # make a tile list that contain all of 4 types of tiles
    tile_list = [list((pinzi_list, souzi_list, manzi_list, honor_tile_list))]

    # building up the mountain list randomly with the numbers in tile list by the below method
    # random to choose 1 out of 4 list(not popping out) -> random to choose any tile in the list by using pop[]
    # for loop/ while loop until the lists are empty
    while not tile_list == [[], [], [], []]:
        b = random.randint(0, len(tile_list) - 1)
        chosen_list = tile_list[b]
        c = random.randint(0, len(chosen_list) - 1)
        mountain = chosen_list.pop(c)
        print(mountain)
    # return the mountain out
    print(mountain)
    return mountain


build_mountain()