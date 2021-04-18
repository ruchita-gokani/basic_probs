"""
# We're in a room with a row of lightbulbs. Below each bulb is a switch that
# controls just the bulb above it.
# When we begin, all the lightbulbs are off. The first person flips the switch
# on every bulb, turning them all on. The second person then comes through
# and flips the switch on every 2nd bulb, turning half of them off. The
# third person then comes through, and flips the switch on every 3rd bulb,
# turning some of them off and some of them on (the ones which person #2
# turned off). The fourth person flips the switch on every 4th bulb, and so on
# down the line, up until the very last person, who flips the switch for just
# the last bulb.
# Write a function that, given a number of bulbs N, prints the number of bulbs
# that will be in the "ON" position once all N people have gone through and
# done their switch flipping.
# For example:
# how_many_bulbs_on(1) => 1
# how_many_bulbs_on(3) => 1
# how_many_bulbs_on(5) => 2
"""


def how_many_bulbs_on(N):
    fact = {}
    on_bulbs = 0
    for i in range(1,N+1):
        for j in range(1,i+1):
            if i%j == 0:
                if i in fact:
                    fact[i].append(j)
                else:
                    fact[i] = [j]

        if len(fact[i]) % 2 == 1:
            on_bulbs += 1
    return on_bulbs


if __name__ == '__main__':
    num_of_bulbs = int(input())
    print(how_many_bulbs_on(num_of_bulbs))

