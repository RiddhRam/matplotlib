from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip

# Load videos
graphClip = VideoFileClip("Graph.mp4")
legendClip = VideoFileClip("Legend.mp4")
counterClip = VideoFileClip("Counter.mp4")

# Calculate total width needed
totalWidth = graphClip.size[0] + counterClip.size[0]
totalHeight = int(totalWidth * (16/9))

print(str(totalWidth) + 'x' + str(totalHeight))

# #282c44 is same as (40, 44, 68)
# Solid dark blue background
solidColour = ColorClip(size=(totalWidth, graphClip.size[1]), color=(40, 44, 68), duration=graphClip.duration)

# Title
titleText = TextClip("2023 Reliable Sedans Price Predictions", font ="Arial-Bold", fontsize=40, color='white')
titleText = titleText.set_duration(graphClip.duration)

# Calculate the horizontal center position for the title text
titleWidth = titleText.size[0]
titleCenterXPosition = (totalWidth - titleWidth) // 2

# This blocks out the 'X' x-axis label from the graph clip so the actual x-axis label below can be seen
textBackgroundColor = ColorClip(size=(50, 20), color=(40, 44, 68), duration=graphClip.duration)

# X-Axis label
# Have to rewrite this one since for some reasons matplotlib didn't want to use the right label when creating the graph
xAxisText = TextClip("Year", font ="Arial-Bold", fontsize=15, color='white')
xAxisText = xAxisText.set_duration(graphClip.duration)

# Create a larger composite frame
compositeClip = CompositeVideoClip([
    solidColour.set_position((0, 600)),
    graphClip.set_position((0, 600)), # Graph on the left at (0, 600)
    titleText.set_position((titleCenterXPosition, 610)),
    textBackgroundColor.set_position((440, 1250)),
    xAxisText.set_position((460, 1260)),
    legendClip.set_position((graphClip.size[0] - 92, 800)), # Legend to the right of the graph, below counter
    counterClip.set_position((graphClip.size[0] - 45, 690))  # Counter to the right of the graph, above legend
], size=(totalWidth, totalHeight))  # Set composite size to match total width and graph's height

# The last frame will be held for 1 second to display text
lastFrame = compositeClip.duration - 1/60
lastFrameClip = compositeClip.to_ImageClip(t=lastFrame, duration=1)

# Have to write it then bring it back as a video or it won't work
lastFrameClip.write_videofile("LastFrame.mp4", codec="libx264", fps=60)

# Save the main video
compositeClip.write_videofile("MainVideo.mp4", codec="libx264", fps=60)