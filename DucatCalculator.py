#!/usr/bin/env python3
import download
import parser.ducats
import calculator.ducats
import parser.mission
import calculator.missions
import output.docx


def main():
    MissionDecks = download.GetMissionDecks()
    RelicData = parser.ducats.GetRelicData(MissionDecks)
    DucatData = calculator.ducats.DucatList(RelicData)
    MissionList = parser.mission.GetRelicMissonData(MissionDecks)
    MissionDucats = calculator.missions.CalculateDucatDrops(MissionList, DucatData)
    output.docx.WriteXLSX(DucatData, MissionDucats)


if __name__ == '__main__':
    main()
