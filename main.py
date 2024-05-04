import pandas as pd
#read csv
dfproj = pd.read_csv('Projects.csv')
print(dfproj.columns)
#Describe the characteristics of the dataset
# Get simple statistics for the 'Total Phase Actual Spending Amount' column
column_description = dfproj['Total Phase Actual Spending Amount'].describe()
# Set display format to remove scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x)
# Print the description
print (column_description)

import matplotlib.pyplot as plt
# Create box plot with matplotlib
plt.figure(figsize=(8, 6))  # Set the figure size
plt.boxplot(dfproj['Total Phase Actual Spending Amount'], vert=False)  # Create box plot
plt.title('Box Plot of Total Phase Actual Spending Amount')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.yticks([])  # Remove y-axis ticks
plt.grid(True)  # Show grid
plt.show()  # Display plot

import pandas as pd
#read csv
dfproj = pd.read_csv('Projects.csv')
#Describe the characteristics of the dataset
# Get simple statistics for the 'Total Phase Actual Spending Amount' column
column_description = dfproj['Total Phase Actual Spending Amount'].describe()
# Set display format to remove scientific notation
#pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Print the description
import matplotlib.pyplot as plt

# Create box plot with matplotlib
plt.figure(figsize=(8, 6))  # Set the figure size
plt.boxplot(dfproj['Total Phase Actual Spending Amount'], vert=False)  # Create box plot
plt.title('Box Plot of Total Phase Actual Spending Amount')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.yticks([])  # Remove y-axis ticks
plt.grid(True)  # Show grid
plt.show()  # Display plot

# Create histogram using pandas
plt.figure(figsize=(8, 6))  # Set the figure size
dfproj['Total Phase Actual Spending Amount'].plot(kind='hist', bins=30, edgecolor='black')  # Create histogram
plt.title('Histogram of Total Phase Actual Spending Amount')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Frequency')  # Set y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot

import pandas as pd
import matplotlib.pyplot as plt

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Calculate Q1, Q3, and IQR of spending from projects dataset
Q1 = dfproj['Total Phase Actual Spending Amount'].quantile(0.25)
Q3 = dfproj['Total Phase Actual Spending Amount'].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds to filter outliers using plus minus 1.5 interquartile range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df_filtered = dfproj[(dfproj['Total Phase Actual Spending Amount'] >= lower_bound) &
                     (dfproj['Total Phase Actual Spending Amount'] <= upper_bound)]

# Create histogram using pandas for the filtered data
plt.figure(figsize=(8, 6))  # Set the figure size
df_filtered['Total Phase Actual Spending Amount'].plot(kind='hist', bins=30, edgecolor='black')  # Create histogram
plt.title('Histogram of Total Phase Actual Spending Amount (Without Outliers)')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Frequency')  # Set y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot

# Create box plot with matplotlib for the filtered data
plt.figure(figsize=(8, 6))  # Set the figure size
plt.boxplot(df_filtered['Total Phase Actual Spending Amount'], vert=False)  # Create box plot
plt.title('Box Plot of Total Phase Actual Spending Amount (Without Outliers)')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.yticks([])  # Remove y-axis ticks
plt.grid(True)  # Show grid
plt.show()  # Display plot

import seaborn as sns
# Create KDE plot using seaborn for the filtered data to show smoother curve of distribution
plt.figure(figsize=(8, 6))  # Set the figure size parameter
sns.kdeplot(df_filtered['Total Phase Actual Spending Amount'], shade=True)  # Create KDE plot
plt.title('KDE Plot of Total Phase Actual Spending Amount (Without Outliers)')  # Set title label
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Density')  # Set y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Calculate IQR
Q1 = dfproj['Total Phase Actual Spending Amount'].quantile(0.25)
Q3 = dfproj['Total Phase Actual Spending Amount'].quantile(0.75)
IQR = Q3 - Q1

# Identify outliers
outliers = dfproj[(dfproj['Total Phase Actual Spending Amount'] < (Q1 - 1.5 * IQR)) |
                  (dfproj['Total Phase Actual Spending Amount'] > (Q3 + 1.5 * IQR))]['Total Phase Actual Spending Amount']

# Create KDE plot of outliers
plt.figure(figsize=(8, 6))  # Set the figure size
sns.kdeplot(outliers, shade=True)  # Create KDE plot
plt.title('KDE Plot of Outliers in Total Phase Actual Spending Amount')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Density')  # Set y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Calculate IQR
Q1 = dfproj['Total Phase Actual Spending Amount'].quantile(0.25)
Q3 = dfproj['Total Phase Actual Spending Amount'].quantile(0.75)
IQR = Q3 - Q1

# Identify outliers
outliers = dfproj[(dfproj['Total Phase Actual Spending Amount'] < (Q1 - 1.5 * IQR)) |
                  (dfproj['Total Phase Actual Spending Amount'] > (Q3 + 1.5 * IQR))]['Total Phase Actual Spending Amount']

# Create KDE plot of outliers
plt.figure(figsize=(8, 6))  # Set the figure size
sns.kdeplot(outliers, shade=True)  # Create KDE plot
plt.title('KDE Plot of Outliers in Total Phase Actual Spending Amount')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Density')  # Set y-axis label
plt.grid(True)  # Show grid

# Format x-axis ticks to avoid scientific notation
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='plain', axis='x')

plt.show()  # Display plot

import pandas as pd

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Get descriptive statistics for the 'project description' column
description_stats = dfproj['Project Description'].describe()

print(description_stats)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Filter data based on project description "DATA CENTER" to create new dataframe
data_center_df = dfproj[dfproj['Project Description'] == 'DATA CENTER']

# Create KDE plot for 'Total Phase Actual Spending Amount' of Data Centers
plt.figure(figsize=(8, 6))  # Set the figure size
sns.kdeplot(data_center_df['Total Phase Actual Spending Amount'], shade=True)  # Create KDE plot
plt.title('KDE Plot of Total Phase Actual Spending Amount for DATA CENTER Projects')  # Set title label
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Density')  # Set y-axis label
plt.grid(True)  # Show grid

# Format x-axis ticks to avoid scientific notation for easier to read x-axis scale
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='plain', axis='x')

plt.show()  # Display plot

import pandas as pd

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Filter data based on project description "DATA CENTER"
data_center_df = dfproj[dfproj['Project Description'] == 'DATA CENTER']

# Get descriptive statistics for 'Total Phase Actual Spending Amount'
description_stats = data_center_df['Total Phase Actual Spending Amount'].describe()

print(description_stats)

import pandas as pd
import matplotlib.pyplot as plt

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Filter data based on project description "DATA CENTER" to create new data frame
data_center_df = dfproj[dfproj['Project Description'] == 'DATA CENTER']

# Create histogram for 'Total Phase Actual Spending Amount' including negative values
plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(data_center_df['Total Phase Actual Spending Amount'], bins=30, color='skyblue', edgecolor='black')  # Create histogram
plt.title('Histogram of Total Phase Actual Spending Amount for DATA CENTER Projects')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Frequency')  # Set y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read csv
dfproj = pd.read_csv('Projects.csv')

# Calculate IQR
Q1 = dfproj['Total Phase Actual Spending Amount'].quantile(0.25)
Q3 = dfproj['Total Phase Actual Spending Amount'].quantile(0.75)
IQR = Q3 - Q1

# Identify outliers
outliers = dfproj[(dfproj['Total Phase Actual Spending Amount'] < (Q1 - 1.5 * IQR)) |
                  (dfproj['Total Phase Actual Spending Amount'] > (Q3 + 1.5 * IQR))]['Total Phase Actual Spending Amount']

# Create histogram of outliers
plt.figure(figsize=(8, 6))  # Set the figure size
sns.histplot(outliers, kde=False, bins=30, color='blue')  # Create histogram
plt.title('Histogram of Outliers in Total Phase Actual Spending Amount')  # Set title
plt.xlabel('Total Phase Actual Spending Amount')  # Set x-axis label
plt.ylabel('Frequency')  # Set y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display plot

desc_stats = outliers.describe()
print (desc_stats)


import pandas as pd
from scipy import stats

# Read CSV
dfproj = pd.read_csv('Projects.csv')

# Select the column for analysis
data = dfproj['Total Phase Actual Spending Amount']

# Set the null hypothesis value and significance level.  This can be adjusted based on other analysis.
null_hypothesis_value = 100000
alpha = 0.05

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(data, null_hypothesis_value, alternative='greater')

# Print the null and alternative hypotheses
print("Null hypothesis: The mean spending amount is less than or equal to", null_hypothesis_value)
print("Alternative hypothesis: The mean spending amount is greater than", null_hypothesis_value)

# Print out the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Check if the null hypothesis can be rejected by comparing significance level to p-value
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")






