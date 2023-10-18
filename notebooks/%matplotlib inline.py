%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data_one = pd.read_csv('/workspaces/codespaces-jupyter/Gen AI Project/Construction_Data_PM_Forms_All_Projects.csv')
data_two = pd.read_csv('/workspaces/codespaces-jupyter/Gen AI Project/Construction_Data_PM_Tasks_All_Projects.csv')

# Report the total number of tasks that are overdue.

# Report the total number of tasks that are overdue.
# For loop iterates over the overdue col in the first data sheet, count adds one for every "TRUE" present
# Results are printed out 
count = 0 
overdue_col1 = data_one['OverDue']
for i in overdue_col1: 
    if i == 'True': 
        count = count + 1 

print(f"The word 'TRUE' appears {count} times in the overdue column.")

overdue_ds1 = data_one[data_one['OverDue'] == 'True'].groupby('Project').size()
print(overdue_ds1)

# For loop iterates over the overdue col in the second data sheet, count2 adds one for every "TRUE" present
# Results are printed out 
count2 = 0 
overdue_col2 = data_two['OverDue']

for n in overdue_col2: 
    if n == 'True': 
        count2 = count2 + 1 

print(f"The word 'TRUE' appears {count2} times in the overdue column.")

overdue_ds2 = data_two[data_two['OverDue'] == 'True'].groupby('project').size()
print(overdue_ds2)

# Report the Total Number of Open and Closed Tasks by Each Task Group. 

#Iterates over the two rows, and prints them together side by side 
# (not super necessary but was a good visual for me to see)
for index, row in data_two.iterrows():
    status = row['Status']
    task_groups = row['Task Group']

#Groups the data columns together by Task Group and Status, combines each of the projects 
# that had the same status by department, and then prints the results
grouped_data = data_two.groupby(['Task Group', 'Status']).size()
print(grouped_data)

# Create a bar chart of the total number of open and closed tasks by each Task Group 
grouped_data = grouped_data.unstack()

# Create a bar chart of the reshaped data
grouped_data.plot(kind='bar', stacked = 'true', figsize=(12, 6))

# X and Y labels and Chart Title Label 
plt.xlabel('Task Group')  # This labels the x-axis
plt.ylabel('Number of Tasks')  # This labels the y-axis
plt.title('Total Number of Tasks by Status and Task Group')

# Shows the bar chart 
plt.show()

# Create a bar chart of the total number of overdue tasks by project. 
overdue_ds1.plot(kind='bar', figsize=(12, 6), width=1)
plt.xlabel('Project')  # This labels the x-axis (the horizontal one)
plt.ylabel('Number of Overdue')  # This labels the y-axis (the vertical one)
plt.title('Number of Overdue by Project')  # This gives our chart a title
plt.show()

overdue_ds2.plot(kind='bar', figsize=(12, 6))
plt.xlabel('Project')  # This labels the x-axis (the horizontal one)
plt.ylabel('Number of Overdue')  # This labels the y-axis (the vertical one)
plt.title('Number of Overdue by Project')  # This gives our chart a title
plt.show()

# Create a bar chart of the percentage of overdue tasks by project. (Optional) 

# Report the mean number of days elapsed since forms were opened by project.(Optional) 

# Create a bar chart of the number of open forms by Type of form. (Optional)

# Create a time series plot of the number of forms opened (which are currently open) by Report Form Group. (Optional)
