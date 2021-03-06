import random
## = function used to debug


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
    ## print(tile_list)
    # building up the mountain list randomly with the numbers in tile list by the below method
    # choosing the list inside tile_list(I don't know how to remove extra list)
    # -> random to choose any tile in the list by using pop[]
    # for loop/ while loop until the lists are empty
    while not tile_list == [[]]:
        list_in_tile_list = tile_list[0]
        c = random.randint(0, len(list_in_tile_list) - 1)
        tile_pop = list_in_tile_list.pop(c)
        mountain.append(tile_pop)
    print(mountain)

    # defining mountains with unfinished state, finished state and unused state
    unfinished_mountain = mountain
    finished_mountain, dead_wall = slice_mountain(unfinished_mountain)
    ## print(finished_mountain)
    ## print(dead_wall)
    dora_indicator = print_dora_indicator(dead_wall)
    # return the mountains output
    return mountain, finished_mountain, dead_wall, dora_indicator


def build_another_mountain():
    """This function is to build the mountain for the game, but the method is different from build_mountain()"""
    # building empty lists
    mountain = []
    # looping to keep running adding random tile to mountain
    while len(mountain) < 136:
        tiles = random.randint(1, 9)

        # limiting tiles to 28 times(1~7), 21 times(8~9)
        mountain.append(tiles)


def slice_mountain(unfinished_mountain):
    finished_mountain = unfinished_mountain[0:120]
    dead_wall = unfinished_mountain[121:135]
    return finished_mountain, dead_wall


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


def print_dora_indicator(unused_mountain):
    """This function is to define the dora indicator, works with dora() function"""

    print("The dora indicator is:", unused_mountain[8])
    dora_indicator = unused_mountain[8]
    return dora_indicator


def dora(dora_indicator):
    """This function is to show dora and make dora useful"""
    # all tiles list is used to show how the tiles arrange and how dora indicator works to show dora
    dora_all_tiles = [['1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '1p'],
                      ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '1s'],
                      ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '1m'],
                      ['1z', '2z', '3z', '4z', '1z'],
                      ['5z', '6z', '7z', '5z']]
    # using index_2d function to get the indices of dora
    count, dora_indicating = index_2d(dora_all_tiles, dora_indicator)
    dora = dora_all_tiles[count][dora_indicating + 1]
    print("Dora: ", dora)
    return dora


def index_2d(mylist, indicator):
    """This function is from stackoverflow, and it is used to get items indices from a 2d list"""
    for count, lists in enumerate(mylist):
        if indicator in lists:
            return count, lists.index(indicator)


def get_starting_hand():
    """This function is used to get the tiles for starting hand"""
    # get first 14 tiles from finished_mountain
    starting_hand = []
    for i in range(0, 14):
        starting_hand.append(finished_mountain.pop(0))
    ## print(starting_hand)
    ## print(finished_mountain)
    true_starting_hand = sort_tiles(starting_hand)
    print("Starting hands: ", true_starting_hand)
    return true_starting_hand


def sort_tiles(hand):
    """This function is used to sort the tiles"""
    # sort tiles by m,p,s,z
    hand.sort(key = lambda item: (list(item)[1], list(item)[0]))
    ## print(starting_hand)
    # making the arranged starting hand tidy, becoming a format of "123m456p789s11177z"
    # join the separated strings first
    hand = "".join(hand)
    # idea: while not count(s)==1, strip(s)> replace now
    # repeat for four type of tiles
    while not hand.count("m") <= 1:
        hand = hand.replace("m", "", hand.count("m") - 1)
    while not hand.count("p") <= 1:
        hand = hand.replace("p", "", hand.count("p") - 1)
    while not hand.count("s") <= 1:
        hand = hand.replace("s", "", hand.count("s") - 1)
    while not hand.count("z") <= 1:
        hand = hand.replace("z", "", hand.count("z") - 1)
    ## print(hand)
    return hand

def mahjong_logic():
    """This function is used to define the basic logic of mahjong combinations, like what is a winning hand is like"""


def ready_hand():
    """This function is used to"""
    #


def effective_pairs():
    """This function is used to distinguish """
    #


def effective_tiles():
    """This function is used to distinguish which tile is effective to shanten"""
    #


def counting_shanten():
    """This function is used to counting shanten, meaning how far(how many tiles at least are needed) to reach tenpai"""
    # logic of counting shantan


def gamemode_explanation():
    """This function is used for explaining details of different gamemode,
    and exact things you need to do when you play"""


def gamemode():
    """This function is used for player to choose the gamemode that they want"""


# main function
if __name__ == "__main__":
    mountain, finished_mountain, unused_mountain, dora_indicator = build_mountain()
    dora = dora(dora_indicator)
    starting_hand = get_starting_hand()