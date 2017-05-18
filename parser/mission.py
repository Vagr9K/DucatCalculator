import re
import parser.ducats


def GetRelicDropSegments(missiondata):
    # Filter out void drops mentioning relics
    voiddroplines = parser.ducats.GetRelicLineNumbers(missiondata)
    start = voiddroplines[0]
    end = voiddroplines[-1] + 9
    del missiondata[start:end]

    # Filter out non-relic drops, rotation information
    rgFilter = re.compile(r'/Lotus/Types/Game/MissionDecks/([^\]]+)|RELIC| - ')
    filtereddata = []
    for line in missiondata:
        res = rgFilter.findall(line)
        if res:
            filtereddata.append(line)

    # Determine mission segments
    rgMission = re.compile(r'/Lotus/Types/Game/MissionDecks/([^\]]+)')
    rgRelic = re.compile(r'RELIC')
    missionlines = []
    for index, line in enumerate(filtereddata):
        res = rgMission.findall(line)
        if res:
            # Append to list the 'header'
            missionlines.append([index, res[0], False])
        else:
            # Check if the last mission drops relics
            res = rgRelic.findall(line)
            if res:
                missionlines[-1][2] = True

    # Generate list of lines to keep
    keeplist = []
    for index, line in enumerate(missionlines):
        if line[2]:
            startline = line[0]
            if (index + 1) != len(missionlines):
                endline = missionlines[index + 1][0] - 1
            else:
                endline = len(filtereddata)
            segment = (startline, endline)
            keeplist.append(segment)

    MissionList = []
    # Store data
    rgNode = re.compile(' - ')
    for segment in keeplist:
        segmentdata = filtereddata[segment[0] + 1:segment[1]]
        Nodes = []
        Relics = []
        for line in segmentdata:
            match = rgNode.findall(line)
            if match:
                Nodes.append(line)
            else:
                Relics.append(line)
        MissionList.append({
            'Nodes': Nodes,
            'Relics': Relics
        })

    return MissionList


def ExtractMissionData(missionlist):
    ExtractedData = []
    rgNode = re.compile(r'([^,]*)')
    rgRelicName = re.compile(r'\d(.+)RELIC')
    rgRelicChance = re.compile(r'([\d\.]+)%')
    for mission in missionlist:
        ExtractedMission = {'Nodes': [], 'Relics': []}

        # Extract nodes
        for node in mission['Nodes']:
            matchlist = []
            for match in rgNode.findall(node):
                if len(match):
                    matchlist.append(match.strip(' -'))
            newnode = {
                'Node': matchlist[0] + ', ' + matchlist[1],
                'Type': matchlist[2],
                'Faction': matchlist[3],
                'NT': matchlist[4]
            }
            ExtractedMission['Nodes'].append(newnode)

        # Extract relics
        for relic in mission['Relics']:
            newrelic = {
                'Name': rgRelicName.findall(relic)[0].strip(),
                'Chance': float(rgRelicChance.findall(relic)[0])
            }
            ExtractedMission['Relics'].append(newrelic)
        ExtractedData.append(ExtractedMission)

    return ExtractedData


def GetRelicMissonData(missiondata):
    mslist = GetRelicDropSegments(missiondata.split('\n'))
    return ExtractMissionData(mslist)


