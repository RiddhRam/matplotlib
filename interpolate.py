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

startingYear = 2017
endingYear = 2037
frames = 480

# Not used here but still used in multiple files
car1 = '2023 Honda Civic'
car2 = '2023 Toyota Camry'
car3 = '2017 Mercedes-AMG C43'

car1Model = 'Civic'
car2Model = 'Camry'
car3Model = 'C43'

savedColors = [
    '#4ca0d7',  # SpecGauge
    '#FE53BB',  # Neon Pink
    '#F5D300',  # Neon Yellow
    '#39FF14', # Neon Green
    '#FFA500', # Neon Orange
    '#B10DC9' # Neon Purple
]

backgroundColor = '#282c44'

carColor1 = '#282c44'
carColor2 = '#282c44'
carColor3 = '#F5D300'

# Data from the spreadsheet
x = np.linspace(startingYear, endingYear, 21)
y1 = np.array([56973.3014024333, 56654.0937876823, 57881.2452594375, 52524.1969847169, 54036.8293883537, 50099.5206906008, 50215.5301243299, 46041.3943538368, 46828.7569460318, 45775.9763466495, 40838.7099152755, 39320.663180075, 39708.4707605066, 39154.8373345083, 44604.9533240305, 40269.7018855158, 35418.1557835016, 33223.2617642196, 38397.2183748647, 38923.1195484233, 34756.6009868669])
y2 = np.array([56973.3014024333, 56654.0937876823, 57881.2452594375, 52524.1969847169, 54036.8293883537, 50099.5206906008, 50215.5301243299, 46041.3943538368, 46828.7569460318, 45775.9763466495, 40838.7099152755, 39320.663180075, 39708.4707605066, 39154.8373345083, 44604.9533240305, 40269.7018855158, 35418.1557835016, 33223.2617642196, 38397.2183748647, 38923.1195484233, 34756.6009868669])
y3 = np.array([56973.3014024333, 56654.0937876823, 57881.2452594375, 52524.1969847169, 54036.8293883537, 50099.5206906008, 50215.5301243299, 46041.3943538368, 46828.7569460318, 45775.9763466495, 40838.7099152755, 39320.663180075, 39708.4707605066, 39154.8373345083, 44604.9533240305, 40269.7018855158, 35418.1557835016, 33223.2617642196, 38397.2183748647, 38923.1195484233, 34756.6009868669])

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