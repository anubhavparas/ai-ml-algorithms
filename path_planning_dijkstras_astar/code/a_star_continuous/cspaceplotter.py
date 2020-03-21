import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


class CSpacePlotter:
    def __init__(self, c_space):
        self.c_space = c_space

    def plotMap(self, fig, ax):
        height = self.c_space.height
        width = self.c_space.width
        padding =  self.c_space.padding
        poly_pts = self.c_space.coord_poly
        rect_pts = self.c_space.coord_rect
        rhom_pts = self.c_space.coord_rhom
        circle = self.c_space.circle
        ellipse = self.c_space.ellipse
        
        #fig = plt.figure()
        fig.set_dpi(100)
        fig.set_size_inches(8.5,6)
        #ax = plt.axes(xlim=(0,width),ylim=(0,height))
        cir = plt.Circle((circle[1]),circle[0],fc=None)
        borders = plt.Rectangle((0,0),width,height,alpha=1,fill=None,ec='b',linewidth=padding)
        rect = plt.Polygon(rect_pts)
        rhom = plt.Polygon(rhom_pts)
        poly = plt.Polygon(poly_pts)
        ell= Ellipse((ellipse[1]),ellipse[0][0],ellipse[0][1],0)
        shapes = [cir,rect,rhom,poly,ell,borders]
        for shape in shapes:
            #plt.gca().add_patch(shape)
            ax.add_patch(shape)
        return fig