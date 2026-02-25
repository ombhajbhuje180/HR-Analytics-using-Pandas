# =========================================
# HR Analytics Project (Beginner Friendly)
# =========================================
# This project is about understanding employee data.
# We analyze experience, salary, departments,
# and identify valuable employees using Pandas.
# =========================================


# -----------------------------
# Import required libraries
# -----------------------------
# pandas -> data handling
# numpy  -> conditional logic
# matplotlib -> charts

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Create employee dataset
# -----------------------------
# Normally data comes from CSV or database,
# but here we are creating it manually for practice.

df = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Aman", "Riya", "Karan", "Neha", "Sohan", "Anita", "Rohit", "Pooja"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT"],
    "Age": [24, 29, 31, 26, 35, 28, 40, 23],
    "Salary": [40000, 52000, 60000, 48000, 75000, 58000, 90000, 30000],
    "Experience": [1, 5, 7, 3, 10, 6, 15, 0],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Pune", "Delhi", "Nagpur"],
    "JoinDate": [
        "2023-01-15", "2022-06-10", "2021-03-20", "2023-07-01",
        "2019-11-05", "2020-02-17", "2018-08-25", "2024-01-10"
    ],
    "Email": [
        "aman@gmail.com", None, "karan@gmail.com", None,
        "sohan@gmail.com", "anita@gmail.com", None, "pooja@gmail.com"
    ]
})

# Convert JoinDate column to proper date format
df["JoinDate"] = pd.to_datetime(df["JoinDate"])


# -----------------------------
# Task 1: Find skilled employees
# -----------------------------
# Conditions:
# - Department should be IT or HR
# - Experience should be 5 years or more
# - Email should be available
# - Joined before 2023

Skilled_Employees = df.loc[
    (df["Department"].isin(["IT", "HR"])) &
    (df["Experience"] >= 5) &
    (df["Email"].notna()) &
    (df["JoinDate"] < "2023-01-01")
].copy()


# -----------------------------
# Task 2: Experience level column
# -----------------------------
# If experience is 5 or more -> Senior
# Otherwise -> Junior

df["Experience_Level"] = np.where(
    df["Experience"] >= 5,
    "Senior",
    "Junior"
)


# -----------------------------
# Task 3: Salary band column
# -----------------------------
# High   -> Salary >= 60000
# Medium -> 40000 to 59999
# Low    -> Below 40000

df["Salary_Band"] = np.select(
    [
        df["Salary"] >= 60000,
        (df["Salary"] >= 40000) & (df["Salary"] < 60000)
    ],
    ["High", "Medium"],
    default="Low"
)


# -----------------------------
# Task 4: Salary revision
# -----------------------------
# Employees who joined before 2020
# get a 10% salary increment

df.loc[df["JoinDate"] < "2020-01-01", "Salary"] += (
    df.loc[df["JoinDate"] < "2020-01-01", "Salary"] * 0.10
)


# -----------------------------
# Task 5: Location based count
# -----------------------------
# Count employees:
# - City name contains 'pu'
# - Department is NOT Finance

count_pune = df.loc[
    (df["City"].str.contains("pu", case=False)) &
    (df["Department"] != "Finance")
].shape[0]


# -----------------------------
# Task 6: High value IT employees
# -----------------------------
# Conditions:
# - IT department
# - High salary band
# - Senior experience level

High_Value_IT = df.loc[
    (df["Department"] == "IT") &
    (df["Salary_Band"] == "High") &
    (df["Experience_Level"] == "Senior")
]


# -----------------------------
# Simple analysis using groupby
# -----------------------------
# These give a quick business overview

avg_salary_by_dept = df.groupby("Department")["Salary"].mean()
salary_band_count = df.groupby("Salary_Band")["EmpID"].count()
avg_salary_by_experience = df.groupby("Experience_Level")["Salary"].mean()


# -----------------------------
# Visualization
# -----------------------------
# Bar chart showing average salary by department

plt.figure(figsize=(6, 4))
avg_salary_by_dept.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()


# -----------------------------
# Final understanding
# -----------------------------
# IT department pays the highest on average
# Senior employees mostly fall in High salary band
# Old employees benefited from salary increment
# Salary bands make compensation easy to understand