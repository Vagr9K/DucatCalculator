#!/usr/bin/env python3
import download
import parser.ducats
import calculator.ducats
import output


def main():
    MissionDecks = download.GetMissionDecks()
    RelicData = parser.ducats.GetRelicData(MissionDecks)
    DucatData = calculator.ducats.DucatList(RelicData)
    output.WriteOutput(DucatData)


if __name__ == '__main__':
    main()
