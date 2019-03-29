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

def plot_probabilities_of_system_states(y, x, i):
	plt.style.use("bmh")
	plt.plot(x, y, label = 'p' + str(i) + '(t)')
	plt.xlabel('Time')
	plt.ylabel('Probabilities')
	plt.title('Probabilities of system states')
	plt.legend()

def prepare_data_for_plot(state, t):
	vectors = []
	for i in range(len(state[0])):
		vectors.append([])

	for i in range(len(t)):
		for j in range(len(vectors)):
			vectors[j].append(state[i][j])

	for i in range(len(vectors)):
		plot_probabilities_of_system_states(vectors[i], t, i)

def main():
	t = arange(0, 2.5, 0.01)
	init_state = [1, 0, 0, 0]
	state = odeint(system_for_non_stationary_mode, init_state, t)

	prepare_data_for_plot(state, t)

	plt.show()

main()