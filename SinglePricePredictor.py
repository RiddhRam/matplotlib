from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip, ImageClip
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

carName = read_csv_file('car3.csv', True, 1)
carColor = read_csv_file('car3Color.csv', True, 1)
endingYear = read_csv_file('endingYear.csv', False, 1)

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

# Solid dark blue background
solidColour = ColorClip(size=(totalWidth, totalHeight), color=(255, 255, 255), duration=resized_GraphClip.duration)

# Title
titleText = TextClip("What will " + carName + '\n cost in ' + str(endingYear) + "?", font ="Arial-Bold", fontsize=50, color=carColor)
titleText = titleText.set_duration(resized_GraphClip.duration)

# Calculate the horizontal center position for the title text
titleWidth = titleText.size[0]
titleCenterXPosition = (totalWidth - titleWidth) // 2

# Logo Image
logoClip = ImageClip("SpecGauge Logo Text.png")
logoClip = logoClip.set_duration(resized_GraphClip.duration)
logoClip = logoClip.resize(width=400)
logoWidth = logoClip.size[0]
logoCenterXPoisition = (totalWidth - logoWidth) // 2

# Create a larger composite frame
compositeClip = CompositeVideoClip([
    solidColour.set_position((0, 0)), # Background
    resized_GraphClip.set_position((20, 190)), # Graph on the left
    titleText.set_position((titleCenterXPosition, 400)), # Title
    resized_CounterClip.set_position((805, 520)),  # Counter to the right of the graph
    logoClip.set_position((logoCenterXPoisition, 20)) # Logo
], size=(totalWidth, totalHeight))  # Set composite size to match total width and graph's height

# The last frame will be held for 0.5 second to display text
# Have to use 0.02s = 1/50 frames
# Not sure why video is in 50fps
lastFrame = compositeClip.duration - 0.02
lastFrameClip = compositeClip.to_ImageClip(t=lastFrame, duration=0.5)

# Have to write it then bring it back as a video or it won't work
lastFrameClip.write_videofile("LastFrame.mp4", codec="libx265", fps=60, bitrate="5000k", audio=False)

# Save the main video
compositeClip.write_videofile("MainVideo.mp4", codec="libx265", fps=60, bitrate="5000k", audio=False)