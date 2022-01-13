import csv

rows = []

with open("cleaned_final.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
        
headers = row[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])

def convert_to_si(radius,mass): 
    for i in range(0,len(radius)-1): 
        radius[i] = radius[i]*6.957e+8 
        mass[i] = mass[i]*1.989e+30 
        convert_to_si(radius,mass)
        
temp_star_data = list(star_data_rows)

def gravity():
    star_masses = []
    star_radiuses = []
    star_name = []
    
    for star_data in temp_star_data:
        star_masses.append(star_data[3])
        star_radiuses.append(star_data[4])
        star_name.append(star_data[1])
        
    star_gravity = []
    
    for index, name in enumerate(star_name):
        gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000) * 6.674e-11
        star_gravity.append(gravity)
        
convert_to_si(star_data_rows[4],star_data_rows[3])
gravity()