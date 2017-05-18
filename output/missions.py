import xlsxwriter


def ReformatData(missiondata, relictype, sortkey=4):
    # NODE / TYPE / FACTION / DUCATS1-2-3-4
    NodeList = []
    for nodegroup in missiondata:
        for node in nodegroup['Nodes']:
            NewNode = [
                node['Node'],
                node['Type'],
                node['Faction'],
                int(round(nodegroup['Ducats'][relictype][0])),
                int(round(nodegroup['Ducats'][relictype][1])),
                int(round(nodegroup['Ducats'][relictype][2])),
                int(round(nodegroup['Ducats'][relictype][3]))
            ]
            NodeList.append(NewNode)
    # Sort by ducat gain
    NodeList = sorted(NodeList, key=lambda x: x[sortkey + 2], reverse=True)
    # Sort by mission type
    NodeList = sorted(NodeList, key=lambda x: x[1], reverse=True)
    return NodeList


def CreateXLSX(workbook, MissionTable):
    # Add a worksheet for each relic type
    for RelicType in MissionTable:
        worksheet = workbook.add_worksheet('Missions ({})'.format(RelicType))
        # Set header
        bold = workbook.add_format({'bold': 1})
        worksheet.set_column(0, 4, 15)
        worksheet.write("A1", "Node", bold)
        worksheet.write("B1", "Type", bold)
        worksheet.write("C1", "Faction", bold)
        worksheet.write("E1", "Solo", bold)
        worksheet.write("D1", "2 players", bold)
        worksheet.write("F1", "3 players", bold)
        worksheet.write("G1", "4 players", bold)
        row = 1
        # Write data
        for node in MissionTable[RelicType]:
            worksheet.write(row, 0, node[0])
            worksheet.write(row, 1, node[1])
            worksheet.write(row, 2, node[2])
            worksheet.write(row, 3, node[3])
            worksheet.write(row, 4, node[4])
            worksheet.write(row, 5, node[5])
            worksheet.write(row, 6, node[5])
            worksheet.write(row, 7, node[5])
            row += 1
    workbook.close()


def WriteOutput(workbook, missiondata):
    MissionTable = {}
    # Generate reformatted data for all relic types
    for rtype in ['Intact', 'Exceptional', 'Flawless', 'Radiant']:
        MissionTable[rtype] = ReformatData(missiondata, rtype, 4)
    # Write document
    CreateXLSX(workbook, MissionTable)


