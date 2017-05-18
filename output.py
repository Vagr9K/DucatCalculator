import xlsxwriter


def ReformatData(ducatdata, relictype, sortkey):
    Data = []
    rdata = ducatdata[relictype]
    # Reformat into lists
    for relicname in rdata:
        relic = [relicname]
        sum = 0
        for ducats in rdata[relicname]:
            ducats = int(round(ducats))
            sum += ducats
            relic.append(ducats)
        avg = sum / 4
        # Add average
        relic.append(avg)
        Data.append(relic)
    # Sort in descending order based on ducat gain
    Data = sorted(Data, key=lambda x: x[sortkey], reverse=True)
    return Data


def CreateXLSX(DucatTable, filepath):
    workbook = xlsxwriter.Workbook(filepath)
    # Add a worksheet for each relic type
    for RelicType in DucatTable:
        worksheet = workbook.add_worksheet(RelicType)
        # Set header
        bold = workbook.add_format({'bold': 1})
        worksheet.set_column(0, 4, 10)
        worksheet.write("A1", "Relic", bold)
        worksheet.write("B1", "Solo", bold)
        worksheet.write("C1", "2 players", bold)
        worksheet.write("D1", "3 players", bold)
        worksheet.write("E1", "4 players", bold)
        worksheet.write("F1", "Average", bold)
        row = 1
        # Write data
        for relic in DucatTable[RelicType]:
            worksheet.write(row, 0, relic[0])
            worksheet.write(row, 1, relic[1])
            worksheet.write(row, 2, relic[2])
            worksheet.write(row, 3, relic[3])
            worksheet.write(row, 4, relic[4])
            worksheet.write(row, 5, relic[5])
            row += 1
    workbook.close()


def WriteOutput(ducatdata, outpath='Ducats.xlsx'):
    DucatTable = {}
    # Generate reformatted data for all relic types
    for relictype in ducatdata:
        DucatTable[relictype] = ReformatData(ducatdata, relictype, 4)
    # Write document
    CreateXLSX(DucatTable, outpath)


