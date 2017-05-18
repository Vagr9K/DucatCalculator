def CalculateDucatDrops(missionlist, ducatlist):
    CalculatedList = []
    for mission in missionlist:
        Ducats = {}
        for relic in mission['Relics']:
            rname = relic['Name']
            rchance = relic['Chance']
            for rtype in ['Intact', 'Exceptional', 'Flawless', 'Radiant']:
                LDucats = []
                for pcount in range(1, 5):
                    rducats = ducatlist[rtype][rname][pcount - 1]
                    LDucats.append(rchance / 100 * rducats)
                Ducats[rtype] = LDucats
        CalcMission = {
            'Nodes': mission['Nodes'],
            'Ducats': Ducats
        }
        CalculatedList.append(CalcMission)

    return CalculatedList
