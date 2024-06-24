import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.interpolate import interp1d
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MaxNLocator

startingYear = 2017
endingYear = 2037

# Original data points
x = np.linspace(startingYear, endingYear, 21)
y1 = np.array([106356.340740281, 96216.436980881, 95297.852725421, 92374.1510970049, 88268.5232595425, 83017.7827710256, 75374.815759741, 76083.1078751301, 69301.5126699472, 61243.1172528893, 56595.5134707797, 58029.4200778409, 44977.9211044186, 39613.4475143056, 36647.7168394631, 35714.7387208223, 33682.5473915311, 33212.4134402537, 28526.7121908407, 27580.4463148876, 25753.7624571823])
y2 = np.array([100907.785245006, 98539.1823254078, 87578.175373726, 82877.1086280486, 79264.2855978508, 65492.5881075766, 64240.0353463041, 65391.6758532198, 65606.2742375082, 61619.0509058298, 50070.2271044226, 47682.6519190801, 44186.8825728957, 40424.5550337697, 37346.7789116302, 37708.8065892751, 29646.8577327109, 23654.7990173267, 25249.3237650831, 26110.8970839078, 26100.612587362])
y3 = np.array([117622.31489817, 101433.12763235, 99254.2366680672, 86723.9961766089, 79669.4974722263, 71650.9671395041, 62602.3635322903, 58143.6725742433, 54350.5035425399, 46357.7659965975, 39511.8186882382, 39187.8895137844, 37306.8871437445, 36032.4305847661, 27562.681987161, 29658.0831343615, 22356.3901417007, 25857.8989166875, 21844.7967049427, 19990.9671137247, 18699.0674264666])

# Interpolation function
def interpolate_data(x, y, num_points):
    f = interp1d(x, y, kind='cubic')
    x_new = np.linspace(x.min(), x.max(), num_points)
    y_new = f(x_new)
    return x_new, y_new

# Interpolate the data to have more points
num_interpolated_points = 500
x_interp, y1_interp = interpolate_data(x, y1, num_interpolated_points)
_, y2_interp = interpolate_data(x, y2, num_interpolated_points)
_, y3_interp = interpolate_data(x, y3, num_interpolated_points)

fig, ax = plt.subplots()
line1, = ax.plot([], [], lw=2, label='2017 Merecedes-AMG E63S', color='#4ca0d7')
line2, = ax.plot([], [], lw=2, label='2017 BMW M5', color='r')
line3, = ax.plot([], [], lw=2, label='2017 Audi RS7', color='g')

ax.legend()

# Text annotations for each line
text1 = ax.text(startingYear, 0, '', fontsize=10, color='#000')
text2 = ax.text(startingYear, 0, '', fontsize=10, color='#000')
text3 = ax.text(startingYear, 0, '', fontsize=10, color='#000')

# Set labels for the axes
ax.set_xlabel('Year')
ax.set_ylabel('Price')

# Format the y-axis labels to show the dollar sign
formatter = FuncFormatter(lambda x, _: f'${x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# Ensure x-axis shows only integers
ax.xaxis.set_major_locator(plt.MaxNLocator(10, integer=True))

# Initialization function
def init():
    ax.set_xlim(startingYear, startingYear+1)
    ax.set_ylim(0, 125000)
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    '''text1.set_position((startingYear, 1000))
    text3.set_position((startingYear, 1000))
    text3.set_position((startingYear, 1000))'''
    #return line1, text1
    return line1, line2, line3
    return line1, line2, line3, text1, text2, text3

# Animation function
def animate(i):
    line1.set_data(x_interp[:i], y1_interp[:i])
    line2.set_data(x_interp[:i], y2_interp[:i])
    line3.set_data(x_interp[:i], y3_interp[:i])
    
    if i > 0:
        '''text1.set_position((min(x_interp[i-1], 2030), y1_interp[i-1]))
        text2.set_position((min(x_interp[i-1], 2033), y2_interp[i-1]))
        text3.set_position((min(x_interp[i-1], 2033), y3_interp[i-1]))'''
    if i < len(x_interp):
        '''text1.set_text('2017 Merecedes-AMG E63S')
        text2.set_text('2017 BMW M5')
        text3.set_text('2017 Audi RS7')'''

    if i >= 1:
        ax.set_xlim(startingYear, x_interp[i])

    '''if i >= 1:
        timeDifference= int(x_interp[i]) - (startingYear+6)

        distance = timeDifference

        years_to_display = np.arange(startingYear, endingYear+1, 2)
        ax.set_xticks(years_to_display)
        ax.figure.canvas.draw()'''
    

    #return line1, text1
    return line1, line2, line3
    return line1, line2, line3, text1, text2, text3

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_interpolated_points, interval=1000/60)

plt.show()
