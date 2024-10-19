import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Monte Carlo Simulation for Black-Scholes Model
def monte_carlo_option_price(S, K, T, r, sigma, num_simulations=10000, num_steps=252, option_type='call'):
    # S: initial stock price
    # K: strike price
    # T: time to maturity (years)
    # r: risk-free rate
    # sigma: volatility
    # num_simulations: number of simulations to run
    # num_steps: number of time steps in each simulation
    # option_type: 'call' or 'put'

    # Generate random price paths
    dt = T / num_steps
    price_paths = np.zeros((num_simulations, num_steps))
    price_paths[:, 0] = S

    for t in range(1, num_steps):
        z = np.random.standard_normal(num_simulations)
        price_paths[:, t] = price_paths[:, t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

    # Calculate the payoff for each path
    if option_type == 'call':
        payoff = np.maximum(price_paths[:, -1] - K, 0)
    else:
        payoff = np.maximum(K - price_paths[:, -1], 0)

    # Discount the average payoff back to present value
    option_price = np.exp(-r * T) * np.mean(payoff)

    return option_price

# Example Parameters
S = 100    # underlying asset price
K = 100    # option strike price
T = 1      # time to maturity
r = 0.05   # risk-free interest rate
sigma = 0.2  # volatility
num_simulations = 10000  # number of Monte Carlo simulations

# Calculate call and put option prices using Monte Carlo
call_price = monte_carlo_option_price(S, K, T, r, sigma, num_simulations, option_type='call')
put_price = monte_carlo_option_price(S, K, T, r, sigma, num_simulations, option_type='put')

print(f"Monte Carlo Call Option Price: {call_price:.2f}")
print(f"Monte Carlo Put Option Price: {put_price:.2f}")

# Optimization Problem: Maximizing the Monte Carlo Call Option Price by changing the strike price
def optimize_strike_price_monte_carlo(S, T, r, sigma, num_simulations=10000):
    def objective_function(K):
        return -monte_carlo_option_price(S, K, T, r, sigma, num_simulations, option_type='call')  # Negative because we minimize by default

    result = minimize(objective_function, x0=S, bounds=[(1, 2 * S)])
    return result.x[0], -result.fun

optimal_K, optimal_call_price = optimize_strike_price_monte_carlo(S, T, r, sigma)

print(f"Optimal Strike Price for Call Option: {optimal_K:.2f}")
print(f"Optimal Call Option Price: {optimal_call_price:.2f}")

# Plotting the Monte Carlo Call Option Price as a Function of Strike Price
strike_prices = np.linspace(50, 150, 50)
call_prices = [monte_carlo_option_price(S, K, T, r, sigma, num_simulations, option_type='call') for K in strike_prices]

plt.figure(figsize=(10, 5))
plt.plot(strike_prices, call_prices, label='Call Option Price')
plt.axvline(optimal_K, color='r', linestyle='--', label=f'Optimal Strike Price: {optimal_K:.2f}')
plt.xlabel('Strike Price')
plt.ylabel('Call Option Price')
plt.title('Monte Carlo Call Option Price vs. Strike Price')
plt.legend()
plt.grid(True)
plt.show()