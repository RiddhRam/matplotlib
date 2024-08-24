import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patheffects as path_effects
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

def readTxt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

startingYear = read_csv_file('startingYear.csv', False, 1)
endingYear = int(readTxt('endingYear.txt'))
frames = read_csv_file('frames.csv', False, 1)

# Function to update the text
def update_text(i):
    currentYear = startingYear + int(i/frames * (endingYear - startingYear)) + 1
    yearText.set_text(str(currentYear))

    return yearText,

# Create a figure and axis
fig, ax = plt.subplots()

# Hide the axis
ax.axis('off')

# Initialize the text element
yearText = ax.text(0.5, 0.5, startingYear, fontsize=30, ha='center', va='center', color='black')

# Calculate the size needed for the figure
bbox = yearText.get_window_extent(renderer=fig.canvas.get_renderer())
bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())

# Set the figure size
fig.set_size_inches(bbox_inches.width, bbox_inches.height)

# Adjust layout
plt.tight_layout(pad=0)

# Create animation
ani = animation.FuncAnimation(fig, update_text, frames=frames, interval=1000/60, blit=True)

# Save the animation
ani.save('CounterRaw.mp4', fps=60, extra_args=['-vcodec', 'libx264', '-b:v', '10M'])

#plt.show()
