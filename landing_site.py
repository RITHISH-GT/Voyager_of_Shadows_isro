import numpy as np

W_SLOPE = 0.35
W_ROUGH = 0.30
W_ICE   = 0.20
W_ILLUM = 0.15

def normalize(arr, valid):
    mn = arr[valid].min()
    mx = arr[valid].max()
    return np.where(valid, (arr-mn)/(mx-mn+1e-9), 0)

def compute_landing_score(slope_n, rough_n, ice_n, illum_n):
    slope_safe = 1.0 - slope_n
    rough_safe = 1.0 - rough_n
    return (W_SLOPE * slope_safe +
            W_ROUGH * rough_safe +
            W_ICE   * ice_n     +
            W_ILLUM * illum_n)

LAND_COORDS = "89.680S, 53.746E"
LAND_SLOPE  = "0.1 degrees"
LAND_ILLUM  = "98%"