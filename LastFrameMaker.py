from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, ColorClip
import csv

def read_csv_file(file_path, string, items):
    if items == 1:
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)

            for row in reader:
                if not string:
                    return int(round(float(row[0])))
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

endingYear = read_csv_file('endingYear.csv', False, 1)

car1Model = read_csv_file('car1Model.csv', True, 1)
car2Model = read_csv_file('car2Model.csv', True, 1)
car3Model = read_csv_file('car3Model.csv', True, 1)

car1Color = read_csv_file('car1Color.csv', True, 1)

car1FinalPrice = read_csv_file('car1FinalPrice.csv', False, 1)
car2FinalPrice = read_csv_file('car2FinalPrice.csv', False, 1)
car3FinalPrice = read_csv_file('car3FinalPrice.csv', False, 1)

# Load Videos
lastFrameClip = VideoFileClip("LastFrame.mp4")
graphClip = VideoFileClip("Graph.mp4")
counterClip = VideoFileClip("Counter.mp4")

# Calculate total width needed
totalWidth = graphClip.size[0] + counterClip.size[0]
totalHeight = int(totalWidth * (16/9))

# Ending text
# Follow Text
followText = TextClip("FOLLOW FOR MORE", font ="Arial-Bold", fontsize=35, color='white')
followText = followText.set_duration(lastFrameClip.duration)

# Ending prices text
pricesText = TextClip(car1Model + ": $" + str(car1FinalPrice) + "\n" + car2Model + ": $" + str(car2FinalPrice) + "\n" + car3Model + ": $" + str(car3FinalPrice)
                      , font ="Arial-Bold", fontsize=40, color='white')

if car1Color == '#282c44':
    pricesText = TextClip(car3Model + ": $" + str(car3FinalPrice), font ="Arial-Bold", fontsize=40, color='white')
    
pricesText = pricesText.set_duration(lastFrameClip.duration)

# What prices do you predict?
questionText = TextClip("What prices do you predict?", font ="Arial-Bold", fontsize=35, color='white')
questionText = questionText.set_duration(lastFrameClip.duration)

# Background for followText and questionText
# This blocks out the 'X' x-axis label from the graph clip so the actual x-axis label below can be seen
textBackgroundColor = ColorClip(size=(550, 200), color=(0, 0, 0), duration=lastFrameClip.duration)

# Calculate the horizontal center position for the texts
followWidth = followText.size[0]
followCenterXPosition = (totalWidth - followWidth) // 2

pricesWidth = pricesText.size[0]
pricesCenterXPosition = (totalWidth - pricesWidth) // 2

questionWidth = questionText.size[0]
questionCenterXPosition = (totalWidth - questionWidth) // 2

textBackgroundWidth = textBackgroundColor.size[0]
textBackgroundCenterXPosition = (totalWidth - textBackgroundWidth) // 2

# Set the positions
lastFrameClip = lastFrameClip.set_position((0, 0))
followText = followText.set_position((followCenterXPosition, 625))
pricesText = pricesText.set_position((pricesCenterXPosition, 60))
questionText = questionText.set_position((questionCenterXPosition, 525))
textBackgroundColor = textBackgroundColor.set_position((textBackgroundCenterXPosition, 500))

lastFrameWithText = CompositeVideoClip([lastFrameClip, textBackgroundColor, followText, pricesText, questionText], size=(totalWidth, totalHeight))
lastFrameWithText.write_videofile("LastFrameFinal.mp4", codec="libx265", fps=60, bitrate="6000k", audio=False)