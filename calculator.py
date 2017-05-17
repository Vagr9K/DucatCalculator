import numpy as np
from numpy.random import choice


def AverageDucats(ducatlist, chancelist, playercount):
    TESTCOUNT = 10000
    Sum = 0
    # Renormalize chancelist
    chancelist = np.array(chancelist)
    chancelist /= chancelist.sum()
    # Brute force test
    for i in range(TESTCOUNT):
        sample = choice(ducatlist, playercount, p=chancelist)
        Sum += np.amax(sample)
    return Sum / TESTCOUNT


def DucatsPerRelic(relic, type):
    ducatlist = []
    chancelist = []
    results = []
    # Generate weight 'tables'
    for relicitem in relic['Items']:
        ducatlist.append(relicitem['Ducats'])
        chancelist.append(relicitem[type])
    # Calculate for 1/2/3/4 player groups
    for playercount in range(1, 5):
        avg = AverageDucats(ducatlist, chancelist, playercount)
        results.append(avg)
    return results


def DucatList(relicdata):
    RelicTypes = ['Intact', 'Flawless', 'Exceptional', 'Radiant']
    Results = {}
    for RelicType in RelicTypes:
        Results[RelicType] = {}
        print('Calculating {} relic stats.'.format(RelicType.lower()))
        for index, relic in enumerate(relicdata):
            print(str(index + 1) + '/' + str(len(relicdata)))
            relicname = relic['RelicName']
            Results[RelicType][relicname] = DucatsPerRelic(relic, RelicType)
    return Results
