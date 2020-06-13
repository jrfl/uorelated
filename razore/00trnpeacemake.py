from System.Collections.Generic import List
from System import Byte
from itertools import chain
import sys

if not Misc.CurrentScriptDirectory() in sys.path:
    sys.path.append(Misc.CurrentScriptDirectory())

import pandoraconstants as pc

"""
"What instrument shall you play?"
"You play poorly, and there is no effect."
"You attempt to disrupt your target, but fail."
"You play jarring music, suppressing your target's strength."
"""

"""
"You have hidden yourself well"
"You fail to hide"
"
"""

def findInstrument():
    for itm in Player.Backpack.Contains:
        if itm.ItemID in pc.instruments:
            Misc.Pause(1000)
            Misc.SendMessage("Found Instrument: " + str(hex(itm.Serial)), 4095)
            return itm.Serial
    return 0

def peacemake(target):
    rv = False
    Player.UseSkill("Peacemaking")
    Misc.Pause(250)
    
    if Journal.Search("What instrument shall you play"):
        Journal.Clear()
        Player.HeadMessage(4095, "Gimme an instrument")
        ins = findInstrument() # dirty
        if ins > 0:
            Items.WaitForContents(ins, 2000)
            Target.TargetExecute(ins)
        return False
        
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(target)
    Misc.Pause(1000)
    
    if Journal.Search("You play poorly, and"):
        rv = False
    
    elif Journal.Search("You attempt to calm your target"):
        rv = False

    elif Journal.Search("You play hypnotic music"):
        rv = True

    else:
        rv = False

    Journal.Clear()
    Misc.Pause(1000)
    return rv


def hide():
    Journal.Clear()
    Misc.Pause(250)
    Player.UseSkill("Hiding")
    Misc.Pause(1000)


    if Journal.Search("You fail to hide"):
        #Player.HeadMessage(4095, "Hide failed")
        return False
    
    elif Journal.Search("You have hidden yourself well"):
        #Player.HeadMessage(4095, "Hide success")
        return True
    else:
        #Player.HeadMessage(4095, "Hide failed")
        return False


while not Player.IsGhost:
    for enemy in chain(pc.cowsnbulls, pc.bearsnbugs, pc.hiryuncu, pc.dragons):
        while not peacemake(enemy):
            Misc.Pause(6000)

        Misc.Pause(11000)

    while hide() == False or Player.Visible:
        Misc.Pause(2000)
    Misc.Pause(16000)

