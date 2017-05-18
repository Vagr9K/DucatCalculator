def CalculateDucatDrops(missionlist, ducatlist, relictype, playercount):
    CalculatedList = []
    for mission in missionlist:
        ducats = 0
        for relic in mission['Relics']:
            rname = relic['Name']
            rchance = relic['Chance']
            rducats = ducatlist[relictype][rname][playercount - 1]
            ducats += rchance / 100 * rducats
        CalcMission = {
            'Nodes': mission['Nodes'],
            'Ducats': ducats
        }
        CalculatedList.append(CalcMission)

    return CalculatedList
