import numpy as np
from numpy.random import choice
import multiprocessing as mp
from multiprocessing.pool import Pool


def AverageDucats(ducatlist, chancelist, playercount):
    TESTCOUNT = 5000
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
    RelicName = relic['RelicName']
    print('{} completed.'.format(RelicName))
    # Return a tuple with name and results
    return (RelicName, results)


def DucatList(relicdata):
    RelicTypes = ['Intact', 'Exceptional', 'Flawless', 'Radiant']
    Results = {}
    for RelicType in RelicTypes:
        Results[RelicType] = {}
        # Generate arguments for multiprocessing pool
        names = []
        args = []
        print('Calculating {} relic stats.'.format(RelicType.lower()))
        for relic in relicdata:
            names.append(relic['RelicName'])
            args.append([relic, RelicType])
        # Limit process count in poll to the number of CPUs
        p = Pool(mp.cpu_count())
        ret = p.starmap(DucatsPerRelic, args)
        p.close()
        p.join()
        # Transform into a dictionary for easier access
        for answer in ret:
            Results[RelicType][answer[0]] = answer[1]
    return Results
