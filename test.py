
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import kurtosis

# Load data from the .npy file
data = np.load('Distributions_unsorted\Binom_distr\Binomial_100000.npy')

# Visualize the binomial distribution using a histogram
plt.hist(data, bins=np.arange(min(data), max(data) + 1) - 0.5, density=True, alpha=0.7, label='Binomial Distribution')
plt.xlabel('Number of Successes')
plt.ylabel('Probability Density')
plt.title('Binomial Distribution Histogram')
plt.legend()
plt.show()


# Φορτώστε τα δεδομένα από το Npy αρχείο


# Υπολογισμός της κυρτότητας
kurtosis_value = kurtosis(data)

print(f"Η κυρτότητα των δεδομένων είναι: {kurtosis_value}")
