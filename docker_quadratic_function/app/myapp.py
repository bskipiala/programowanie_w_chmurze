import io
from flask import Flask, request, escape, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

app = Flask(__name__)

@app.route("/")
def plot_png():
    #name = request.args.get('name', 'World')
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    c = int(request.args.get('c'))
    xmin = int(request.args.get('xmin'))
    xmax = int(request.args.get('xmax'))
    ymin = int(request.args.get('ymin'))
    ymax = int(request.args.get('ymax'))
    
    x = np.linspace(xmin, xmax, 1000)
    y = a*x**2 + b*x + c
    
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_xlim([xmin, xmax])
    axis.set_ylim([ymin, ymax])
    axis.plot(x, y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')




