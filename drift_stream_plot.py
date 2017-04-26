__author__ = 'Heitor Murilo Gomes'

import matplotlib.pyplot as plt
import types

def plotline(dataset_name,
              yvalues,
              loc_legend=3,
              figure_name=None,
              axis=[0, 1010, 40, 100],
              classifiers=['HoeffdingTree'],
              drifts=None,
              gradual_drift=None,
              xvalues=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
              xlabel='# instances (thousands)',
              ylabel='accuracy'):

    plt.title(dataset_name + ' - ' + ylabel)
    plt.axis(axis)

    line_style = ['-o', '-x', '-p', '-1', '-s', '-v', '-d']
    idx = 0
    stream_classifier = []
    for classifier in classifiers:
        plotted, = plt.plot(xvalues, yvalues[classifier], line_style[idx % len(line_style)], label=classifier)
        stream_classifier.append(plotted)
        idx+=1

    plt.axhline(y=0, xmax=1, color='black', ls='--')

    if drifts is not None:
        for drift in drifts:
            if gradual_drift is not None:
                if isinstance(gradual_drift, types.ListType) is False:
                    plt.axvline(x=drift-gradual_drift, ymax=1, color='r', ls='--')
                    plt.axvline(x=drift+gradual_drift, ymax=1, color='r', ls='--')
            plt.axvline(x=drift, ymax=1, color='r')

    if isinstance(gradual_drift, types.ListType):
        for i in range(0,len(gradual_drift)):
            if gradual_drift[i] > 0:
                plt.axvline(x=drifts[i]-gradual_drift[i], ymax=1, color='r', ls='--')
                plt.axvline(x=drifts[i]+gradual_drift[i], ymax=1, color='r', ls='--')

    plt.legend(stream_classifier, classifiers, loc=loc_legend, ncol=2, bbox_to_anchor=(0., 0, 1, 0))
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if figure_name is None:
        figure_name = 'plot.pdf'

    plt.savefig(figure_name)
    plt.clf()


if __name__ == "__main__":
    ex1abrupt_yvalues = {'HoeffdingTree': [84.2,87.1,87.9,85,85.5,83.5,86.6,87.6,86.7,85.7,87.3,86.9,86.4,88,85.7,86.2,87,87.1,89.1,85.4,86.7,87.9,90.5,87.4,88.6,86.8,87.9,89.2,88.8,87.4,88.2,88.9,88.7,88.6,89.5,87.5,87.8,88.3,89.1,88.9,89.6,89.1,89.3,88.5,87.9,87.7,89.5,88.4,89.2,88.7,81.7,84.7,82.8,85.7,84.1,84,83.3,85,84.9,83.7,86.6,84.9,84,84.3,83.8,84,85.9,85.1,85.3,84.5,83.9,87.4,88.3,86.5,86.1,86.9,87.5,88.6,87.2,87.3,88.3,87.6,88.5,87.1,89.1,86.8,88.9,87.2,88.1,88.4,88.4,88.1,88.7,88,87,86.8,88.5,87.8,88.4,88]}
    ex1abrupt_xvalues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

    plotline(dataset_name='SEA with 1 abrupt drift',
                yvalues=ex1abrupt_yvalues,
                axis=[0, 102, 30, 95],
                classifiers=['HoeffdingTree'],
                xvalues=ex1abrupt_xvalues,
                figure_name='SEA1abrupt.pdf',
                drifts=[50],
                gradual_drift=None,
                ylabel='accuracy',
                xlabel='#instances (thousands)')

    example4_yvalues = {'NaiveBayes': [82,87.1,87,88.4,86.6,88.5,88.2,89.6,89.7,85.7,89,86.5,88.3,89.8,87.9,87.4,86.7,87.3,82.3,84.3,83.7,80.6,77.9,73.7,66.2,63.8,60.4,52.7,53.2,47.1,45,44.8,42.9,43.3,43.6,41.5,42.5,44.3,44.7,43.7,46.5,44.5,45.4,45.8,48.4,46.2,50.7,49.4,50.3,51.4,70.7,71.5,71.8,73.1,72.6,72.9,73.2,73.8,74.1,75.7,74.9,73.8,77.2,75.8,77.7,77.4,75,76.6,73.6,75.7,73.9,73.8,72.6,69.1,65.5,62.2,61.4,56.1,57.7,56.4,54.1,54.4,53.3,53.2,55.1,53.2,55.5,55.3,52.9,55.9,57.5,57.8,58.1,56.7,57.6,57.4,56.8,58.6,59,59.7],
                    'LevBag':[78.1,85.2,88.4,92.2,92.5,91.9,94.1,93,92.8,92.9,93.8,92.7,94,94.2,93.6,93.2,91.7,92.4,89.1,86.4,87.5,85,82.2,74.7,63.2,56.7,59.9,55.5,54.7,58.1,61.1,59.8,63.5,60.5,64,63.8,64.7,64.7,63,66.9,63.1,63.9,63.3,66.4,61.9,62.8,64.5,63.2,61.6,63.1,70.8,83.2,86.2,91.1,89.8,89.8,92.5,90.8,90.8,91.2,91.5,91.3,92.4,92.2,92.3,91.2,90,90.3,89.1,85.8,86.6,83,81,76.5,66.2,58.3,59.1,55.3,59.1,62.2,63.9,66.8,68,64.1,71.4,70.5,68.4,70,69.6,71.7,69.9,69.9,71.2,70,69.7,69.4,71,71,73.8,72.4]}
    example4_xvalues = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,1000]

    plotline(dataset_name='SEA with 2 gradual drifts and 1 abrupt drift',
            yvalues=example4_yvalues,
            axis=[30, 1020, 20, 95],
            classifiers=['NaiveBayes', 'LevBag'],
            xvalues=example4_xvalues,
            # figure_name='SEA2gradual1abrupt.pdf',
            drifts=[250,500,750],
            gradual_drift=[100,0,100],
            ylabel='accuracy',
            xlabel='#instances (hundreds)')