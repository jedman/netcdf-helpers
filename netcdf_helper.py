import netCDF4 as nc 
import numpy as np

class ncvar():
    '''generic variable for writing to netcdf file'''
   
    def __init__(self, name):
        self.name = name 
        self.dims = list() # list with dimension names 
        self.data = [] # array with data
	self.long_name = ''
        self.units = '' 
        return
    
    def add_dim(self, dim_name):
        self.dims.append(dim_name) 
        return

class ncdim():
     '''should be nearly identical to ncvar object, except the only dim is itself'''
     def __init__(self, name):
         self.name = name 
         self.dims = name
         self.data = []
         self.long_name = ''
         self.units = ''
         return 

def create_netcdf(filename, ncvars, ncdims):
    '''takes a dict of ncvar objects and writes to a file'''
     
    ncfile = nc.Dataset(filename,'w')
    
    # first argument is name of variable, second is datatype, third is
    # a tuple with the names of dimensions.
    outvars = {}
    outdims = {}
    for name in ncdims:
        # create dimension 
        outdims[name] = ncfile.createDimension(name, ncdims[name].data.shape[0])
        # create a variable matching dimension
        outvars[name] = ncfile.createVariable(name, np.float, (name, )) 
        outvars[name][:] = ncdims[name].data
        outvars[name].units = ncdims[name].units
        outvars[name].long_name = ncdims[name].long_name  
        
    
    for name in ncvars: 
        # create the variable
        outvars[name] = ncfile.createVariable(name, np.float, ncvars[name].dims)
        outvars[name][:] = ncvars[name].data
        outvars[name].units = ncvars[name].units
        outvars[name].long_name = ncvars[name].long_name  
    
    ncfile.close() 
    return 


