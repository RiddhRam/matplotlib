import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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

startingYear = read_csv_file('startingYear.csv', False, 1)
endingYear = read_csv_file('endingYear.csv', False, 1)
frames = read_csv_file('frames.csv', False, 1)

car1 = read_csv_file('car1.csv', True, 1)
car2 = read_csv_file('car2.csv', True, 1)
car3 = read_csv_file('car3.csv', True, 1)

car1Color = read_csv_file('car1Color.csv', True, 1)
car2Color = read_csv_file('car2Color.csv', True, 1)
car3Color = read_csv_file('car3Color.csv', True, 1)

# Original data points
x_interp = read_csv_file('x_interp.csv', False, 2)
y1_interp = read_csv_file('y1_interp.csv', False, 2)
y2_interp = read_csv_file('y2_interp.csv', False, 2)
y3_interp = read_csv_file('y3_interp.csv', False, 2)

# Initialize a figure and axis
fig, ax = plt.subplots()

#fig.patch.set_facecolor('#282c44')

# Function to update the plot
def update(i):
    # Clear previous plot
    ax.clear()  

    # Update the data for the new frame
    car1Val = y1_interp[i]
    car2Val = y2_interp[i]
    car3Val = y3_interp[i]
    
    values = [(car1, car1Val, car1Color), (car2, car2Val, car2Color), (car3, car3Val, car3Color)]

    sorted_values = sorted(values, key=lambda x: x[1], reverse=True)

    for index, val in enumerate(sorted_values):
        # Color box, it still needs text so it matches the length of the text
        ax.text(0.5, 0.6-0.2*index+0.004, val[0], color=val[2], ha='center', 
                fontsize=15, alpha=0, transform=ax.transAxes, 
                bbox=dict(facecolor=val[2], edgecolor=val[2], alpha=0.1, boxstyle='round,pad=0.1'))

        # Main text
        ax.text(0.5, 0.6-0.2*index, val[0], color=val[2], ha='center', fontsize=15,
                            transform=ax.transAxes)


    ax.axis('off')  # Turn off axis
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/60)

# Save the animation
ani.save("LegendRaw.mp4", fps=60, extra_args=['-vcodec', 'libx265', '-b:v', '10M'])

#plt.show()