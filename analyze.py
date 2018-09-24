import numpy as np
import matplotlib.pyplot as plt
import os

#Extrac drag and t

def PlotDragVst(wd, iteration):
	# wd: working directory
	# Load the log1 file
	log_file = open(wd+"log1", "r")

	drag_t_array = []

	for line in log_file: 
		if 'drag' in line and 'step' not in line and 'mean' not in line: 
			#print(line)
			#print(line.split())
			#print(line.split()[1], line.split()[4])
			drag_t = [ float(line.split()[1]), float(line.split()[4]) ] #
			#print(drag_t)
			drag_t_array.append(drag_t)

		if 'mean drag' in line:
			#print(line.split())
			mean_drag_str = line.split()[2] #float()
			

	drag_t_array = sorted(drag_t_array, key=lambda el: el[1])

	drag_t_array = np.asarray(drag_t_array)

	#print(drag_t_array)

	plt.figure()
	plt.plot(drag_t_array[:,1],drag_t_array[:,0])
	plt.plot(drag_t_array[:,1],drag_t_array[:,0], '.')

	plt.title('Plot of drag force vs time, %s \n mean drag: %s' %(iteration, mean_drag_str))
	plt.grid(True)
	plt.xlabel('t')
	plt.ylabel('drag force')
	plt.grid(True)
	plt.show()

	return

if __name__ == "__main__":
	wd = ''
	iteration = 'iter_00/'
	wd = wd + iteration 
	PlotDragVst(wd, iteration)


