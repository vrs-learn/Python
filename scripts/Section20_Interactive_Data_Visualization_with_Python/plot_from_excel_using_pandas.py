
import pandas

from bokeh.plotting import figure, output_file , show

df = pandas.read_excel("verlegenhuken.xlsx",sheetname="Ark1")

#print(df)

p = figure(plot_width=500,plot_height=400,tools="pan,resize",logo=None)

p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"

p.yaxis.minor_tick_line_color = None
p.xaxis.minor_tick_line_color = None

p.xaxis.axis_label="Temperature (degC)"
p.yaxis.axis_label="Pressure(hPa)"

df["Temperature"] = df["Temperature"]/10
df["Pressure"] = df["Pressure"]/10
#x_elements = a.append(for i in df("Temperature")

p.circle(df["Temperature"],df["Pressure"])

output_file("Weather.html")

show(p)
