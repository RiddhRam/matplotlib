import matplotlib.pyplot as plt
import matplotlib.animation as animation

startingYear = 2017
endingYear = 2037
frames = 500

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

plt.show()
