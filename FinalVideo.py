from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load Videos
lastFrameClip = VideoFileClip("LastFrameFinal.mp4")
mainClip = VideoFileClip("MainVideo.mp4")

finalClip = concatenate_videoclips([mainClip, lastFrameClip])
finalClip.write_videofile("Final.mp4", codec='libx265', bitrate="5000k", audio=False)