import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('z-artist-names.csv')
print(pd.options.display.max_rows)#prints the max rows present in the dataframe
print(df.to_string())#prints the entire dataframe
print(df)#prints the first and last 5 rows
print(df.head())#displays the first 5 rows of the dataframe
print(df.tail())#displays the last N rows of the dataframe
print(df.dtypes)
print(df.info())
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
fd = pd.DataFrame(data)
names=fd["Name"] #selects specific columns from a dataframe
fd.plot.box() #creates the plot
plt.show()#displays the plot
[

    method_name

    for method_name in dir(fd.plot)

    if not method_name.startswith("_")

] #displays alternative methods for plot
