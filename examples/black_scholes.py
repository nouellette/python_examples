from scipy.stats import norm
import math

"""
Calculate the Black-Scholes option price for a call option.

Parameters:
S (float): current stock price
K (float): option strike price
T (float): time to maturity in years
r (float): risk-free interest rate
sigma (float): volatility of the stock

Returns:
float: Black-Scholes price of the call option
"""
def black_scholes_call(S, K, T, r, sigma):
    # Calculating d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Calculating the Black-Scholes formula
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price

# Example usage
S = 100  # current stock price
K = 100  # strike price
T = 1    # time to maturity (1 year)
r = 0.05 # risk-free interest rate (5%)
sigma = 0.2 # volatility of the stock (20%)

price = black_scholes_call(S, K, T, r, sigma)
print(price)