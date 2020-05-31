from System.Collections.Generic import List
from System import Byte
def Main():
    eNumber = 0
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 1
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    while not Player.IsGhost:
        enemies = Mobiles.ApplyFilter(fil)
        enemy = Mobiles.Select(enemies,'Nearest')
        eNumber = len(enemies)
        #for enemy in enemies:
        #    eNumber += 1
        if eNumber > 0:
            if not(Timer.Check("Divine")) and Player.Stam < (Player.StamMax * .80):
                if not Player.BuffsExist("Divine Fury"):
                    Spells.CastChivalry("Divine Fury")
                    Misc.Pause(10)
                    Timer.Create("Divine", 10000 )
            if not(Timer.Check("Consecrate")):
                Spells.CastChivalry("Consecrate Weapon")
                Misc.Pause(10)
                Timer.Create("Consecrate", 10000 )
            if not(Timer.Check("EOO")):
                if not Player.BuffsExist("Enemy Of One"):
                    Spells.CastChivalry("Enemy Of One")
                    Misc.Pause(10)
                    Timer.Create("EOO", 30000 )
            if not(Timer.Check("Bless")):
                if not Player.BuffsExist("Bless"):
                    Spells.CastMagery("Bless")
                    Target.WaitForTarget(2000)
                    Target.Self()
                    Misc.Pause(10)
                    Timer.Create("Bless", 2300 )
    
        if eNumber == 1:
            eNumber = 0
            if not Player.HasSpecial:
                Player.WeaponPrimarySA()
            Player.Attack(enemy)
        if eNumber == 2:
            eNumber = 0
            if not Player.SpellIsEnabled('Momentum Strike'):
                Spells.CastBushido('Momentum Strike')
            Player.Attack(enemy) 
        if eNumber > 2 :
            eNumber = 0
            if not Player.HasSpecial:
                Player.WeaponSecondarySA()
            Player.Attack(enemy)
        Misc.Pause(250)
Main()
