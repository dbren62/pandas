import pandas as pd


grades = pd.Series([87, 100, 94])

print(grades)

grades = pd.Series(98.6, range(3))

print(grades)

a = grades[0]
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

# Calling Series method describe produces all these stats and more:
grades.describe()


grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])

print(grades)

# If you initalize a Series with a dictionary, its keys become the
# Series' indices, and its vlaues become the Series' element values:

grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})

# you can acces individual elements via square brackets
# containing a custom index value:
print(grades["Eva"])

# If the custom indices  are strings that could represent valid Python identifiers,
# pandas automatically adds them to the Series as attributes that you can access

grades.Wally

# Series also has built-in attribute. For example, the dtype attribute returns
# underlying array's element type:
grades.dtype

grades.values