from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, concatenate_videoclips

# Load Videos
lastFrameClip = VideoFileClip("LastFrame.mp4")
mainClip = VideoFileClip("MainVideo.mp4")

finalClip = concatenate_videoclips([mainClip, lastFrameClip])
finalClip.write_videofile("Final.mp4", codec='libx264')