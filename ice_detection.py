import numpy as np
from scipy import ndimage

SHADOW_DN_MAX = 51
LIT_DN_MIN    = 115
ROUGH_WIN     = 11
ROUGH_PCTILE  = 85

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def compute_cpr_dop(dn_norm):
    cpr = 0.4 + 1.2 * dn_norm
    dop = np.clip(0.9 - 0.8 * dn_norm, 0.05, 0.95)
    return cpr, dop

def compute_ice_score(cpr, dop, valid):
    score = (0.6 * sigmoid((cpr - 1.0) * 6.0) +
             0.4 * sigmoid((0.30 - dop) * 8.0))
    score = np.where(valid, score, 0.0)
    mn, mx = score[valid].min(), score[valid].max()
    return np.where(valid, (score-mn)/(mx-mn+1e-9), 0.0)

def detect_ice_candidates(dn, valid):
    cpr, dop = compute_cpr_dop(dn/255.0)
    return compute_ice_score(cpr, dop, valid)