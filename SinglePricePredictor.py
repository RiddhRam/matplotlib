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

# Cropping and resizing
counterX1, counterY1 = 490, 420
counterX2, counterY2 = 830, 525
cropped_CounterClip = CounterClip.crop(x1=counterX1, y1=counterY1, x2=counterX2, y2=counterY2).resize(width=141)
resized_GraphClip = GraphClip.resize(width=1080)

# Solid color background
solidColour = ColorClip(size=(1080, 1920), color=(255, 255, 255), duration=resized_GraphClip.duration)

# Title
titleText = TextClip(carName + '\n Price Predictions', font="Arial-Bold", fontsize=43, color=carColor).set_duration(resized_GraphClip.duration)
titleWidth = titleText.size[0]
titleCenterXPosition = (1080 - titleWidth) // 2

# Create composite frame
compositeClip = CompositeVideoClip([
    solidColour.set_position((0, 0)),
    resized_GraphClip.set_position((20, 210)),
    titleText.set_position((titleCenterXPosition, 420)),
    cropped_CounterClip.set_position((865, 375))
], size=(1080, 1920))

# Render settings
output_file = "MainVideo.mp4"
last_frame_file = "LastFrame.mp4"

compositeClip.write_videofile(output_file, codec="libx264", fps=60, bitrate="4000k", audio=False)
compositeClip.to_ImageClip(t=compositeClip.duration - 0.02, duration=1).write_videofile(last_frame_file, codec="libx264", fps=24, bitrate="4000k", audio=False)
