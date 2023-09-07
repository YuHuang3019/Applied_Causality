import os
import numpy as np
import xarray as xr
import xesmf as xe


casm_ds = xr.open_dataset("/burg/glab/users/os2328/data/casm_xr.zarr", engine="zarr")
regrid_ds = xr.Dataset({"lon":casm_ds.lon, "lat":casm_ds.lat})
igbp_ds = xr.open_dataset("./data/annual_igbp_cmg.nc")

regridder = xe.Regridder(igbp_ds, regrid_ds, "nearest_s2d")
regridded_igbp = regridder(igbp_ds)
    
regridded_igbp.to_netcdf("./data/annual_igbp.nc")