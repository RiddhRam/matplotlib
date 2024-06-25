from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip

# Load videos
graphClip = VideoFileClip("Graph.mp4")
legendClip = VideoFileClip("Legend.mp4")
counterClip = VideoFileClip("Counter.mp4")

# Calculate total width needed
total_width = graphClip.size[0] + counterClip.size[0] # Should be same as graphClip.size[0] + counterClip.size[0]
total_height = int(total_width * (16/9))

print(str(total_width) + 'x' + str(total_height))

# Solid white background
solid_color = ColorClip(size=(total_width, graphClip.size[1]), color=(255, 255, 255), duration=graphClip.duration)

# Title
txt = TextClip("2024 Sports Car Price Predictions", font ="Arial-Bold", fontsize=50, color='black')
txt = txt.set_duration(graphClip.duration)

# Create a larger composite frame
composite_clip = CompositeVideoClip([
    solid_color.set_position((0, 1000)),
    graphClip.set_position((0, 1000)), # Graph on the left at (0, 0)
    txt.set_position((220, 1025)),
    legendClip.set_position((graphClip.size[0] - 120, 1200)), # Legend to the right of the graph, below counter
    counterClip.set_position((graphClip.size[0] - 50, 1030))  # Counter to the right of the graph, above legend
], size=(total_width, total_height))  # Set composite size to match total width and graph's height

# Export the final composite
composite_clip.write_videofile("Final.mp4", codec='libx264')
