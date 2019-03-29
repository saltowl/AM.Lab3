from scipy.integrate import odeint
from numpy import arange

def system_for_non_stationary_mode(state, t):
	p0, p1, p2, p3 = state
	d_p0 = -8.63 * p0 + 2.2 * p1
	d_p1 = 8.63 * p0 - 10.83 * p1 + 4.4 * p2
	d_p2 = 8.63 * p1 - 13.03 * p2 + 4.4 * p3
	d_p3 = 8.63 * p2 - 4.4 * p3
	return [d_p0, d_p1, d_p2, d_p3]

def main():
	t = arange(0, 20, 0.1)
	init_state = [1, 0, 0, 0]
	state = odeint(system_for_non_stationary_mode, init_state, t)
	pass

main()