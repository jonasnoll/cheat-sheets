# Just Datascience things to reuse


# Add to Sys path so you can auto reaload updates on imports ##########################

# On top of Notebook
import sys 

sys.path.append('/Path/Devprojects/project')
%load_ext autoreload
%autoreload 2



# Read CSV and Start Analyzing ########################################################

import pandas as pd

filepath = 'pathToFile' # Liked Dishes 
df = pd.read_csv(filepath, sep=',', skiprows=0) # or '\t'
# Check if Any Values are NaN
print(f'Null Values existing: {df.isnull().values.any()}')
print(df.shape)
df.head()

# Only Take certain columns ###########################################################

# df.loc[rows, columns]
df = df.loc[:,['ColumnX']]
df

# Show Uniques & Count them ###########################################################

df['hID'].value_counts()

# with condition
df.loc[df['mID']=='A','hID']
# or stirngs
df.loc[df['mID'].str.contains("hello"),'hID']

# Just counts
df['hID'].unique()

#Count distinct values, use nunique:
df['hID'].nunique()

# Count only non-null values, use count:
df['hID'].count()

#Count total values including null values, use the size attribute:
df['hID'].size


# Writing & Open Files #################################################################

filepath ="my/path/file.txt"
# Opening
with open(filepath) as f:
    data = json.load(f)
# Writing
with open(filepath, "w") as text_file:
    text_file.write(data)


# Read Textfile only ###################################################################

with open("filename.txt", "rt") as f:
    data_lines = f.readlines()


# Save & Load Python Object ############################################################
import pickle as pkl

#write
with open("filename.pkl", "wb") as f:
    pkl.dump(obj, f)

#open
with open("filename.pkl", "rb") as f:
    obj = pkl.load(f)


# Notebook Access to parent folders ####################################################
import sys 

sys.path.append('/Users/path/to/project')
%load_ext autoreload
%autoreload 2


# Easy & Simple Dataframe for testing ##################################################

import pandas as pd

d = {'A': [1, 2, 3, 4], 'B': [4, 5, 6, 7]}
df = pd.DataFrame(data=d)
df

# Add Dict to Dataframe ################################################################

df = pd.DataFrame(columns=['A', 'B'])

dic = {'A':2, 'B':12}
df = pd.concat([df, pd.DataFrame.from_records([dic])], ignore_index=True)
 

# Append Dataframe to Df (Join Dataframes)##############################################

a_df = pd.DataFrame() # Empty DF
b = {'A': [1, 2, 3], 'B': [4, 5, 6]}
b_df = pd.DataFrame(data=d)

df = pd.concat([a_df, b_df], ignore_index=True)


# Map function to Dataframe ############################################################

df['C'] = df['B'].map(lambda x: x+1)
df


# Plotting ##########################
print("https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html")

import matplotlib.pyplot as plt


# Timestamp String to Dt
df['DateTime'] = pd.to_datetime(df['timestamp']) # optional mit format format='%Y-%m-%d

fig = plt.figure(figsize=(8, 6), dpi=80)
ax = plt.axes()

x = df['DateTime']
y = df['metric']

ax.plot(x, y);

plt.title(f"Plot Title")
plt.xlabel("Datetime")
plt.ylabel('Metric');
plt.show()


# MULTIPLE PLOTS IN FIGURE

# Initialise the subplot function using number of rows and columns
cols = 5
rows = 6
figure, axis = plt.subplots(rows, cols, figsize=(24, 20), dpi=80)
figure.tight_layout()
# Get locations of the plots
locs = [(r,c) for r in range(rows) for c in range(cols)]

y = [1,2,3]
x = df['timestamp']
for loc in locs:
    axis[loc].bar(x, y)
    axis[loc].set_title('mytitle')

plt.show()


# Open Image as Np #####################################################################

from PIL import Image 
import numpy as np

img = Image.open("imagefile.jpg")
img = np.asarray(img)


# Epochs & Batch Size ##################################################################

'''
epoch = 1 forward and backward pass of ALL training samples

batch_size = number of training samples in one forward & backward pass

number of iterations = number of passes, each pass using [bath_size] number of samples

eg. 100 samples, batch_size=20 --> 100/20 = 5 iterations for 1 epoch
'''


# read & save dataframe #######################################################################
import pandas as pd

# Read
df = pd.read_csv('../data/df_defects.csv', sep=';')

# Save
df.to_csv('Path/to/save.csv', index=False)


# Dates in Pandas #####################################################################

# Change to date eg. for plotting
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y-%m-%d %H:%M:%S')

# Check time period 
start = min(df.loc[:, 'DateTime'].dt.strftime('%Y-%m-%d'))
end = max(df.loc[:, 'DateTime'].dt.strftime('%Y-%m-%d'))


# Fiilter column by multiple Substring / Regex / Regstr #################################

regstr = '|'.join(['01', '02', '03', '04', '05'])
df_filtered = df[df['Type'].str.contains(regstr)]





