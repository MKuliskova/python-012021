schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}

total = 0
count = 0
for item, value in schoolReport.items():
    total += value
    count += 1
    avg = total/count
print(avg)

for item, value in schoolReport.items():
    if value ==1:
        print(item)