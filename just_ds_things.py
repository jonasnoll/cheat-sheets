# Just Datascience things to reuse

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


# read dataframe #######################################################################
import pandas as pd

df = pd.read_csv('../data/df_defects.csv', sep=';')



# Dates in Pandas #####################################################################

# Change to date eg. for plotting
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y-%m-%d %H:%M:%S')

# Check time period 
start = min(df.loc[:, 'DateTime'].dt.strftime('%Y-%m-%d'))
end = max(df.loc[:, 'DateTime'].dt.strftime('%Y-%m-%d'))


# Fiilter column by multipy Substring / Regex / Regstr#################################

regstr = '|'.join(['01', '02', '03', '04', '05'])
df_filtered = df[df['Type'].str.contains(regstr)]





