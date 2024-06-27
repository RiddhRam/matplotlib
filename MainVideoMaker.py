from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip

# Load videos
GraphClip = VideoFileClip("GraphRaw.mp4")
LegendClip = VideoFileClip("LegendRaw.mp4")
CounterClip = VideoFileClip("CounterRaw.mp4")

# Cropping
legendX1, legendY1 = 350, 320  # top-left corner - legend
legendX2, legendY2 = 950, 750  # bottom-right corner - legend
cropped_LegendClip = LegendClip.crop(x1=legendX1, y1=legendY1, x2=legendX2, y2=legendY2)

counterX1, counterY1 = 450, 400  # top-left corner - counter
counterX2, counterY2 = 850, 550  # bottom-right corner - counter
cropped_CounterClip = CounterClip.crop(x1=counterX1, y1=counterY1, x2=counterX2, y2=counterY2)

# Resizing
resized_GraphClip = GraphClip.resize(width=929)
resized_LegendClip = cropped_LegendClip.resize(width=250)
resized_CounterClip = cropped_CounterClip.resize(width=151)

# Calculate total width needed
totalWidth = resized_GraphClip.size[0] + resized_CounterClip.size[0]
totalHeight = int(totalWidth * (16/9))

print(str(totalWidth) + 'x' + str(totalHeight))

# #282c44 is same as (40, 44, 68)
# Solid dark blue background
solidColour = ColorClip(size=(totalWidth, totalHeight), color=(40, 44, 68), duration=resized_GraphClip.duration)

# Title
titleText = TextClip("2020 Tesla Model Y Price Predictions", font ="Arial-Bold", fontsize=40, color='white')
titleText = titleText.set_duration(resized_GraphClip.duration)

# Calculate the horizontal center position for the title text
titleWidth = titleText.size[0]
titleCenterXPosition = (totalWidth - titleWidth) // 2

# This blocks out the 'X' x-axis label from the graph clip so the actual x-axis label below can be seen
textBackgroundColor = ColorClip(size=(50, 20), color=(40, 44, 68), duration=resized_GraphClip.duration)

# X-Axis label
# Have to rewrite this one since for some reasons matplotlib didn't want to use the right label when creating the graph
xAxisText = TextClip("Year", font ="Arial-Bold", fontsize=15, color='white')
xAxisText = xAxisText.set_duration(resized_GraphClip.duration)

# Create a larger composite frame
compositeClip = CompositeVideoClip([
    solidColour.set_position((0, 0)),
    resized_GraphClip.set_position((0, 600)), # Graph on the left at (0, 600)
    titleText.set_position((titleCenterXPosition, 610)),
    textBackgroundColor.set_position((440, 1250)),
    xAxisText.set_position((460, 1260)),
    resized_LegendClip.set_position((resized_GraphClip.size[0] - 92, 800)), # Legend to the right of the graph, below counter
    resized_CounterClip.set_position((resized_GraphClip.size[0] - 45, 690))  # Counter to the right of the graph, above legend
], size=(totalWidth, totalHeight))  # Set composite size to match total width and graph's height

# The last frame will be held for 1 second to display text
lastFrame = compositeClip.duration - 1/60
lastFrameClip = compositeClip.to_ImageClip(t=lastFrame, duration=1)

# Have to write it then bring it back as a video or it won't work
lastFrameClip.write_videofile("LastFrame.mp4", codec="libx265", fps=60, bitrate="5000k", audio=False)

# Save the main video
compositeClip.write_videofile("MainVideo.mp4", codec="libx265", fps=60, bitrate="5000k", audio=False)