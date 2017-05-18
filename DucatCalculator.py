#!/usr/bin/env python3
import download
import parser.ducats
import calculator.ducats
import output.ducats


def main():
    MissionDecks = download.GetMissionDecks()
    RelicData = parser.ducats.GetRelicData(MissionDecks)
    DucatData = calculator.ducats.DucatList(RelicData)
    output.ducats.WriteOutput(DucatData)


if __name__ == '__main__':
    main()
