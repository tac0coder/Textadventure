import shopp
import os
import pickle

inventorydic = {}
ores = []

# TODO make purchase and sell function

# FIXME not returning ores


def mine():
    global ores
    if 'miner' in list(inventorydic):
        ores = inventorydic['pickaxe'].trigger()


def exit():
    if input('Admin password?: ') == '12ab34cd':
        # add funcs to use in shell
        def listtostr(args):
            string = ''
            for var in args:
                string += var
                return string

        def format_table():
            """
            prints table of formatted text format options
            """
            for style in range(8):
                for fg in range(30, 38):
                    s1 = ''
                    for bg in range(40, 48):
                        format = ';'.join([str(style), str(fg), str(bg)])
                        s1 += '\x1b[%sm %s \x1b[0m' % (format, range(format))
                        print(s1)
                    print('\n')

        def clear():
            from os import system as cmd
            cmd('clear')
        while True:
            prog = input('\x1b[6;33m'+'>>> '+'\x1b[0m')
            getothercode = ''
            othercode = []
            try:
                if prog[len(prog)-1] == ':':
                    while True:
                        getothercode = input('\x1b[7;40m...\t\x1b[0m ')
                    if not getothercode == '':
                        othercode.append(getothercode)
                    else:
                        for var in range(0, len(othercode)):
                            othercode[var] = f"\n\t{othercode[var]}"
                            print(othercode)
                            try:
                                exec(prog+listtostr(othercode))
                                break
                            except KeyboardInterrupt or Exception as e:
                                print('\x1b[6;31m'+str(e)+'\x1b[0m')
                                break
                else:
                    try:
                        exec(prog)
                    except Exception as e:
                        print('\x1b[6;31m'+str(e)+'\x1b[0m')

            except:
                pass


def percent(tier):
    if not tier in list(tiers):
        raise IndexError('Tier not found in "tiers"')
    from random import randint as rd
    var = rd(1, 101)
    type_mined = None
    for percent in list(tiers[tier]):
        if var in tiers[tier][percent]:
            type_mined = percent
            break
    return type_mined


def inventory():
    global inventorydic
    for var in inventorydic:
        print(
            f'{inventorydic[var].quantity}x  {inventorydic[var].item}:\n{inventorydic[var].description}'
        )


def listtostr(args):
    string = ''
    for var in args:
        string += var
    return string


def message(text, timeout):
    from os import system as cmd
    from time import sleep as sl
    doneletters = []
    sl(1)
    for var in text[0:len(text) - 1]:
        print(listtostr(doneletters) + var)
        sl(timeout)
        cmd('clear')
        doneletters.append(var)
    print(listtostr(doneletters) + text[text.index(var) + 1])


class item():
    def __init__(self,
                 quantity: int,
                 item: str,
                 description: str,
                 code: list = None, type=None):
        global inventorydic
        self.quantity = str(quantity)
        self.item = item
        self.description = description
        self.get = (self.quantity, self.item, self.description)
        self.code = code
        inventorydic[type] = self
# FIXME:TRY scrap it and change the trigger function to 'mine' and make a new function for miners?

    def trigger(self):
        if self.code != None:
            for line in self.code:
                exec(line)
            try:
                return ores
            except:
                pass


message(
    "Hello " + input("What's your name? ") +
    ",I heard you wanted to start a mine.\nWell here is a starter kit.\nAlso, the commands are mine,inventory,sell,shop,explore, and (in explore) open,n,e,s,w,map.\nYou’ll learn more later.\n\n\nStarter Kit:\n1x pickaxe\n5x dynamite\n500 coins,\nand a miner. \n\nHit ENTER to continue. ",
    0.05)
dynamite = item(
    5, 'dynamite', 'Blows stuff up in mine or explore modes', type='dynamite')
coins = item(500, 'coins', 'Money to be used in shop', type='coins')
pickaxe = item(
    1, 'pickaxe tier 1',
    'Used to mine stuff at mine or explore at 1 ore per 3 secs, chance of mining ores: diamond:1%,gold:10%,iron:25%,stone:64%',
    [
        'import run', 'ores = run.main(3,1,1)', 'print("Done Mining!")'], 'pickaxe')
miner = item(1, 'miner', 'Mines ores with \033[4mpickaxe\033[0m', type='miner')
if input() == '':

    while True:
        prog = input('\x1b[6;33m' + 'mining-sim>>> ' + '\x1b[0m')
        if prog in ['mine', 'inventory', 'sell', 'shop', 'explore', 'exit']:
            try:
                exec(prog + '()')
            except Exception as e:
                print('\x1b[6;31m' + str(e) + '\x1b[0m')
        else:
            print("\x1b[6;31mYour command isn't a valid command.\x1b[0m")
