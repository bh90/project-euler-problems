import math

def min_cards(R,C):
    # R+1 is the number of gates we have to pass hence it is <= the minimum
    if C >= R+1:
        return R + 1


    #this is the room for which C is enough to get out.
    # for example - R=3, C=3, R-C+1=1 and as we saw 3 cards at room 1 will take as out.
    curr_room = R - C + 1
    cards_in_last_room = C
    total = C
    while curr_room > 0:
        # on each step from room x to room x+1 we will use 1 card to get to x+1,
        # 1 card to get back to x and C-2 we can store on x+1
        cards_to_store = C - 2

        # if room x+1 need Y cards, and in each step we can leave C-2 cards on
        # x+1, then at total we Y/(c-2) steps (and round up the result because
        # we can't have 'half' step.
        num_of_transfers = math.ceil(cards_in_last_room / cards_to_store)

        #special case - if only c-1 cards left at room x we can take them all together to room x+1
        if cards_in_last_room % cards_to_store == 1:
            num_of_transfers = cards_in_last_room // cards_to_store

        if cards_to_store == 1:
            num_of_transfers = cards_in_last_room - 1

        # for each transfer of cards from x to x+1 we need 1 card for each direction, except
        # of the last transfer at which we won't come back to room x
        total += num_of_transfers * 2 - 1
        cards_in_last_room = total
        curr_room -= 1

    return total





sig = 0
for c in range(3,41):
    sig += min_cards(30,c)
print(sig)