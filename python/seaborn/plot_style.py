# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Load data
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")
# Set axes style to white for first subplot
with sns.axes_style("white"):
    plt.subplot(211)
sns.swarmplot(x="species", y="petal_length", data=iris)
# Initialize second subplot
plt.subplot(212)
# Plot violinplot
sns.violinplot(x = "total_bill", data=tips)
# Show the plot
plt.show()