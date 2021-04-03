import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def plot_pgn():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def save_png():
    centipawns_fig = plt.figure(facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax_cp = centipawns_fig.add_axes((left, bottom, width, height), facecolor="lightgray")
    centipawns = np.linspace(-1000, 1000, 101)
    ax_cp.set_xticks([n for n in range(-1000, 1001, 200)])
    ax_cp.set_yticks([n for n in range(0, 101, 20)])
    ax_cp.spines['bottom'].set_position(('data', 0))
    ax_cp.spines['left'].set_position(('data', 0))
    wining_chances = 50 + 50 * (2 / (1 + np.exp(-0.004 * centipawns)) - 1)
    ax_cp.plot(centipawns, wining_chances, lw=1)
    ax_cp.grid(linestyle=':', linewidth=0.5, which="both")
    centipawns_fig.savefig('centipawns_fig.png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig