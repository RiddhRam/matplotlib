from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip
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
followText = TextClip("FOLLOW FOR MORE", font ="Arial-Bold", fontsize=40, color='white')
followText = followText.set_duration(lastFrameClip.duration)

# Ending prices text
pricesText = TextClip("Prices in " + str(endingYear) + "\n" + car1Model + ": $" + str(car1FinalPrice) + "\n" + car2Model + 
                      ": $" + str(car2FinalPrice) + "\n" + car3Model + ": $" + str(car3FinalPrice)
                      , font ="Arial-Bold", fontsize=40, color='white')
pricesText = pricesText.set_duration(lastFrameClip.duration)

# What prices do you predict?
questionText = TextClip("What prices do you predict?", font ="Arial-Bold", fontsize=40, color='white')
questionText = questionText.set_duration(lastFrameClip.duration)

# Calculate the horizontal center position for the texts
followWidth = followText.size[0]
followCenterXPosition = (totalWidth - followWidth) // 2

pricesWidth = pricesText.size[0]
pricesCenterXPosition = (totalWidth - pricesWidth) // 2

questionWidth = questionText.size[0]
questionCenterXPosition = (totalWidth - questionWidth) // 2

# Set the positions
lastFrameClip = lastFrameClip.set_position((0, 0))
followText = followText.set_position((followCenterXPosition, 1350))
pricesText = pricesText.set_position((pricesCenterXPosition, 150))
questionText = questionText.set_position((questionCenterXPosition, 400))

lastFrameWithText = CompositeVideoClip([lastFrameClip, followText, pricesText, questionText], size=(totalWidth, totalHeight))
lastFrameWithText.write_videofile("LastFrame.mp4", codec="libx264", fps=60)