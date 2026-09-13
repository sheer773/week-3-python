
with open("sample.txt", "w") as f:
    f.write("Hello mawa\nIla undi week 3\nPython easy ye")

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")


    # 2 files create 
with open("file1.txt", "w") as f: f.write("Idi first file\n")
with open("file2.txt", "w") as f: f.write("Idi second file\n")

# merge code
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data = f1.read() + f2.read()

with open("merged.txt", "w") as mf:
    mf.write(data)

print("Merged file created!")



import pandas as pd
# sample csv create 
data = {"Name": ["Sheer", "Rahul", "Teja"], "Marks": [85, 90, 78]}
df = pd.DataFrame(data)
df.to_csv("marks.csv", index=False)

# read & analyze
df = pd.read_csv("marks.csv")
print(df)
print("\nAverage marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())


#4
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 90]

plt.plot(days, marks, marker='o')
plt.title("Week 3 Practice - Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


#5
import json

# data
student = {"name": "Sheer", "course": "Python", "week": 3}

# write JSON
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

print("JSON created!")

# read JSON
with open("student.json", "r") as f:
    data = json.load(f)
    print("Data from JSON:", data)
    print(f"Name is {data['name']}")