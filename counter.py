import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
    
    current_year = startingYear + int(i/frames * (endingYear - startingYear)) + 1
    text.set_text(str(current_year))

    return text,

# Create a figure and axis
fig, ax = plt.subplots()

# Set up the plot with a white background and black text
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initialize the text element
text = ax.text(0.5, 0.5, startingYear, fontsize=50, ha='center', va='center', color='black')

# Create animation
ani = animation.FuncAnimation(fig, update_text, frames=frames, interval=1000/60, blit=True)

# Save the animation
ani.save('CounterRaw.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

plt.close()