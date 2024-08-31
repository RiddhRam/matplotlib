#!/bin/bash

# Make white background
ffmpeg -f lavfi -y -i color=c='D3D3D3':s=1080x1920:d=8.3334 -t 8.3334 -r 60 whiteBackground.mp4

# Read the car name from the CSV file
car3=$(awk -F, 'NR==1 {print $1}' car3.csv)
# Read the car color 
carColor=$(awk -F, 'NR==1 {print $1}' car3Color.csv)

endingYear=$(awk -F, 'NR==1 {print $1}' endingYear.txt)

finalPrice=$(awk -F, 'NR==1 {print $1}' car3FinalPrice.txt)

# We use #D5D5D5 for the background here because the compression/codec affects the color, and #D5D5D5 becomes #D3D3D3, but #D3D3D3 becomes #D0D0D0
# Make Car Name Title Video
ffmpeg -f lavfi -y -i color=c='D5D5D5':s=1080x100:d=8.3334 -vf "drawtext=text='$car3':fontcolor=$carColor:fontsize=48:x=(w-text_w)/2:y=0" -frames:v 1 TextVideoName.png

# Make Last Part Of Title 
ffmpeg -f lavfi -y -i color=c='D5D5D5':s=1080x40:d=8.3334 -vf "drawtext=text='Price Predictions':fontcolor=$carColor:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2" -frames:v 1 TextVideoEnd.png

# Overlay the above 2 Images
ffmpeg -loop 1 -y -i TextVideoName.png -i TextVideoEnd.png -filter_complex "[0:v][1:v]overlay=0:60" -t 8.3334 -r 60 TextVideoTitle.mp4

# Scale GraphRaw.mp4 down to 1080x1680 then overlay it onto solidColour.mp4 at 0x210, then overlay TextVideoTitle.mp4 onto that video at 0x370, then overlay CounterRaw.mp4 onto that video at 830x240
ffmpeg -y -i whiteBackground.mp4 -i GraphRaw.mp4 -i TextVideoTitle.mp4 -i CounterRaw.mp4 -filter_complex "[1:v]scale=1080:1680[graph];[0:v][graph]overlay=0:210[graphAndBG];[graphAndBG][2:v]overlay=0:435[graphBGandTitle];[graphBGandTitle][3:v]overlay=800:240" -r 60 MainVideo.mp4

# Get the last frame of the MainVideo.mp4
ffmpeg -sseof -3 -y -i MainVideo.mp4 -update 1 -q:v 1 LastFrame.png
# Display last average price and year and make an outline that matches the cars line color
ffmpeg -f lavfi -y -i color=c=white:s=590x170:d=8.3334 -vf "drawbox=x=0:y=0:w=590:h=170:color=$carColor:t=5,drawtext=text='Average Price in $endingYear\: \$$finalPrice':fontcolor=black:fontsize=35:x=(w-text_w)/2:y=10" -frames:v 1 LastFrameInfo.png

# Make the last part of the last frame text
ffmpeg -f lavfi -y -i color=c=white:s=549x40 -vf "drawtext=text='FOLLOW FOR MORE':fontcolor=black:fontsize=35:x=(w-text_w)/2:y=(h-text_h)/2" -frames:v 1 LastFrameEnd.png

# Overlay the above 2 images
ffmpeg -y -i LastFrameInfo.png -i LastFrameEnd.png -filter_complex "overlay=x=21:y=120" LastFrameText.png

# Overlay the above video onto LastFrame.mp4
ffmpeg -y -i LastFrame.png -i LastFrameText.png -filter_complex "overlay=x=260:y=980" LastFrameFinal.png

# Make the LastFrameFinal.png into a 1 second long video
ffmpeg -loop 1 -y -i LastFrameFinal.png -c:v libx264 -t 1 -pix_fmt yuv420p -r 60 LastFrameFinal.mp4

# Concatenate LastFrameFinal.mp4 to MainVideo.mp4
ffmpeg -y -f concat -i concatVideos.txt -c copy FinalVideoUntrimmed.mp4

# Trim the first 32 frames
ffmpeg -ss 0.53334 -y -i FinalVideoUntrimmed.mp4 -c:v libx264 FinalVideo.mp4