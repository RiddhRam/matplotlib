#!/bin/bash

# Make white background
#ffmpeg -f lavfi -y -i color=c=white:s=1080x1920:d=8.3334 -t 8.3334 -r 60 whiteBackground.mp4

# Read the car name from the CSV file
car3=$(awk -F, 'NR==1 {print $1}' car3.csv)

# Read the car color 
carColor=$(awk -F, 'NR==1 {print $1}' car3Color.csv)

endingYear=$(awk -F, 'NR==1 {print $1}' endingYear.txt)

finalPrice=$(awk -F, 'NR==1 {print $1}' car3FinalPrice.txt)

# Make Car Name Title Video
ffmpeg -f lavfi -y -i color=c=white:s=1080x80:d=8.3334 -vf "drawtext=text='$car3':fontcolor=$carColor:fontsize=48:x=(w-text_w)/2:0" \-t 8.3334 -r 60 TextVideoName.mp4

# Make Last Part Of Title 
ffmpeg -f lavfi -y -i color=c=white:s=1080x40:d=8.3334 -vf "drawtext=text='Price Predictions':fontcolor=$carColor:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2" \-t 8.3334 -r 60 TextVideoEnd.mp4

# Overlay the above 2 videos
ffmpeg -y -i TextVideoName.mp4 -i TextVideoEnd.mp4 -filter_complex "[0:v][1:v]overlay=0:40" -r 60 FullTitle.mp4

# Scale GraphRaw.mp4 down to 1080x1680 then overlay it onto solidColour.mp4 at 0x210, then overlay FullTitle.mp4 onto that video at 0x370, then overlay CounterRaw.mp4 onto that video at 830x240
ffmpeg -y -i whiteBackground.mp4 -i GraphRaw.mp4 -i FullTitle.mp4 -i CounterRaw.mp4 -filter_complex "[1:v]scale=1080:1680[graph];[0:v][graph]overlay=0:210[graphAndBG];[graphAndBG][2:v]overlay=0:370[graphBGandTitle];[graphBGandTitle][3:v]overlay=830:240" -r 60 MainVideo.mp4

# Get the last frame of the MainVideo.mp4
ffmpeg -sseof -3 -y -i MainVideo.mp4 -update 1 -q:v 1 LastFrame.png

# Display last average price and year
ffmpeg -f lavfi -y -i color=c=white:s=560x160:d=8.3334 -vf "drawtext=text='Average Price in $endingYear\: \$$finalPrice':fontcolor=black:fontsize=35:x=(w-text_w)/2" -frames:v 1 LastFrameInfo.png

# Make the last part of the last frame text
ffmpeg -f lavfi -y -i color=c=white:s=560x40 -vf "drawtext=text='FOLLOW FOR MORE':fontcolor=black:fontsize=35:x=(w-text_w)/2:y=(h-text_h)/2" -frames:v 1 LastFrameEnd.png

# Overlay the above 2 videos
ffmpeg -y -i LastFrameInfo.png -i LastFrameEnd.png -filter_complex "overlay=x=0:y=120" LastFrameText.png

# Overlay the above video onto LastFrame.mp4
ffmpeg -y -i LastFrame.png -i LastFrameText.png -filter_complex "overlay=x=260:y=980" LastFrameFinal.png

# Make the LastFrameFinal.png into a 1 second long video
ffmpeg -loop 1 -y -i LastFrameFinal.png -c:v libx264 -t 1 -pix_fmt yuv420p -r 60 LastFrameFinal.mp4

# Concatenate LastFrameFinal.mp4 to MainVideo.mp4
ffmpeg -y -f concat -i concatVideos.txt -c copy FinalVideo.mp4