
import matplotlib.pyplot as plt

def plot_kmeans_clustering_results(c1, c2, c3, vq1, vq2, vq3):

    # Setting plot limits
    x1, x2 = -10, 10
    y1, y2 = -10, 10

    fig = plt.figure()
    fig.subplots_adjust(hspace=0.1, wspace=0.1)

    ax1 = fig.add_subplot(121, aspect='equal')
    ax1.scatter(c1[:, 0], c1[:, 1], lw=0.5, color='#00CC00')
    ax1.scatter(c2[:, 0], c2[:, 1], lw=0.5, color='#028E9B')
    ax1.scatter(c3[:, 0], c3[:, 1], lw=0.5, color='#FF7800')
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(False)
    ax1.set_xlim(x1, x2)
    ax1.set_ylim(y1, y2)
    ax1.text(-9, 8, 'Original')

    ax2 = fig.add_subplot(122, aspect='equal')
    ax2.scatter(vqc1[:, 0], vqc1[:, 1], lw=0.5, color='#00CC00')
    ax2.scatter(vqc2[:, 0], vqc2[:, 1], lw=0.5, color='#028E9B')
    ax2.scatter(vqc3[:, 0], vqc3[:, 1], lw=0.5, color='#FF7800')
    ax2.xaxis.set_visible(False)
    ax2.yaxis.set_visible(False)
    ax2.set_xlim(x1, x2)
    ax2.set_ylim(y1, y2)
    ax2.text(-9, 8, 'VQ identified')

    return fig