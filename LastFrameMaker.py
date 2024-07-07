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
totalWidth = 1080
totalHeight = 1920

# Ending text
# Ending prices text
pricesText = TextClip(car1Model + ": $" + str(car1FinalPrice) + "\n" + car2Model + ": $" + str(car2FinalPrice) + "\n" + car3Model + ": $" + str(car3FinalPrice)
                      , font ="Arial-Bold", fontsize=40, color='black')

if car1Color == '#282c44':
    pricesText = TextClip("Price in " + str(endingYear) + ": $" + str(car3FinalPrice), font ="Arial-Bold", fontsize=40, color='black')
    
pricesText = pricesText.set_duration(lastFrameClip.duration)

# Ending Follow Text
followText = TextClip("FOLLOW FOR MORE", font ="Arial-Bold", fontsize=35, color='black')
followText = followText.set_duration(lastFrameClip.duration)

# Calculate the horizontal center position for the texts
pricesWidth = pricesText.size[0]
pricesCenterXPosition = (totalWidth - pricesWidth) // 2

followWidth = followText.size[0]
followCenterXPosition = (totalWidth - followWidth) // 2

# Set the positions
lastFrameClip = lastFrameClip.set_position((0, 0))
pricesText = pricesText.set_position((pricesCenterXPosition - 100, 1125))
followText = followText.set_position((followCenterXPosition - 100, 1225))

lastFrameWithText = CompositeVideoClip([lastFrameClip, followText, pricesText], size=(totalWidth, totalHeight))
lastFrameWithText.write_videofile("LastFrameFinal.mp4", codec="libx265", fps=60, bitrate="6000k", audio=False)