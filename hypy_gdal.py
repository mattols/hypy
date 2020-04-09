
import pandas
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal, gdalnumeric

#filename = "Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort"
filename = "/Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort"

casi = gdal.Open(filename)

b1 = casi.GetRasterBand(1)


b1arr = gdalnumeric.BandReadAsArray(b1)
b1mask = np.ma.masked_values(
    b1arr,
    b1.GetNoDataValue(),
    copy=False
)

plt.figure()
plt.imshow(b1mask)
plt.legend()
plt.show()


# np.ma.vstack or dstack
# multi-dimentional array

