import h5py
import numpy as np

file_loc = './data/train/data.h5py'
file_loc = "../kakao_comp_data/train.chunk.01"

# file_loc = "../kakao_comp_data/dev.chunk.01"
f = h5py.File(file_loc, 'r')


list(f.keys())
dset = f['train']

nset = np.array(dset)

for i, item in enumerate(f['train']['img_feat']):
    if i == 10:
        break
    print(i, item)

print(len(f['train']['img_feat'][1]))

cols = []
for i, item in enumerate(f['train']):
    if i == 15:
        break
    print(i, item)
    cols.append(item)


['bcateid',
 'brand',
 'dcateid',
 'img_feat',
 'maker',
 'mcateid',
 'model',
 'pid',
 'price',
 'product',
 'scateid',
 'updttm']

unnecessay_cols = ['img_feat',]

print([col for col in cols if col not in unnecessay_cols])
for i in range(0, 20):
    row_i = []
    for j in range(len(cols)):
        col_row = f['train'][cols[j]][i]
        if isinstance(col_row, type(b'')):
            col_row = col_row.decode('utf-8')
        if cols[j] not in unnecessay_cols:
            row_i.append(col_row)
    print(row_i)

import pandas as pd


file_loc = './data/train/data.h5py'
file_loc = "../kakao_comp_data/train.chunk.01"

chunksize = 10000
pd.read_hdf(file_loc, chunksize=chunksize)

for item in f['train'].items():
    print(item)

#
# import numpy as np
# from PIL import Image
# import PIL
#
# img = np.copy(f['train']['img_feat'][1])
# img = np.reshape(img, (32, 64))
# # img = np.reshape(img, (64, 32))
# img = PIL.Image.fromarray(img)
# img.show()

#
# This examaple creates an HDF5 file dset.h5 and an empty datasets /dset in it.
#
#
# Create a new file using defaut properties.
#
file = h5py.File('dset.h5','w')
#
# Create a dataset under the Root group.
#
dataset = file.create_dataset("dset",(4, 6), h5py.h5t.STD_I32BE)
print ("Dataset dataspace is", dataset.shape)
print ("Dataset Numpy datatype is", dataset.dtype)
print ("Dataset name is", dataset.name)
print ("Dataset is a member of the group", dataset.parent)
print ("Dataset was created in the file", dataset.file)
#
# Close the file before exiting
#
file.close()
#
# This example writes data to the existing empty dataset created by h5_crtdat.py and then reads it back.
#
#
# Open an existing file using default properties.
#
file = h5py.File('dset.h5','r+')
#
# Open "dset" dataset under the root group.
#
dataset = file['/dset']
#
# Initialize data object with 0.
#
data = np.zeros((4,6))
#
# Assign new values
#
for i in range(4):
    for j in range(6):
        data[i][j]= i*6+j+1
#
# Write data
#
print("Writing data...")
dataset[...] = data
#
# Read data back and print it.
#
data_read = dataset[...]
print(data_read)
#
# Close the file before exiting
#
file.close()
