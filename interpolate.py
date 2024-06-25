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

startingYear = 2022
endingYear = 2042
frames = 500

# Not used here but still used in multiple files
car1 = '2022 Hyundai Ioniq 5'
car2 = '2022 Tesla Model 3'
car3 = '2022 Chevrolet Bolt'

# Data from the spreadsheet
x = np.linspace(startingYear, endingYear, 21)
y1 = np.array([51695.98330709779, 47574.18026880567, 50559.013776021806, 44074.20845666196, 41867.579835571334, 40479.32234036543, 38358.491355741, 36697.12851490923, 36197.06935225603, 38658.62575448269, 33532.1280395441, 31536.868207528583, 30497.44686027516, 31858.886008382455, 31854.98418046609, 27290.979464987737, 27769.343151785943, 23485.088987447645, 24879.57536084494, 27261.096551645453, 20778.8236691417])
y2 = np.array([54542.05974220787, 54361.50608089083, 48495.076881697794, 48067.99779979887, 45449.19829186816, 42613.8293753185, 44143.87063148435, 43477.3817641876, 43452.10536728388, 34830.92087748463, 36254.64977809161, 32541.600663307843, 31513.95418333627, 32108.429385614116, 33243.799528027295, 29445.001230621376, 29344.13032171271, 23904.151584054463, 27355.624737134298, 26096.854857214814, 21749.75199697566])
y3 = np.array([43535.2743487193, 39694.96099698011, 32991.201326210714, 32777.75702704248, 27092.881537977384, 26052.481996323106, 22804.054078444857, 21034.4209590,20497.420822278695, 16681.941324465475, 18847.437167732307, 13454.989332993691, 14216.11397477662, 11495.834101152424, 10495.634492227238, 11024.2424002 ,12024.648901093073, 7671.737478603442, 9593.794493279102, 6128.509283250209, 6789.480505974481])

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

# Write x_interp
write_csv_file('x_interp.csv', x_interp, 2)

# Write y1_interp
write_csv_file('y1_interp.csv', y1_interp, 2)

# Write y2_interp
write_csv_file('y2_interp.csv', y2_interp, 2)

# Write y3_interp
write_csv_file('y3_interp.csv', y3_interp, 2)