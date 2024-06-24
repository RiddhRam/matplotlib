import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter, MaxNLocator
import csv

def read_csv_file(file_path, string, items):
    if items == 1:
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)

            for row in reader:
                if not string:
                    return int(row[0])
                else:
                    return row[0]

    else:
        results = []
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)

            for row in reader:
                for item in row:
                    results.append(float(item))

        return results

maximumY = 95000

startingYear = read_csv_file('startingYear.csv', False, 1)
endingYear = read_csv_file('endingYear.csv', False, 1)
frames = read_csv_file('frames.csv', False, 1)

car1 = read_csv_file('car1.csv', True, 1)
car2 = read_csv_file('car2.csv', True, 1)
car3 = read_csv_file('car3.csv', True, 1)

# Original data points
x_interp = read_csv_file('x_interp.csv', False, 2)
y1_interp = read_csv_file('y1_interp.csv', False, 2)
y2_interp = read_csv_file('y2_interp.csv', False, 2)
y3_interp = read_csv_file('y3_interp.csv', False, 2)

fig, ax = plt.subplots()
line1, = ax.plot(x_interp, y1_interp, lw=2, label=car1, color='#4ca0d7')
line2, = ax.plot(x_interp, y2_interp, lw=2, label=car2, color='r')
line3, = ax.plot(x_interp, y3_interp, lw=2, label=car3, color='g')

# Set labels for the axes
ax.set_xlabel('Year')
ax.set_ylabel('Price')

# Format the y-axis labels to show the dollar sign
formatter = FuncFormatter(lambda x, _: f'${x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# Ensure x-axis shows only integers
ax.xaxis.set_major_locator(MaxNLocator(6, integer=True))

# Initialization function
def init():
    #ax.set_xlim(startingYear, startingYear+1)
    ax.set_ylim(0, maximumY)

    return line1, line2, line3

# Animation function
def animate(i):
    # Animate the next frame for the lines
    line1.set_data(x_interp[:i], y1_interp[:i])
    line2.set_data(x_interp[:i], y2_interp[:i])
    line3.set_data(x_interp[:i], y3_interp[:i])

    # Animate the next frame for the x axis
    if i >= 1:
        ax.set_xlim(startingYear, x_interp[i])

    return line1, line2, line3

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000/60)

plt.show()