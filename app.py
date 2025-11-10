import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------
# Employee Salary Increment Application
# ---------------------------------------------

# Employee data
data = {
    'Employee ID': ['2025ENGG0030', '2025ENGG1066', '2025ENGG0581', '2025ENGG0678'],
    'Employee': ['Kapil', 'Cherry', 'Arnab', 'Raahi'],
    'Base_Salary': [16000, 18000, 20000, 25000],
    'Experience_Years': [1, 2, 3, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Employees eligible for special increment
special_increment_ids = ['2025ENGG1066', '2025ENGG0678']  # Example IDs

# Define increment logic
def calculate_increment(base_salary, years, emp_id):
    increment_rate = 0.12  # 12% per year
    salary = base_salary * (1 + increment_rate) ** years

    # Apply special bonus if applicable
    if emp_id in special_increment_ids:
        salary += 15000  # Special bonus

    return salary

# Apply increment calculation
df['Updated_Salary'] = [
    calculate_increment(row['Base_Salary'], row['Experience_Years'], row['Employee ID'])
    for _, row in df.iterrows()
]

# Round salary
df['Updated_Salary'] = df['Updated_Salary'].round(2)

# Display updated table
print("\n🏢 Employee Salary Details (After Increment):\n")
print(df.to_string(index=False))

# 🔍 Lookup feature
emp_id = input("\nEnter Employee ID to view details: ").strip()
if emp_id in df['Employee ID'].values:
    emp_info = df[df['Employee ID'] == emp_id]
    print("\nEmployee Details:\n")
    print(emp_info.to_string(index=False))
else:
    print("\n❌ Employee ID not found.")

# 📊 Plotting the graph
plt.figure(figsize=(8, 6))
plt.bar(df['Employee'], df['Updated_Salary'], color='teal')
plt.title('Updated Salaries After 12% Annual Increment', fontsize=14)
plt.xlabel('Employee', fontsize=12)
plt.ylabel('Updated Salary (INR)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
