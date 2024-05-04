




import pandas as pd
import matplotlib.pyplot as plt

dfwf = pd.read_csv('workforce.csv')
#print (dfwf.columns)

# Filter rows where 'Occupational Title' contains 'electrician'
electrician_df = dfwf[dfwf[' Occupational Title'].str.contains('electrician', case=False, na=False)]

# Group by 'Occupational Title' and sum 'employment'
sum_by_occupation = electrician_df.groupby(' Occupational Title')[' Employment'].sum().reset_index()
print(sum_by_occupation)



import matplotlib.pyplot as plt
# Filter rows where 'Occupational Title' contains 'electrician'
electrician_df = dfwf[dfwf[' Occupational Title'].str.contains('electrician', case=False, na=False)]

# Group by ' Area Name' and sum ' Employment'
sum_by_area = electrician_df.groupby(' Area Name')[' Employment'].sum().reset_index()

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(sum_by_area[' Area Name'], sum_by_area[' Employment'], color='blue')
plt.xlabel('Area Name')
plt.ylabel('Total Employment')
plt.title('Total Employment of Electricians by Area')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


print(dfwf.columns)
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
dfwf = pd.read_csv('workforce.csv')

# Filter rows where 'Occupational Title' contains 'electrician'
electrician_df = dfwf[dfwf[' Occupational Title'].str.contains('electrician', case=False, na=False)]

# Plot a histogram
plt.figure(figsize=(10, 6))
plt.hist(electrician_df['Mean Wage'], bins=20, color='green', edgecolor='black')
plt.xlabel('Mean Wage')
plt.ylabel('Frequency')
plt.title('Histogram of Mean Wage for Electricians')
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
dfwf = pd.read_csv('workforce.csv')

# Filter rows where 'Occupational Title' contains 'electrician'.  This should show electricians and helpers.
electrician_df = dfwf[dfwf[' Occupational Title'].str.contains('electrician', case=False, na=False)]

descriptive_stats_wage = electrician_df['Mean Wage'].describe()
print(descriptive_stats_wage)

# Set the style and size for seaborn plot
sns.set(style="whitegrid")

# Plot a smooth distribution of mean wages for electricians in the state of New York
plt.figure(figsize=(10, 6))
sns.kdeplot(electrician_df['Mean Wage'], shade=True, color='green')
plt.xlabel('Mean Wage')
plt.ylabel('Density')
plt.title('Smooth Distribution of Mean Wage for Electricians')
plt.grid(True)
plt.tight_layout()
plt.show()



import pandas as pd
import scipy.stats as stats

# Data has already been loaded and filtered by area in earlier part of script
# Calculate the mean number of electricians of all the areas in New York
mean_electricians = sum_by_area[' Employment'].mean()

# Define the specified value for comparison
specified_value = 100  # This value can be adjusted based on feedback from the business

# Perform one-sample t-test.  (one-sided: greater than)
t_statistic, p_value = stats.ttest_1samp(sum_by_area[' Employment'], specified_value, alternative='greater')

# Print the results and hypothesis
print("One-Sample T-Test Results:")
print("===================================")
print(f"Null Hypothesis: The mean number of electricians in New York is {specified_value}.")
print(f"Alternative Hypothesis: The mean number of electricians in New York is greater than {specified_value}.")
print("-----------------------------------")
print(f"Sample Mean: {mean_electricians}")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")
print("-----------------------------------")

# Compare p-value to the significance level of .05
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis.")
    print("There is sufficient evidence to suggest that the mean number of electricians in New York is greater than the specified value.")
else:
    print("Conclusion: Fail to reject the null hypothesis.")
    print("There is not sufficient evidence to suggest that the mean number of electricians in New York is greater than the specified value.")


import pandas as pd
import scipy.stats as stats

# Load the data
dfwf = pd.read_csv('workforce.csv')

# Filter rows where 'Occupational Title' contains 'electrician'
electrician_df = dfwf[dfwf[' Occupational Title'].str.contains('electrician', case=False, na=False)]

# Group by 'Area Name' and sum 'Employment'
sum_by_area = electrician_df.groupby(' Area Name')[' Employment'].sum().reset_index()

# Calculate the mean number of electricians in New York
mean_electricians = sum_by_area[' Employment'].mean()

# Define the specified value for comparison
specified_value = 100  # You can replace this with any other value if needed

# Perform one-sample t-test (one-sided: greater than)
t_statistic, p_value = stats.ttest_1samp(sum_by_area[' Employment'], specified_value, alternative='greater')

# Print the results
print("One-Sample T-Test Results:")
print("===================================")
print(f"Null Hypothesis: The mean number of electricians in New York is {specified_value}.")
print(f"Alternative Hypothesis: The mean number of electricians in New York is greater than {specified_value}.")
print("-----------------------------------")
print(f"Sample Mean: {mean_electricians}")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")
print("-----------------------------------")

# Compare p-value to the significance level
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis.")
    print("There is sufficient evidence to suggest that the mean number of electricians in New York is greater than the specified value.")
else:
    print("Conclusion: Fail to reject the null hypothesis.")
    print("There is not sufficient evidence to suggest that the mean number of electricians in New York is greater than the specified value.")


import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
dfwf = pd.read_csv('workforce.csv')

# Filter rows where 'Occupational Title' contains 'electrician'
electrician_df = dfwf[dfwf[' Occupational Title'].str.contains('electrician', case=False, na=False)]

# Group by 'Occupational Title' and sum 'employment'
sum_by_occupation = electrician_df.groupby(' Occupational Title')[' Employment'].sum().reset_index()
print(sum_by_occupation)

# Descriptive statistics for the 'Employment' column of the filtered data
electrician_employment_stats = electrician_df[' Employment'].describe()

# Print descriptive statistics
print("\nDescriptive Statistics for Employment of Electricians:")
print(electrician_employment_stats)

# Plot a histogram for the 'Employment' column of electricians
plt.hist(electrician_df[' Employment'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Employment')
plt.ylabel('Frequency')
plt.title('Histogram of Employment for Electricians')
plt.show()