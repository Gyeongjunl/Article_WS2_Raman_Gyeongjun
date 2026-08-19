# Figure Proposition
## Optical Thermometry in Monolayer WS₂ from 5 K to 1273 K

---

## MAIN TEXT FIGURES

---

### Figure 1 — Platform Overview and Reference Spectra

**Purpose:** Introduce the experimental setup and show sample quality.

**Layout:** 2×2 panel

**Panels:**

**(a) Schematic of the platform**
- hBN/WS₂/hBN stack on SiC membrane + cryostat integration
- Temperature arrow (5 K → 1273 K)
- Style: clean vector illustration (adapted from SPE paper Fig 1(a))

**(b) Optical image of sample on membrane**
- White-light image of encapsulated WS₂ flake on SiC membrane
- Scale bar: 10 µm; dashed circle: laser spot
- Source: existing optical image from experiment

**(c) Reference Raman spectrum at RT (non-encapsulated)**
- x-axis: Raman shift (cm⁻¹), range 300–470 cm⁻¹
- Both Stokes and anti-Stokes; labeled E₂g+2LA (~355 cm⁻¹) and A₁g (~417 cm⁻¹)
- Source: `raman first heat up 25C to 1000C.dat` (RT) or `Figure/reference raman at 298_15K.dat`

**(d) Reference PL spectrum at 5 K (encapsulated)**
- x-axis: Energy (eV), range 1.92–2.10 eV
- Labeled peaks: X⁰, trion, dark exciton; FWHM annotation on X⁰
- Source: `Analysis/spectra_fit_data/spectrum_5.15K.dat`

**Key message:** Two complementary samples; non-encap for Raman, encap for PL + Raman.

---

### Figure 2 — Raman Thermal Indicator: Non-encapsulated and hBN-encapsulated

**Purpose:** Establish the linear Raman thermometer using the clean non-encap dataset,
then show the encap sample reproduces the same linear trend while revealing an
intensity evolution/crossover across the full temperature range.

**Layout:** 2×2 panel

**Panels:**

**(a) 2D Raman intensity map — non-encapsulated, RT to 1000°C**
- x-axis: Raman shift (cm⁻¹), range 330–450 cm⁻¹
- y-axis: Temperature (°C or K), RT to 1000°C
- Color: Raman intensity (log scale or linear, plasma or viridis colormap)
- Dashed lines tracking E₂g+2LA and A₁g peak positions (redshift visible)
- Horizontal dashed line at ~1000°C: dissociation threshold
- Source: `raman first heat up 25C to 1000C.dat`

**(b) A₁g peak position vs T — non-encapsulated**
- x-axis: Temperature (K), 300–1273 K
- y-axis: ω_A₁g (cm⁻¹)
- Black filled circles: experimental data
- Red solid line: linear fit, slope = −0.0134 cm⁻¹/K labeled
- Grey shaded region: T > 1273 K (dissociation zone)
- Source: fit peaks from `analyze_cooling.py` output

**(c) 2D Raman intensity map — hBN-encapsulated, 5 K to 1000°C**
- x-axis: Raman shift (cm⁻¹), range 330–450 cm⁻¹
- y-axis: Temperature (K), 5 K to ~1273 K
- Color: Raman intensity (log scale, same colormap as (a))
- Key features to annotate:
  - LT region (5–100 K): E₂g+2LA dominant
  - Intermediate region: both peaks weak (missing points region)
  - HT region: A₁g > E₂g+2LA (intensity crossover)
- Dashed lines tracking peak positions where visible
- Source: `raman LT heat up 5K to 295K.dat` (LT) + `raman first cooldown from 1000C to 25C_bg_subtracted.dat` (HT)
- Existing: `Figure/Raman_LT_map.png`

**(d) A₁g peak position vs T — encapsulated + non-encap linear fit overlay**
- x-axis: Temperature (K), 5–1273 K
- y-axis: ω_A₁g (cm⁻¹)
- Open symbols: encap data (LT + HT, with gaps where signal lost)
- Red solid line: linear fit from non-encap (b) — same slope
- Grey shaded region: T > 1273 K
- Note: This same encap sample was used for simultaneous PL measurements (Fig 3)
- Source: `raman LT heat up 5K to 295K.dat` + HT encap dat

**Key message:** Clean linear redshift from RT to 1000°C in non-encap (a,b);
encap sample (c,d) shows the same linear trend while its intensity evolution
reveals E₂g↔A₁g competition across temperature; Raman and PL measured simultaneously
on the encap sample.

---

### Figure 3 — PL Thermal Indicator

**Purpose:** Show the rich temperature-dependent PL response as a comprehensive thermal indicator.

**Layout:** 2×2 panel

**Panels:**

**(a) PL 2D color map**
- x-axis: Energy (eV), range 1.55–2.10 eV
- y-axis: Temperature (K), 5–1273 K
- Color: PL intensity (log scale, viridis or plasma)
- Annotate: X⁰ peak track (white dashed curve)
- Mark: blackbody onset above 925 K; dissociation at 1273 K
- Source: `PL spec 5K to 1273K overall.dat`
- Existing: `PL_2Dmap.png`

**(b) E₀(T) neutral exciton peak energy**
- x-axis: Temperature (K), 5–1273 K
- y-axis: E₀ (eV), 1.68–2.06 eV
- Symbols with error bars: Voigt fit results from `PL_voigt_fit_results.csv`
- Blue solid line: Pässler model fit
- Grey shading: T > 925 K (blackbody region)
- Source: `PL_voigt_fit_results.csv` + `Analysis/PL_E0_vs_T.dat`
- Existing: `Analysis/PL_E0_model_fits.png`

**(c) Spectral linewidth decomposition**
- x-axis: Temperature (K), 5–925 K
- y-axis: FWHM (meV)
- Black: total Voigt FWHM; Blue: Γ_G; Red: Γ_L
- Vertical dashed line at crossover T (~200 K)
- Source: `PL_voigt_fit_results.csv`
- Existing: `PL_FWHM_vs_T.png`

**(d) η and integrated intensity vs T**
- Lorentzian fraction η (top) + integrated intensity log scale (bottom)
- Shared x-axis 5–925 K
- Source: `PL_voigt_fit_results.csv`
- Existing: `PL_eta_vs_T.png`, `PL_integrated_intensity.png`

**Key message:** PL encodes temperature in four observables; Pässler calibration 5 K–1273 K;
lineshape crossover at ~200 K.

---

## SUPPORTING INFORMATION FIGURES

---

### Figure S1 — Bandgap Model Comparison

**(a)** E₀(T) data + three model fits (Varshni dashed red, Pässler solid blue, O'Donnell–Chen dash-dot orange)

**(b)** Residuals (data − model) in meV — Varshni fails at low T

Source: `Analysis/PL_E0_model_fits.png`, `Analysis/PL_E0_model_residuals.png`

---

### Figure S2 — Voigt Fit Quality Grid

3×3 grid at representative temperatures (5 K, 40 K, 100 K, 200 K, 295 K, 500 K, 700 K, 873 K, 925 K).
Each panel: raw spectrum + Voigt fit + Gaussian/Lorentzian components + residual.

Source: `Analysis/spectra_fit_data/spectrum_*.dat`

---

### Figure S3 — Blackbody Calibration

**(a)** Blackbody emission spectra at T > 925 K + Planck fits

**(b)** Agreement between PL (Pässler) and blackbody temperatures at 925 K (±5 K)

Source: `Article_WS2_SPE_Gyeongjun/Data/Figure S5_a_black body.xlsx`

---

### Figure S4 — Thermal Dissociation Optical Images

Before and after 1200°C annealing. WS₂ monolayer disappears.

---

## COLOR AND STYLE NOTES

- Journal: ACS (ACS Nano or similar)
- Font: Arial, 8–9 pt in-panel labels, 10 pt axis labels
- Colors:
  - Temperature colormap: plasma or RdYlBu_r (consistent across Fig 2(a), Fig 2(c), Fig 3(a))
  - Non-encap Raman: filled black symbols
  - Encap Raman: open symbols
  - Pässler fit: blue; Varshni: red; O'Donnell–Chen: orange
- Tick marks: inward, all 4 sides; box frame

## DATA SOURCES SUMMARY

| Figure | Panel | Data file |
|--------|-------|-----------|
| Fig 1c | Raman RT (non-encap) | `raman first heat up 25C to 1000C.dat` or `Figure/reference raman at 298_15K.dat` |
| Fig 1d | PL 5K (encap) | `Analysis/spectra_fit_data/spectrum_5.15K.dat` |
| Fig 2a | Raman 2D map (non-encap) | `raman first heat up 25C to 1000C.dat` |
| Fig 2b | A₁g position (non-encap) | fit peaks from `analyze_cooling.py` |
| Fig 2c | Raman 2D map (encap) | `raman LT heat up 5K to 295K.dat` + HT encap dat |
| Fig 2d | A₁g position (encap) | same + non-encap linear fit overlay |
| Fig 3a | PL color map | `PL spec 5K to 1273K overall.dat` |
| Fig 3b | E₀(T) | `PL_voigt_fit_results.csv` |
| Fig 3c,d | FWHM, η, intensity | `PL_voigt_fit_results.csv` |
| SI S1 | Model comparison | `Analysis/PL_E0_model_*.png` |
| SI S2 | Fit grid | `Analysis/spectra_fit_data/*.dat` |
| SI S3 | Blackbody | `Article_WS2_SPE.../Data/Figure S5*.xlsx` |

## THINGS TO RESOLVE BEFORE FIGURE FINALIZATION

1. **High-T Voigt fit issues**: ~~Points at 473 K, 623 K, 673 K, 1073 K, 1173 K show η = 1.0
   or FWHM_G ≈ 0.~~ Addressed in `Analysis/PL_encap/fit_PL.py` (sep-parametrized
   double Voigt + per-temperature data-derived sigma/gamma bounds instead of a
   fixed/chained cap). Re-run `fit_PL.py` then `plot_PL_linewidth_eta.py` and
   spot-check `fit_PL__fit_quality_grid.png` before finalizing Fig 3c/3d.

2. **E₂g+2LA slope**: Extract from Raman fit and fill [TBD] in main.tex.

3. **Pässler fit parameters**: Run `fit_E0_models.py` and fill Table S1 + [TBD] in main.tex.

4. **Encap Raman intensity crossover**: Physical origin of E₂g↔A₁g competition vs T
   needs further investigation before writing caption for Fig 2(c).

5. **Figure 1(a) schematic**: Vector illustration needed (or adapt from SPE paper).

6. **Figure 1(b) optical image**: Locate best optical image of sample on membrane.

7. **Confirm data files**: Verify which .dat files are Exp 1 (non-encap) vs Exp 2 (encap).
