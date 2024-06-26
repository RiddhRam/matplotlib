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

startingYear = 2023
endingYear = 2043
frames = 1000

# Not used here but still used in multiple files
car1 = '2023 Honda Civic'
car2 = '2023 Toyota Camry'
car3 = '2023 Nissan Altima'

car1Model = 'Civic'
car2Model = 'Camry'
car3Model = 'Altima'

savedColors = [
    '#4ca0d7',  # SpecGauge
    '#FE53BB',  # Neon Pink
    '#F5D300',  # Neon Yellow
    '#39FF14', # Neon Green
    '#FFA500', # Neon Orange
    '#B10DC9' # Neon Purple
]

carColor1 = '#FE53BB'
carColor2 = '#4ca0d7'
carColor3 = '#39FF14'

# Data from the spreadsheet
x = np.linspace(startingYear, endingYear, 21)
y1 = np.array([26503.9843813951, 25359.5629310573, 24297.933637698, 23796.566189364, 23844.7694038624, 22512.198023565, 20715.6889435745, 20784.1878044953, 20244.1186602053, 20960.6922917999, 18520.4573765486, 18367.5550251063, 16443.0673134262, 16654.4709180607, 14508.4485818386, 14772.1925210552, 14779.0247524565, 15129.6469616316, 15367.4065869368, 10810.0621728551, 13009.7455499745])
y2 = np.array([26658.583579468, 25462.264433237, 25396.7126429275, 24731.9792179487, 23061.3292864692, 21842.9066554199, 21018.4402053115, 20357.235762865, 19159.5195214647, 18872.0993372494, 19906.2091641096, 16212.5297145283, 17949.3983814795, 17887.6147862336, 15169.1360329179, 16567.3070164986, 14705.7613437986, 13418.0120272979, 12507.411111418, 14345.8737806548, 13128.1564301215])
y3 = np.array([26312.8292017247, 24603.7159281849, 24349.0321061038, 23929.9396942997, 23031.1442642186, 21931.8565515457, 21941.5638916822, 21539.8443355752, 19370.6756172271, 20710.1914190974, 16086.7110208032, 17057.8905909404, 18838.8909718848, 17542.5402081759, 17944.2242565336, 16044.2515719009, 14417.0049294523, 12477.8633054185, 15373.9212575361, 11266.3376071417, 10728.3299367821])

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