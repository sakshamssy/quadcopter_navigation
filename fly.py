//how to import csv file from folder?
import csv

# Define data
data = [
    (1, "A towel,", 1.0),
    (42, " it says, ", 2.0),
    (1337, "is about the most ", -1),
    (0, "massively useful thing ", 123),
    (-2, "an interstellar hitchhiker can have.", 3),
]

# Write CSV file
with open("test.csv", "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(data)

# Read CSV file
with open("test.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(data_read)


[['1', 'A towel,', '1.0'],
 ['42', ' it says, ', '2.0'],
 ['1337', 'is about the most ', '-1'],
 ['0', 'massively useful thing ', '123'],
 ['-2', 'an interstellar hitchhiker can have.', '3']]


import mpu.io
data = mpu.io.read('example.csv', delimiter=',', quotechar='"', skiprows=None)
mpu.io.write('example.csv', data)


import pandas as pd

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('myfile.csv', sep=',')
print(df)

# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
dicts = df.to_dict().values()


1,"A towel,",1.0
42," it says, ",2.0
1337,is about the most ,-1
0,massively useful thing ,123
-2,an interstellar hitchhiker can have.,3





