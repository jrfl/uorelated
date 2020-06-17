
Items.UseItem(0x4066E7F2)
Gumps.WaitForGump(1425364447, 10000)

#Gumps.SendAction(1425364447, 3)
go = True
f = open("bodlist.txt", "w")
while go:
    totalLines = Gumps.LastGumpGetLineList()
    jlines = "; ".join(totalLines)
    for line in totalLines:
        if line:
            f.write(line + "\n")
    if jlines.find("Next page") == -1:
        go = False
    else:
        Gumps.SendAction(1425364447, 3)
        Gumps.WaitForGump(1425364447, 10000)

f.close()

