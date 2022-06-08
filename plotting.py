import asynchat
from motion_detection import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

# df["Start_str"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
# df["End_str"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["Start_str"] = df["Start"].astype(str)
df["End_str"] = df["End"].astype(str)

cds = ColumnDataSource(df)

# instead of responsive = True use sizing_mode='scale_width'
p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_width', title="Motion Graph")

p.yaxis.minor_tick_line_color = None
#p.ygrid[0].ticker.desired_num_ticks = 1 


hover = HoverTool(tooltips=[("Start","@Start_str"), ("End", "@End_str")])

p.add_tools(hover)

# q = p.quad(left=df['Start'], right=df['End'], top=1, bottom=0, color='green')
q = p.quad(left='Start', right='End', top=1, bottom=0, color='green', source=cds)

output_file('graph.html')

show(p)

