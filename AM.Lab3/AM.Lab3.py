from scipy.integrate import odeint
from numpy import arange
import matplotlib.pyplot as plt

def system_for_non_stationary_mode(state, t):
	p0, p1, p2, p3 = state

	d_p0 = -8.63 * p0 + 2.2 * p1
	d_p1 = 8.63 * p0 - 10.83 * p1 + 4.4 * p2
	d_p2 = 8.63 * p1 - 13.03 * p2 + 4.4 * p3
	d_p3 = 8.63 * p2 - 4.4 * p3

	return [d_p0, d_p1, d_p2, d_p3]

def plot_probabilities_of_system_states(vectors, x):
	plt.figure()

	for i in range(len(vectors)):
		plt.plot(x, vectors[i], label = 'p' + str(i) + '(t)')

	plt.xlabel('Time')
	plt.ylabel('Probabilities')
	plt.title('Probabilities of system states')
	plt.legend()

def plot_coefficients(y, x, label):
	plt.plot(x, y, label = label)
	plt.xlabel('Time')
	plt.ylabel('Coefficients')
	plt.title('Load and idle factors machines in the shop')
	plt.legend()

def prepare_data_for_plot(state):
	vectors = []
	for i in range(len(state[0])):
		vectors.append([])

	for i in range(len(state)):
		for j in range(len(vectors)):
			vectors[j].append(state[i][j])

	return vectors

def calculate_load_factor(vectors):
	load_factor = []
	for i in range(len(vectors[0])):
		load_factor.append((vectors[1][i] + 2 * (vectors[2][i] + vectors[3][i])) / 2)
	return load_factor

def calculate_idle_rate(vectors):
	idle_rate = []
	for i in range(len(vectors[0])):
		idle_rate.append((vectors[1][i] + 2 * vectors[0][i]) / 2)
	return idle_rate

def main():
	t = arange(0, 2.5, 0.01)
	init_state = [1, 0, 0, 0]
	state = odeint(system_for_non_stationary_mode, init_state, t)

	vectors = prepare_data_for_plot(state)
	plt.style.use("bmh")	

	plot_probabilities_of_system_states(vectors, t)

	load_factor = calculate_load_factor(vectors)
	idle_rate = calculate_idle_rate(vectors)
	
	plt.figure()
	plot_coefficients(load_factor, t, "load factor")
	plot_coefficients(idle_rate, t, "idle rate")

	plt.show()

main()