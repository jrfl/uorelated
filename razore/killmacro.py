import time
import sys
import math

if not Misc.CurrentScriptDirectory() in sys.path:
    sys.path.append(Misc.CurrentScriptDirectory())
    
#for x in sys.path:
#    Misc.SendMessage("Path: " + str(x), 4095)

import common as c

moduleName = "c"
for x in c.razorModules:
    x = str(x)
    exec(compile(moduleName + "." + x + " = " + x, "<retards>", "exec"))

    
enemy = Target.PromptTarget("Choose a mob")

if enemy != -1:
    #Target.WaitForTarget(10000, False)
    Player.InvokeVirtue("Honor")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(enemy)
    
    c.enemyOfOne()
    c.consecrateWep()
    Player.Attack(enemy)
    Player.ChatSay(4095, "all kill")
    Target.WaitForTarget(10000, False)
    Target.Last()
