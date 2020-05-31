toolbag = 0x41C5ECAD
miningRunebook = 0x407f8132
mining_smelt_runebookid = 7
mining_bank_runebookid = 13
mspot1_runebookid = 19
mspot2_runebookid = 25
mspot3_runebookid = 31
mspot4_runebookid = 37
mspot5_runebookid = 43
mspot6_runebookid = 49
mspot7_runebookid = 55
mspot8_runebookid = 61
mspot9_runebookid = 67

miningSpots = [
    (981, 3264, "Right", mspot1_runebookid, "Minespot 1"),    # 1
    (980, 3271, "West", mspot2_runebookid, "Minespot 2"),     # 2
    (981, 3279, "West", mspot3_runebookid, "Minespot 3"),     # 3
    (979, 3289, "West", mspot4_runebookid, "Minespot 4"),     # 4
    (974, 3293, "Up", mspot5_runebookid, "Minespot 5"),       # 5
    (969, 3302, "West", mspot6_runebookid), "Minespot 6",     # 6
    (978, 3313, "South", mspot7_runebookid), "Minespot 7",    # 7
    (972, 3323, "North", mspot8_runebookid), "Minespot 8",    # 8
    (962, 3307, "North", mspot9_runebookid), "Minespot 9"     # 9
]

minePos = -1
minePosMax = len(miningSpots)


def nextMinePos():
    global minePos
    minePos += 1
    if minePos not in range(0, minePosMax):
        minePos = 0
    return getInfo()


def curMinePos():
    return getInfo()


def getCurMiningPosition():
    return getInfo(minePos)[0:2]

def getInfo(info=-1):
    if info not in range(0, minePosMax):
        info = minePos
    return miningSpots[info]
