def perfectSquare(giris, karelist = [], kontrollist = []):
    for kareler in range(1,giris):
        karelist.append(kareler**2)
   
    for g in range(1,giris + 1):
        x = giris/g
        if x in karelist:
            kontrollist.append(int(x))
        

    if(len(kontrollist) > 1):
        out = max(kontrollist)
    else:
        out = kontrollist[0]
    
    lastout = int(giris/out)

    return lastout

