Voyagers of Shadows
Bharatiya Antariksh Hackathon 2026 — Problem Statement 8
Uncovering water in the Moon's darkness

What We Built
An integrated end-to-end pipeline that transforms raw Chandrayaan-2
DFSAR radar and OHRC optical data into a complete mission intelligence
package for lunar south pole ice detection and resource planning.
We go beyond detection — we deliver landing sites, rover paths,
and resource estimates, all in one pipeline.


The Problem
The lunar south pole holds water ice trapped in Permanently Shadowed
Regions (PSRs) — craters that never receive sunlight. This ice could
supply drinking water, breathable oxygen, and rocket fuel for future
missions. But it is buried 5 metres below the surface, invisible to
optical cameras, and difficult to distinguish from rocky terrain even
with radar. Five challenges must be solved simultaneously: detect the
ice, separate it from rocks, find a safe landing zone, plan a feasible
rover route, and quantify how much water is actually accessible.


Our Pipeline
Chandrayaan-2 DFSAR + OHRC Data
            ↓
      Preprocessing
   (calibration · normalization)
            ↓
     Ice Detection ⭐ CORE
   (CPR + DOP · Sigmoid fusion)
            ↓
    Terrain Analysis
   (roughness · boulders · illumination)
            ↓
  Landing Site Selection
   (4-factor weighted scoring)
            ↓
   Rover Path Planning
   (A* · solar-power constraint)
            ↓
  Resource Quantification
   (volume · mass · habitat duration)
            ↓
  Mission Intelligence Package

Key Results
OutputValueLanding site89.680°S, 53.746°ESlope0.1°Illumination98%Ice target ε′≈ 4.05 (ice-consistent)TraverseA* optimized · staged · charging haltsHabitat supportConservative to optimistic scenarios

Data Used
DatasetPurposeChandrayaan-2 DFSARSubsurface ice (CPR + DOP)Chandrayaan-2 OHRCSurface morphology · illuminationLOLA DEMSlope · terrain — build phase

Tech Stack
Python · NumPy · SciPy · Matplotlib
Pillow · Rasterio · Scikit-Image · Heapq
Platform: Google Colab · GitHub
Cost: ₹0 (100% open-source)


Scientific Honesty
OHRC detects shadow only — not ice directly
Ice confirmation requires DFSAR CPR/DOP analysis
Brightness-gradient ≠ slope in degrees (needs LOLA DEM)
All browse images are proxies, not calibrated products
Every threshold stated · every assumption cited



Repository Structure
├── outputs/     → PNG maps and analysis figures
├── notebooks/   → Colab pipeline notebooks
├── src/         → Python source modules
├── docs/        → SVG diagrams and proposal
└── data/        → OHRC and DFSAR browse images


References
Spudis et al. 2010 — DFSAR penetration depth (5 m)
Colaprete et al. 2010 — LCROSS ice fraction (5–10%)
Ulaby et al. — Pure ice dielectric ε′ ≈ 3.1
NASA ECLSS — Water baseline 1,500 kg/person/year


Team
Voyagers of Shadows
Multidisciplinary engineering students — mechanical engineering
and programming — passionate about lunar exploration.
Bharatiya Antariksh Hackathon 2026 · Problem Statement 8


Prototype output — our processing. Generated from Chandrayaan-2
DFSAR and OHRC data. All results are preliminary and subject to
full CPR/DOP calibrated-data confirmation.
