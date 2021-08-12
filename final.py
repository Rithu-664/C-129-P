import csv

brightStars = []
dwarfStars = []

with open("C:/Users/JAYASANKAR/Downloads/C-129/Project/bright_stars.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        brightStars.append(row)

with open("C:/Users/JAYASANKAR/Downloads/C-129/Project/dwarf_stars_sorted.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dwarfStars.append(row)

header1 = brightStars[0]
starsData1 = brightStars[1:]
header2 = dwarfStars[0]
starsData2 = dwarfStars[1:]
headers = header1 + header2
starsData = []
for index,data_row in enumerate(starsData1):
    starsData.append(starsData1[index] + starsData2[index])

with open("all_stars.csv","a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(starsData)
