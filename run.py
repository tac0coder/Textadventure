def percent(tier):
    from shopp import tiers
    if not tier in list(tiers):
        raise IndexError('Tier not found in "tiers"')
    from random import randint as rd
    var = rd(1, 101)
    type_mined = None
    for percent in list(tiers[tier]):
        if var in tiers[tier][percent]:
            type_mined = percent
            break
    if type_mined == None:
        type_mined = 'gold'
    return type_mined


def main(timesleep, tier, ores_per):
    from time import sleep as sl
    ores = []
    print('Hit CTRL+C to stop mining')
    while True:
        try:
            sl(timesleep)
            for i in range(1, ores_per+1):
                ores.append(percent(f"pickaxe tier {tier}"))
            print(f'Ores mining:{ores[-1]},Ores Mined:{len(ores)}')
        except KeyboardInterrupt as e:
            break
    return ores
