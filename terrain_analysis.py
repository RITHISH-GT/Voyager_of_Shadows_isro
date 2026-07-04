import numpy as np
from scipy import ndimage

ROUGH_WIN    = 11
ROUGH_PCTILE = 85
EDGE_PCTILE  = 93

def local_std(g, win):
    m  = ndimage.uniform_filter(g, win)
    m2 = ndimage.uniform_filter(g**2, win)
    return np.sqrt(np.clip(m2 - m**2, 0, None))

def compute_roughness(dn, valid):
    rough = local_std(dn, ROUGH_WIN)
    rough = np.where(valid, rough, 0)
    thr   = np.percentile(rough[valid], ROUGH_PCTILE)
    return rough, valid & (rough > thr)

def compute_edges(dn, valid):
    sm   = ndimage.gaussian_filter(dn, 1.5)
    grad = np.hypot(ndimage.sobel(sm,1), ndimage.sobel(sm,0))
    grad = np.where(valid, grad, 0)
    proxy = grad / (grad[valid].max() + 1e-9)
    thr   = np.percentile(grad[valid], EDGE_PCTILE)
    edge  = ndimage.binary_opening(valid&(grad>thr), iterations=1)
    return proxy, edge

def compute_hazard(rough_mask, boulder_mask, edge_mask, valid):
    from scipy import ndimage
    struct = ndimage.generate_binary_structure(2, 2)
    raw    = valid & (rough_mask | boulder_mask | edge_mask)
    hazard = ndimage.binary_opening(raw, struct, iterations=1)
    hazard = ndimage.binary_closing(hazard, struct, iterations=2)
    return hazard & valid