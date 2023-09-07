import os
import numpy as np
import xarray as xr
import xesmf as xe

annual_sif_dir = [os.path.join("./data", "csif_annual", f) for f in sorted(os.listdir(os.path.join("./data", "csif_annual")))]
casm_ds = xr.open_dataset("/burg/glab/users/os2328/data/casm_xr.zarr", engine="zarr")
regrid_ds = xr.Dataset({"lon":casm_ds.lon, "lat":casm_ds.lat})
regridder = xe.Regridder(xr.open_dataset(annual_sif_dir[0]), regrid_ds, "bilinear")
regrid_ds_list = []
for f in annual_sif_dir:
    sif_ds = xr.open_dataset(f)
    regrid_sif_ds = regridder(sif_ds)
    regrid_ds_list.append(regrid_sif_ds)
    
combined_regrid = xr.concat(regrid_ds_list, dim="time")
combined_regrid.to_netcdf("./data/regrided_csif.nc")