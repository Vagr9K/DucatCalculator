import re


def GetRelicLineNumbers(missiondata):
    # Determine line numbers between segments
    relicLineNumbers = []
    relicTest = re.compile(r'\[(.+VoidKeyMissionRewards.+)\]')
    for index, line in enumerate(missiondata):
        if relicTest.findall(line):
            relicLineNumbers.append(index)
    return relicLineNumbers


def GetRelicSegments(missiondata):
    RelicSegments = []
    relicLineNumbers = GetRelicLineNumbers(missiondata)
    # Parse relic names and their item strings
    for index, linenum in enumerate(relicLineNumbers):
        relicName = missiondata[linenum + 1]
        relicName = (re.sub(r'(-|RELIC)', '', relicName)).strip()
        relicLines = []
        if (index + 1) == len(relicLineNumbers):
            # Special case for the last relic
            endline = linenum + 10
        else:
            endline = relicLineNumbers[index + 1] - 2
        # Loop threw items
        for itemlinenum in range(linenum + 4, endline):
            relicLines.append(missiondata[itemlinenum])
        segment = {'RelicName': relicName, 'RelicLines': relicLines}
        RelicSegments.append(segment)
    return RelicSegments


def GetDropData(dropstring):
    try:
        # Parse data
        ItemName = re.findall(r'\d ([^,]*)', dropstring)[0]
        ItemRarity = re.findall(r',([^,]*),', dropstring)[0]
        IntactChance = re.findall(r'I:(\d+\.*\d*)%', dropstring)[0]
        ExceptionalChance = re.findall(r'E:(\d+\.*\d*)%', dropstring)[0]
        FlawlessChance = re.findall(r'F:(\d+\.*\d*)%', dropstring)[0]
        RadiantChance = re.findall(r'R:(\d+\.*\d*)%', dropstring)[0]
        Ducats = re.findall(r'(\d+) Ducats', dropstring)
        if not Ducats:
            Ducats = 0
        else:
            Ducats = Ducats[0]
        return {
            'ItemName': ItemName,
            'ItemRarity': ItemRarity.strip(),
            'Intact': float(IntactChance),
            'Exceptional': float(ExceptionalChance),
            'Flawless': float(FlawlessChance),
            'Radiant': float(RadiantChance),
            'Ducats': float(Ducats)
        }
    except IndexError:
        # If the file format changes, don't instantly fail
        print('WARNING: Failed to parse ITEM: {}'.format(dropstring))
        return None


def ExtractRelicData(relicsegments):
    RelicData = []
    for relic in relicsegments:
        Items = []
        relicname = relic['RelicName']
        for dropstring in relic['RelicLines']:
            Drop = GetDropData(dropstring)
            if Drop:
                Items.append(Drop)
        Data = {'RelicName': relicname, 'Items': Items}
        RelicData.append(Data)
    return RelicData


def GetRelicData(missiondecks):
    # Separate Relic segments from main file
    RelicSegments = GetRelicSegments(missiondecks.split('\n'))
    # Return parsed Relic data
    return ExtractRelicData(RelicSegments)
