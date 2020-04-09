import xarray as xr

# filename = "/Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort"
filename = "/Users/mattolson/data/ASO/CASI/20170220/174008/casi_test.nc"


data = xr.open_dataset(filename)

print(data.dims)
print(data.data_vars)



# # tips
# gdalsrsinfo -V filename = "/Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort"
# gdalinfo /Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort
# gdal_translate -of netCDF /Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort /Users/mattolson/data/ASO/CASI/20170220/174008/casi_test.nc

# import
#
# filename = "/Users/mattolson/data/ASO/CASI/20170220/174008/CASI_2017_02_20_174008_atm_ort"
#
# casi = rasterio.open(filename)