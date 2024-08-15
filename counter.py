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

startingYear = read_csv_file('startingYear.csv', False, 1)
endingYear = read_csv_file('endingYear.csv', False, 1)
frames = read_csv_file('frames.csv', False, 1)

# Function to update the text
def update_text(i):
    
    currentYear = startingYear + int(i/frames * (endingYear - startingYear)) + 1
    yearText.set_text(str(currentYear))

    return yearText,

# Create a figure and axis
fig, ax = plt.subplots()

# Set up the plot with a white background and black text
#fig.patch.set_facecolor('#282c44')
ax.axis('off')

# Initialize the text element
yearText = ax.text(0.5, 0.5, startingYear, fontsize=50, ha='center', va='center', color='black')

# Create animation
ani = animation.FuncAnimation(fig, update_text, frames=frames, interval=1000/60, blit=True)

# Add outline
'''
yearText.set_path_effects([
        #path_effects.Stroke(linewidth=3.5, foreground="#4ca0d7"),
        #path_effects.SimpleLineShadow(offset=(1, -1), linewidth=1.5, alpha=0.5),
        path_effects.Normal(),
        #path_effects.withStroke(linewidth=3, foreground='white'),
        #path_effects.SimplePatchShadow(offset=(1, -1), alpha=0.8)
    ])'''

# Save the animation
ani.save('CounterRaw.mp4', fps=60, extra_args=['-vcodec', 'libx265', '-b:v', '10M'])

#plt.show()