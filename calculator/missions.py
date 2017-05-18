def CalculateDucatDrops(missionlist, ducatlist):
    CalculatedList = []
    for mission in missionlist:
        Ducats = {
            'Intact': [0, 0, 0, 0],
            'Exceptional': [0, 0, 0, 0],
            'Flawless': [0, 0, 0, 0],
            'Radiant': [0, 0, 0, 0]
        }
        for relic in mission['Relics']:
            rname = relic['Name']
            rchance = relic['Chance']
            for rtype in ['Intact', 'Exceptional', 'Flawless', 'Radiant']:
                for pcount in range(1, 5):
                    rducats = ducatlist[rtype][rname][pcount - 1]
                    Ducats[rtype][pcount - 1] += rchance * rducats / 100
        CalcMission = {
            'Nodes': mission['Nodes'],
            'Ducats': Ducats
        }
        CalculatedList.append(CalcMission)

    return CalculatedList
