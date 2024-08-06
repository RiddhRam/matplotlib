import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter, MaxNLocator
import pandas as pd
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


# Original data points
x_interp = read_csv_file('x_interp.csv', False, 2)
y3_interp = read_csv_file('y3_interp.csv', False, 2)
# Manual set maximumY
#maximumY = 33000

# Automatically set maximumY 1.5k above the highest price
maximumY = max(y3_interp) + 1800

startingYear = read_csv_file('startingYear.csv', False, 1)
endingYear = read_csv_file('endingYear.csv', False, 1)
frames = read_csv_file('frames.csv', False, 1)

car = read_csv_file('car3.csv', True, 1)

carImageName = read_csv_file('car3ImageName.csv', True, 1)

carColor = read_csv_file('car3Color.csv', True, 1)

#plt.style.use({"axes.facecolor": "#282c44"})
'''Available styles:
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 
'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 
'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 
'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']'''

fig, ax = plt.subplots()

# Size of the graph in inches
fig.set_size_inches(9, 14)

# Adjust tick labels color
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# Set the border color of the plot
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')

# Color for the line
colors = [
    carColor,  # Car 3
]

# Combine into a data frame and then we will plot it
df = pd.DataFrame({car: y3_interp, 'x':x_interp})

# Format the y-axis labels to show the dollar sign
formatter = FuncFormatter(lambda x, _: f'${x:,.0f}')

image = plt.imread('Logos/' + carImageName + '.png')

# Animation function
def animate(i):
    ax.clear()

    # Set data for the next frame for the lines
    df = pd.DataFrame({car: y3_interp[:i], 'x':x_interp[:i]})

    #ax.set_ylim(0, maximumY)

    # Redraw the plot with updated data
    lines = df.plot(x='x', y=[car], linewidth=9, ax=ax, legend=False, color=colors)

    # Hide by setting font size to 0 and colour to white
    # Hide these since they will be added in MainVideoMaker.py
    ax.set_xlabel('Year', color='white', fontsize=0)
    ax.set_ylabel('Price', color='white', fontsize=0)

    # Format the prices to have a $ at the start
    ax.yaxis.set_major_formatter(formatter)

    # Ensure x-axis shows only integers
    ax.xaxis.set_major_locator(MaxNLocator(6, integer=True))

    # Set the font size for the tick labels
    ax.tick_params(axis='both', which='major', labelsize=15)

    # Add the glow to the lines
    ''' n_lines = 10
    diff_linewidth = 0.5
    alpha_value = 0.03
    for n in range(1, n_lines):
        df.plot(
                x='x', 
                y=[car1, car2, car],
                linewidth=9+(diff_linewidth*n),
                alpha=alpha_value,
                legend=False,
                ax=ax,
                color=colors)'''

    # Text annotations for each line
    text = ax.text(startingYear, 0, car, fontsize=16, color='#000', fontweight='bold')

    if i > 0:
        text.set_position((x_interp[i-1], y3_interp[i-1] + 1000))

    return lines, text

# Margins from the right and top window edge
plt.subplots_adjust(right=0.68, top=0.8)
# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/60)

# Add the image to the top
fig.figimage(image, xo=fig.bbox.xmax/2 - image.shape[1]/2, yo=fig.bbox.ymax - image.shape[0], zorder=1)

# Save the animation
ani.save('GraphRaw.mp4', fps=60, extra_args=['-vcodec', 'libx265', '-b:v', '10M'])

#plt.show()