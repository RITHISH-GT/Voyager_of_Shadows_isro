import numpy as np

DEPTH_M          = 5.0
ICE_DENSITY      = 917.0
WATER_PER_PERSON = 1500.0
EPS_VOLUME_BASE  = 3.0
EPS_TARGET       = 4.05

SCENARIOS = {
    "Conservative": 0.05,
    "Best Estimate": 0.075,
    "Optimistic":   0.10,
}

def quantify(area_m2, depth_m, ice_frac,
             ice_density, water_per_person):
    regolith_vol = area_m2 * depth_m
    ice_vol      = regolith_vol * ice_frac
    ice_mass_kg  = ice_vol * ice_density
    water_kg     = ice_mass_kg
    person_years = water_kg / water_per_person
    return dict(
        area_m2      = area_m2,
        area_km2     = area_m2 / 1e6,
        ice_vol_m3   = ice_vol,
        ice_mass_t   = ice_mass_kg / 1000,
        water_t      = water_kg / 1000,
        person_years = person_years,
        ice_frac     = ice_frac,
    )

def run_all_scenarios(area_m2):
    return {
        name: quantify(area_m2, DEPTH_M, frac,
                       ICE_DENSITY, WATER_PER_PERSON)
        for name, frac in SCENARIOS.items()
    }