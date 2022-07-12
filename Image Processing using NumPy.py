import numpy as np   # for arrays
import pandas as pd    # for data frame, data leaning, and analysis
import matplotlib.pyplot as plt    # for graph plotting and data visualization
import scipy    # optimization, stats and signal processing
import warnings  #
import skimage   # remove the unwanted portion of image or to focus on a particular part of the image
import imageio   # provides an easy interface to read and write a wide range of image data

warnings.filterwarnings('ignore')

print("******reading of image/reading of dataframe in image format*******")
df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
print(df)                    # this will display image data im matrix format
print(df.shape)              # length width and layers

print("********* Display of image *****")
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print(df.size)  # ??
print(df.min(),df.max())  # min(red, green, blue) & max(red, green, blue)
print(df.mean())            # mean of (value of (red, green, blue pixels))

print(df[150,250])          # this syntax will show value of Red green and blue at 150,250 pixel
print(df[150,250,0])        # this syntax will show value of green, 0-red, 1-green, 2-blue

print(df[1,1])

print("******************setting red green and blue value to zero at 150,250 pixel****************")

df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
df[150,250] = 0
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print("***************changing the colour to full intensity for selected range of pixel********* ")

df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
df[200:800, : , 2] = 255
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print(" for white pixel")
df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
df[200:800, : ] = 255
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print(" for Black Pixel ")
df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
df[200:800, : ] = 0
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()


print("*************** filtering out low values pixel < 100 ************************")
df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
print(df.shape)
low_value_filter = df < 200  # what's the use of this line
print("shape of low value filter:- ", low_value_filter.shape)

print("setting all low values pixel to zero value")
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()
df[low_value_filter] = 0
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print("***************** finding range of ROW and COLUMN ****************************")
row_range = np.arange(len(df))   # this command arrange in 1D format (start stop and difference)
print(row_range)
# col_range = np.arange(len(df[1]))
# print(col_range)
col_range = row_range
print(col_range)

print("****************** diagonally white colour ***********************************")
df[row_range, col_range] = 255
print(df)
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print("********************* image in circular form ************************")
row, col, lyr = df.shape  # 1D
x, y = np.ogrid[:row, :col]   # 1D
# print(x.shape, y.shape)
center_row, center_col = row/2, col/2   # float
center_distance = (x-center_row)**2 + (y-center_col)**2  # it will convert into 2D
print("center_distance", center_distance.shape)
radius = (row/2)**2     # float
circular_mask = (center_distance > radius)   # 2D
print("circular mask",circular_mask.shape)
# print(circular_mask[1500:1700, 2000:2200])     # it will create an array of true and false

df = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
df[circular_mask] = 255
plt.figure(figsize=(5,5))
plt.imshow(df)
plt.show()

print("We can further improve the mask, for example just get upper half disc")
X, Y = np.ogrid[:row, :col]
half_upper = X < center_row              # this line generates a mask for all rows above the center
half_lower = X > center_row
half_upper_mask = np.logical_and(half_upper, circular_mask)
print("half upper mask", half_upper_mask.shape)
half_lower_mask = np.logical_or(half_lower, circular_mask)
print("half lower mask", half_lower_mask.shape)
photo_data = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
photo_data[half_upper_mask] = 255
photo_data[half_lower_mask] = 255
plt.figure(figsize=(15,15))
plt.imshow(photo_data)
plt.show()


photo_data = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
red_mask = photo_data[:,:,0] < 150
photo_data[red_mask] = 255
plt.figure(figsize=(5,5))
plt.imshow(photo_data)
plt.show()

photo_data = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
green_mask = photo_data[:,:,1] < 150
photo_data[green_mask] = 255
plt.figure(figsize=(5,5))
plt.imshow(photo_data)
plt.show()

photo_data = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
blue_mask = photo_data[:,:,2] < 150
photo_data[blue_mask] = 255
plt.figure(figsize=(5,5))
plt.imshow(photo_data)
plt.show()

photo_data = imageio.imread(r"H:\DataScience\Day-28\26 JUNE 2022\Projects\data\sd-3layers.jpg")
red_mask = photo_data[:,:,0] < 150
green_mask = photo_data[:,:,1] > 100
blue_mask = photo_data[:,:,2] < 100
final_mask = np.logical_and(red_mask, green_mask, blue_mask)
print("final mask", final_mask.shape)
photo_data[final_mask] = 255
plt.figure(figsize=(5,5))
plt.imshow(photo_data)
plt.show()
