import csv

data = []
with open('C:/Users/JAYASANKAR/Downloads/C-129/Project/dwarf_stars.csv','r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]
stars_data = data[1:]

stars_data.sort(key=lambda stars_data:stars_data[2])
with open("dwarf_stars_sorted.csv","a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(stars_data)
