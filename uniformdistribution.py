# Import necessary libraries
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import uniform
import seaborn as sns

# Set seaborn plotting style and figure size
sns.set(rc={'figure.figsize': (5, 5)})

# Define parameters for the uniform distribution
n = 10000  # Number of random samples
start = 10  # Lower bound of the uniform distribution
width = 20  # Width or range of the uniform distribution

# Generate random samples from the uniform distribution
data_uniform = uniform.rvs(size=n, loc=start, scale=width)

# Create a seaborn distribution plot
ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={
                      "linewidth": 15,
                      'alpha': 1
                  })

# Set labels for the x-axis and y-axis
ax.set(xlabel='Uniform Distribution', ylabel='Frequency')

# Display the plot
plt.show()

[Text(0, 0.5, u'Frequency'), Text(0.5, 0, u'Uniform Distribution ')]
