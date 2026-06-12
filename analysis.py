import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("students.csv")

print("\n===== DATASET =====")
print(df)

# Dataset Information
print("\n===== DATASET INFO =====")
df.info()

# Missing Values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Summary Statistics
print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# Students Scoring Above 80
high_scorers = df[df["Marks"] > 80]

print("\n===== STUDENTS ABOVE 80 MARKS =====")
print(high_scorers)

# Department-wise Average Marks
dept_avg = df.groupby("Department")["Marks"].mean()

print("\n===== DEPARTMENT AVERAGE MARKS =====")
print(dept_avg)

# Highest Scorer
highest = df.loc[df["Marks"].idxmax()]

print("\n===== HIGHEST SCORER =====")
print(highest)

# Insights
print("\n===== INSIGHTS =====")
print("Average Marks:", df["Marks"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Bar Graph
dept_avg.plot(kind="bar")

plt.title("Department Wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.savefig("graph.png")

plt.show()