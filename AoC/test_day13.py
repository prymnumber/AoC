from day13 import *

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
l_file = get_file(l_file).split('\n')

layers = build_firewall(l_file)
packet = Packet()

delay_sec = -1
ct = 0
part2 = True
while True:
    packet.reset()
    for x in layers:
        x.reset()
    penalty = 0

    delay_sec += 1

    print('-----------------')
    penalty = travel_through_firewall(layers,packet,delay_sec,part2)
    if penalty !=0 :
        print('penalty:',penalty,'delayed sec:',delay_sec)
    else :
        print('!!!!!!!!!!!!!!!!!!!!! NO PENALTY:',penalty,'delayed sec:',delay_sec)
        break
