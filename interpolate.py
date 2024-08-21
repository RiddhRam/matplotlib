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

startingYear = 2024 # Place Holder
endingYear = 2044 # Place Holder
frames = 500

car1ImageName = ''
car2ImageName = ''
car3ImageName = 'VW'

# Not used here but still used in multiple files
car1 = '' # Place Holder
car2 = '' # Place Holder
car3 = '' # Place Holder

# Not needed for single price predictor since no legend is used
car1Model = 'Civic'
car2Model = 'Camry'
car3Model = 'Hilux'

car3Values = []

# Count the number of years to show
count = 0

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

            count += 1
            
        last_row = row
    
    if last_row is not None:
        endingYear = int(last_row[0])

savedColors = [
    '#4ca0d7',  # SpecGauge - GOOD
    '#FF10F0',  # Neon Pink - GOOD
    '#F8FF00',  # Neon Yellow
    '#39FF14', # Neon Green
    '#ff3131', # Neon red
    '#9900ff' # Neon Purple
]

backgroundColor = '#282c44'

carColor1 = '#282c44'
carColor2 = '#282c44'
carColor3 = '#39FF14'

# Data from the spreadsheet
x = np.linspace(startingYear, endingYear, count)
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

# Write car1ImageName
write_csv_file('car1ImageName.csv', car1ImageName, 1)

# Write car2ImageName
write_csv_file('car2ImageName.csv', car2ImageName, 1)

# Write car3ImageName
write_csv_file('car3ImageName.csv', car3ImageName, 1)

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