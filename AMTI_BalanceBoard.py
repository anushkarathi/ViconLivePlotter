import matplotlib.pyplot as plt
import colorsys as colors
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
        init_total_force = 20
        self.bars = self.ax.bar((0,1), (init_total_force,init_total_force))
        self.ax.set_ylim(0, 10)
        self.ax.set_xticks((0, 1))
        self.ax.set_xticklabels(plates)
        self.ax.set_ylabel('Force (N)')

        # Draw a line showing symmetry
        self.symmline = self.ax.axhline(init_total_force/2, linestyle='--')

        self.animation = FuncAnimation(self.fig, update, interval=100, cache_frame_data=False)
        plt.show()

    def update_plot(self):
        """
        This method gets called by the animation to update the plot at a fixed rate.
        """
        AMTI_vals = [f*-1 for f in self.viconServer.get_latest_device_values(["AMTI2","AMTI3"], ["Force"], ["Fz"])]

        # Set color. DoA of 0 = green, DoA of 1 = red
        total_force = sum(AMTI_vals)
        if total_force > 10: 
            DoA = (AMTI_vals[1] - AMTI_vals[0])/total_force
            rgb_colors = colors.hsv_to_rgb((115 - 115*abs(DoA))/255, 90/100, 90/100)

            # Configure height of the graph to be the total force
            self.ax.set_ylim(0, total_force)

            # Update symmetry line height
            self.symmline.set_ydata((total_force/2, total_force/2))
            
            for bar, height in zip(self.bars, AMTI_vals):
                bar.set_height(height)
                bar.set_color(rgb_colors)
        return self.bars


if __name__=='__main__':
    balancePlot = AMTI_BalanceBoardGUI()