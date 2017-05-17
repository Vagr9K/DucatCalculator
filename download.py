import urllib.request


def GetMissionDecks():
    DMContentPath = 'https://raw.githubusercontent.com/VoiDGlitch/WarframeData/master/MissionDecks.txt'
    rs = urllib.request.urlopen(DMContentPath)
    text = rs.read().decode('utf-8')
    return text
