import os, argparse
import numpy as np
import matplotlib.pyplot as plt

from model import PENG_model
from utils import integration_utils
from scipy.optimize import newton_krylov, brentq

from astropy.cosmology import Planck15 as cosmo, z_at_value

z_init  = 10
z_final = 0

cluster_mass = 13.5  #log10(Mhalo)
n_clusters   = 100

oc_flag      = True      #
oc_eta       = 2

logMh_range  = np.arange(9,14,0.1)
logMs_range  = np.arange(0.5,11.5,0.1)
Mh_range     = np.power(10, logMh_range)
z_range      = np.arange(0,10,0.1)

if __name__ == "__main__":
    model           = PENG_model()
    # model.sf_masses = 4.5
    # model.setup_evolve(10,0)
    
    # while model.t >= model.t_final and model.condition:
    #     model.mass_array  = model.integ.RK45(model.mass_array, model.t, model.force)
        
    #     if (model.t - model.integ.step) > model.t_final:
    #         pass
    #     else:
    #         model.integ.step = model.t - model.t_final
    #         model.force      = True
    #         model.condition  = False
            
    #     print(np.log10(model.mass_array))
            

    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
    
    # model.oc_eta = 1
    # tt = np.array([cosmo.lookback_time(z).value - model.t_delay_2(Mh_range, z) for z in z_range])
    
    # fig,ax = plt.subplots()
    # ax.contourf(z_range, logMh_range, tt.T, np.arange(0,14,2), extend='both')
    
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
    
    logMh = np.array([[brentq(model.M_star_inv(logMs,z), 5, 35 ) for z in z_range] for logMs in logMs_range])
    
    fig,ax = plt.subplots()
    contourf_ = ax.contourf(z_range, logMs_range, logMh)#, np.arange(0,14,2), extend='both')
    cbar      = fig.colorbar(contourf_, label='Halo Mass')
    ax.set_xlabel('z')
    ax.set_ylabel('stellar mass')
    
plt.show()