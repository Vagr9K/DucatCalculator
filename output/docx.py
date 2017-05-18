from output import ducats
from output import missions
import xlsxwriter


def WriteXLSX(ducatdata, missiondata, filepath='DucatData.xlsx'):
    workbook = xlsxwriter.Workbook(filepath)
    ducats.WriteOutput(workbook, ducatdata)
    missions.WriteOutput(workbook, missiondata)
    workbook.close()
