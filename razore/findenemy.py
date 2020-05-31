from System.Collections.Generic import List
from System import Byte
import sys

def FindEnemy():
    fodder = []
    tfilter = Mobiles.Filter()
    tfilter.Enabled = True
    tfilter.RangeMin = 0
    tfilter.RangeMax = 9
    # tfilter.IsHuman = False
    tfilter.IsGhost = False
    tfilter.Notorieties = List[Byte](bytes([3,4,5,6]))
    tfilter.Friend = False
    enemies = Mobiles.ApplyFilter(tfilter)
    Mobiles.Select(enemies, 'Nearest')
    if len(enemies) < 1:
        Player.HeadMessage(4095, 'No hostiles detected')
        return None

    Target.ClearLastandQueue()
    Target.Cancel()

    #makes list with [Serial, DistanceTo]
    for enemy in enemies:
        fodder.append([enemy.Serial, Player.DistanceTo(enemy)])

    #sorts list according to distance
    fodder.sort(key=lambda x: x[1])

    enemy = fodder[0][0]
    Misc.Pause(200)

    return enemy

