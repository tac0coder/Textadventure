items = {
    'pickaxe tier 1': [
        'Used to mine stuff at mine at 1 ore per 3 secs, chance of mining ores: diamond:1%,gold:10%,iron:25%,stone:64%',
        50, 'pickaxe'
    ],
    'pickaxe tier 2': [
        'Used to mine stuff at mine at 1 ore per 1.5 secs, chance of mining ores: diamond:5%,gold:30%,iron:40,stone:25%',
        100, 'pickaxe'
    ],
    'pickaxe tier 3': [
        'Used to mine stuff at mine at 5 ore per 1.5 secs, chance of mining ores: diamond:30%,gold:40%,iron:25%,stone:5%',
        250, 'pickaxe'
    ],
    'drill': [
        'Used to mine stuff at mine at 3 ore per 0.5 secs, chance of mining ores: diamond:1%,gold:10%,iron:25%,stone:64%',
        150, 'pickaxe'
    ],
    'miner': ['Mines stuff with \033[4mpickaxe\033[0m', 75, 'miner'],
    'Miner boost': ['Boost Miner Strength by 5%', 30, 'Miner Boost'],
    'dynamite': ['Blows stuff up in mine or explore modes', 50, 'dynamite']
}
code = {
    'pickaxe tier 1':
        (3, 1, 1),
    'pickaxe tier 2':
        (1.5, 2, 1),
    'pickaxe tier 3':
        (1.5, 3, 5), 'drill':
        (0.5, 1, 3),
    'miner': None,
    'Miner boost': None,
    'dynamite': None
}
tiers = {
    'pickaxe tier 1': {
        'stone': list(range(38, 102)),
        'iron': list(range(13, 38)),
        'gold': list(range(2, 12)),
        'diamond': [1]
    },
    'pickaxe tier 2': {
        'stone':  list(range(6, 31)),
        'iron': list(range(31, 71)),
        'gold': list(range(26, 56)),
        'diamond': [1, 2, 3, 4, 5]
    },
    'pickaxe tier 3': {
        'stone': [1, 2, 3, 4, 5],
        'iron': list(range(6, 31)),
        'gold': list(range(31, 71)),
        'diamond': list(range(71, 101))
    },
    'drill': {
        'stone': list(range(38, 102)),
        'iron': list(range(13, 38)),
        'gold': list(range(2, 12)),
        'diamond': [1]
    }
}
