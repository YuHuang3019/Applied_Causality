import os
import numpy as np
import xarray as xr
import xesmf as xe


casm_ds = xr.open_dataset("/burg/glab/users/os2328/data/casm_xr.zarr", engine="zarr")
regrid_ds = xr.Dataset({"lon":casm_ds.lon, "lat":casm_ds.lat})
ai_ds = xr.open_dataset("./data/terra_AI.nc")

regridder = xe.Regridder(ai_ds, regrid_ds, "bilinear")
regridded_ai = regridder(ai_ds)
regridded_ai.to_netcdf("./data/AI_EASE2.nc")