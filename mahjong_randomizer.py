import random


def build_mountain():
    """This function is to build the mountain for the game"""
    # building empty mountain list
    mountain = []
    pinzi_list = []
    souzi_list = []
    manzi_list = []
    honor_tile_list = []

    # run define mahjong type function
    mahjong_type_tiles(pinzi_list, souzi_list, manzi_list, honor_tile_list)

    # make a tile list that contain all of 4 types of tiles
    tile_list = [pinzi_list + souzi_list + manzi_list + honor_tile_list]
    print(tile_list)
    # building up the mountain list randomly with the numbers in tile list by the below method
    # random to choose 1 out of 4 list(not popping out) -> random to choose any tile in the list by using pop[]
    # for loop/ while loop until the lists are empty
    while not tile_list == [[]]:
        c = random.randint(0, len(tile_list[0][0]) - 1)
        list_in_tile_list = tile_list[0]
        tile_pop = list_in_tile_list.pop(c)
        mountain.append(tile_pop)
        print(list_in_tile_list)
    # return the mountain out
    print(mountain)
    return mountain


def build_another_mountain():
    """This function is to build the mountain for the game, but the method is different from build_mountain()"""
    # building empty lists
    mountain = []
    # looping to keep running adding random tile to mountain
    while len(mountain) < 136:
        tiles = random.randint(1, 9)

        # limiting tiles to 28 times(1~7), 21 times(8~9)
        mountain.append(tiles)


def mahjong_type_tiles(pinzi_list, souzi_list, manzi_list, honor_tile_list):
    """This function is to define the type of mahjong index,, correspond to each tile. Also filling up the tile list."""
    # filling the empty tile list with tiles
    # pinzi = p, souzi = s, manzi = m, honor_tile = z
    # honor tile arrangement: 1~7 = east, south, west, north, haku, hatsu, chun
    pinzi = ('1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p')
    souzi = ('1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s')
    manzi = ('1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m')
    honor_tile = ('1z', '2z', '3z', '4z', '5z', '6z', '7z')
    # each number of tile has 4 with respect to each colour
    for a in range(0, 4):
        pinzi_list.extend(pinzi)
        souzi_list.extend(souzi)
        manzi_list.extend(manzi)
        honor_tile_list.extend(honor_tile)
    return pinzi_list, souzi_list, manzi_list, honor_tile_list



build_mountain()
# build_another_mountain()