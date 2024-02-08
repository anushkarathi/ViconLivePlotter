import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from vicon import ViconSDK_Wrapper

class AMTI_BalanceBoardGUI:
    """
    This class creates a figure with two bar charts that scale with the force on AMTI plates 2 and 3. 
    The bars change color to try to promote symmetric loading on the two plates. 
    This is useful in sit/stand training for prostheses. 

    Kevin Best 2/8/2024.
    """
    def __init__(self, vicon_IP = 'ROB-ROUSE-VICON.adsroot.itcs.umich.edu'):
        self.viconServer = ViconSDK_Wrapper(vicon_IP=vicon_IP)

        self.fig, self.ax = plt.subplots()
        plates = ['Left','Right']
        update = lambda frame : self.update_plot()
        self.bars = self.ax.bar((0,1), (20,20))
        self.ax.set_ylim(0, 10)
        self.ax.set_xticks((0, 1))
        self.ax.set_xticklabels(plates)
        self.ax.set_ylabel('Force (N)')

        self.animation = FuncAnimation(self.fig, update, interval=100, cache_frame_data=False)
        plt.show()

    def update_plot(self):
        """
        This method gets called by the animation to update the plot at a fixed rate.
        """
        AMTI_vals = self.viconServer.get_latest_device_values(["AMTI2","AMTI3"], ["Force"], ["Fz"])
        if max(AMTI_vals) > self.ax.get_ylim()[1]:
            self.ax.set_ylim(0, max(AMTI_vals))

        for bar, height in zip(self.bars, AMTI_vals):
            bar.set_height(height)
        return self.bars


if __name__=='__main__':
    balancePlot = AMTI_BalanceBoardGUI()