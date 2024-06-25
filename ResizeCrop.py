from moviepy.editor import VideoFileClip

GraphClip = VideoFileClip("GraphRaw.mp4")
LegendClip = VideoFileClip("LegendRaw.mp4")
CounterClip = VideoFileClip("CounterRaw.mp4")

# Cropping
legendX1, legendY1 = 600, 200  # top-left corner - legend
legendX2, legendY2 = 1200, 450  # bottom-right corner - legend
cropped_LegendClip = LegendClip.crop(x1=legendX1, y1=legendY1, x2=legendX2, y2=legendY2)

counterX1, counterY1 = 450, 400  # top-left corner - counter
counterX2, counterY2 = 850, 550  # bottom-right corner - counter
cropped_CounterClip = CounterClip.crop(x1=counterX1, y1=counterY1, x2=counterX2, y2=counterY2)

# Resizing
resized_GraphClip = GraphClip.resize(width=929)
resized_LegendClip = cropped_LegendClip.resize(width=250)
resized_CounterClip = cropped_CounterClip.resize(width=151)

# Writing
#resized_GraphClip.write_videofile("Graph.mp4")

resized_LegendClip.write_videofile("Legend.mp4")

resized_CounterClip.write_videofile("Counter.mp4")