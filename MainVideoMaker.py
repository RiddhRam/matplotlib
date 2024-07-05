from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip

# Load videos
GraphClip = VideoFileClip("GraphRaw.mp4")
CounterClip = VideoFileClip("CounterRaw.mp4")

# Cropping
counterX1, counterY1 = 450, 400  # top-left corner - counter
counterX2, counterY2 = 850, 550  # bottom-right corner - counter
cropped_CounterClip = CounterClip.crop(x1=counterX1, y1=counterY1, x2=counterX2, y2=counterY2)

# Resizing
resized_GraphClip = GraphClip.resize(width=1060)
resized_CounterClip = cropped_CounterClip.resize(width=181)

# Calculate total width needed
totalWidth = 1080
totalHeight = 1920

print(str(totalWidth) + 'x' + str(totalHeight))

# #282c44 is same as (40, 44, 68)

# When making the raw counter, graph and legend videos, the above colour was used
# Due to compression, the colour is changed to the one below

# #272B43 is same as (39, 43, 67)

# Solid dark blue background
solidColour = ColorClip(size=(totalWidth, totalHeight), color=(255, 255, 255), duration=resized_GraphClip.duration)

# Title
titleText = TextClip("2020 Tesla Model 3 Price Predictions", font ="Arial-Bold", fontsize=40, color='#4ca0d7')
titleText = titleText.set_duration(resized_GraphClip.duration)

# Calculate the horizontal center position for the title text
titleWidth = titleText.size[0]
titleCenterXPosition = (totalWidth - titleWidth) // 2

# X-Axis label
xAxisText = TextClip("Year", font ="Arial-Bold", fontsize=25, color='#4ca0d7')
xAxisText = xAxisText.set_duration(resized_GraphClip.duration)

# Calculate the horizontal center position for the x-axis text
xAxisWidth = xAxisText.size[0]
xAxisCenterXPosition = (totalWidth - xAxisWidth) // 2

# Y-Axis label
# Can't rotate 90 for some reason so rotate 89.9
yAxisText = TextClip("Price", font="Arial-Bold", fontsize=80, color='#4ca0d7')
yAxisText = yAxisText.rotate(89.9)
yAxisText = yAxisText.resize(height=65)  # Adjust the height as needed
yAxisText = yAxisText.set_duration(resized_GraphClip.duration)

# Create a larger composite frame
compositeClip = CompositeVideoClip([
    solidColour.set_position((0, 0)),
    resized_GraphClip.set_position((20, 180)), # Graph on the left
    titleText.set_position((titleCenterXPosition, 260)),
    xAxisText.set_position((xAxisCenterXPosition, 1725)),
    yAxisText.set_position((10, 900)),
    resized_CounterClip.set_position((835, 380))  # Counter to the right of the graph
], size=(totalWidth, totalHeight))  # Set composite size to match total width and graph's height

# The last frame will be held for 1 second to display text
lastFrame = compositeClip.duration - 1/60
lastFrameClip = compositeClip.to_ImageClip(t=lastFrame, duration=1)

# Have to write it then bring it back as a video or it won't work
lastFrameClip.write_videofile("LastFrame.mp4", codec="libx265", fps=60, bitrate="5000k", audio=False)

# Save the main video
compositeClip.write_videofile("MainVideo.mp4", codec="libx265", fps=60, bitrate="5000k", audio=False)