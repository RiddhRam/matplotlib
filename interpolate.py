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
frames = 500

# Not used here but still used in multiple files
car1 = '2024 Mercedes-AMG C63'
car2 = '2024 BMW M3'
car3 = '2024 Audi RS5'

# Data from the spreadsheet
x = np.linspace(startingYear, endingYear, 21)
y1 = np.array([89904.7484557957, 85150.8012066517, 71131.0556949064, 66083.7483432992, 60622.962684726, 53408.4884629658, 46856.1105027104, 46725.1153087014, 40301.343888725, 39526.7980265352, 32393.6875945769, 26333.8514646596, 25192.5482778282, 27528.6354291961, 24151.8968179318, 19291.947509473, 17470.7248285494, 17358.3580167504, 14602.0040270785, 13411.817284205, 12979.7814466904])
y2 = np.array([79715.4817292415, 70695.029540097, 69933.6617563746, 64418.1603345813, 55896.3932149316, 50430.690362201, 47358.6629068902, 38897.2096008501, 38972.9115187638, 31879.1392875884, 30895.5031097028, 25297.5342980258, 24138.9185707458, 21022.9053738104, 21623.8521199996, 19365.7859086583, 14105.8394856146, 16795.5266153385, 11880.7892101187, 13036.1887946071, 11936.9273319738])
y3 = np.array([84392.886968633, 79295.3491883744, 68014.8483147137, 61707.9621079849, 55576.8766081791, 50797.7329702725, 49083.2611658808, 41035.0112252737, 36124.3085738805, 37371.5117914243, 28687.9694667618, 26606.8013946526, 26039.3238987339, 25524.4262559698, 21720.962219624, 18079.9223762867, 17446.2438359879, 13254.3130151043, 14364.9930166511, 14096.851071715, 9286.68175477814])

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