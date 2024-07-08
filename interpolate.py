import numpy as np
from scipy.interpolate import interp1d
import csv

def write_csv_file(path, data, items):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        if items == 1:
            writer.writerow([data])
        else:
            writer.writerows([data])

# Interpolation function
def interpolate_data(x, y, num_points):
    f = interp1d(x, y, kind='cubic')
    x_new = np.linspace(x.min(), x.max(), num_points)
    y_new = f(x_new)
    return x_new, y_new

startingYear = 2024
endingYear = 2044
frames = 360

# Not used here but still used in multiple files
car1 = ''
car2 = ''
car3 = ''

car1Model = 'Civic'
car2Model = 'Camry'
car3Model = 'Hilux9468903806'

car3Values = []

with open('table_data.csv', 'r', newline='') as f:
    reader = csv.reader(f)

    last_row = None
    for index, row in enumerate(reader):
        if index == 0:
            car3 = row[1]
        else:
            car3Values.append(float(row[1]))
            if index == 1:
                startingYear = int(row[0])
            
        last_row = row
    
    if last_row is not None:
        endingYear = int(last_row[0])

savedColors = [
    '#4ca0d7',  # SpecGauge
    '#ff00ff',  # Neon Pink
    '#ffff00',  # Neon Yellow
    '#00ff00', # Neon Green
    '#ff0000', # Neon red
    '#9900ff' # Neon Purple
]

backgroundColor = '#282c44'

carColor1 = '#282c44'
carColor2 = '#282c44'
carColor3 = '#4ca0d7'

# Data from the spreadsheet
x = np.linspace(startingYear, endingYear, 21)
y1 = np.array(car3Values)
y2 = np.array(car3Values)
y3 = np.array(car3Values)

# Interpolate the data
x_interp, y1_interp = interpolate_data(x, y1, frames)
_, y2_interp = interpolate_data(x, y2, frames)
_, y3_interp = interpolate_data(x, y3, frames)

# Write startingYear
write_csv_file('startingYear.csv', startingYear, 1)

# Write endingYear
write_csv_file('endingYear.csv', endingYear, 1)

# Write frames
write_csv_file('frames.csv', frames, 1)

# Write car1
write_csv_file('car1.csv', car1, 1)

# Write car2
write_csv_file('car2.csv', car2, 1)

# Write car3
write_csv_file('car3.csv', car3, 1)

# Write car1 color
write_csv_file('car1Color.csv', carColor1, 1)

# Write car2 color
write_csv_file('car2Color.csv', carColor2, 1)

# Write car3 color
write_csv_file('car3Color.csv', carColor3, 1)

# Write car1 model
write_csv_file('car1Model.csv', car1Model, 1)

# Write car2 model
write_csv_file('car2Model.csv', car2Model, 1)

# Write car3 model
write_csv_file('car3Model.csv', car3Model, 1)

# Write car1 final price
write_csv_file('car1FinalPrice.csv', y1[-1], 1)

# Write car2 final price
write_csv_file('car2FinalPrice.csv', y2[-1], 1)

# Write car3 final price
write_csv_file('car3FinalPrice.csv', y3[-1], 1)

# Write x_interp
write_csv_file('x_interp.csv', x_interp, 2)

# Write y1_interp
write_csv_file('y1_interp.csv', y1_interp, 2)

# Write y2_interp
write_csv_file('y2_interp.csv', y2_interp, 2)

# Write y3_interp
write_csv_file('y3_interp.csv', y3_interp, 2)