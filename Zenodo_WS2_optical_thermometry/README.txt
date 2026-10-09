Data for: Optical Thermometry in Monolayer WS2: Raman and Photoluminescence
Spectroscopy from 5 K to 1273 K

G. Lee, A. Borel, T. Taniguchi, K. Watanabe, F. Sirotti, F. Cadiz
Laboratoire de Physique de la Matiere Condensee, CNRS, Ecole polytechnique,
Institut Polytechnique de Paris, 91120 Palaiseau, France
(hBN crystals: T. Taniguchi and K. Watanabe, NIMS, Tsukuba, Japan)

All files are tab-separated plain text with one header line giving the column
names and units. Temperatures are in K, Raman shifts in cm-1, photon energies
in eV and intensities in arbitrary units (a.u.).


SAMPLES AND MEASUREMENTS
------------------------
- Non-encapsulated sample: monolayer WS2 exfoliated onto the suspended SiC
  membrane of a micro-heater chip (EDEN Instruments). Raman only, 298-1273 K,
  under vacuum. The WS2 Raman signal is last observed at 1223 K; at 1273 K the
  monolayer has dissociated.
- hBN-encapsulated sample: hBN/WS2/hBN heterostructure on a second membrane
  chip. Raman and photoluminescence (PL), 5-1273 K. Raman measurement
  sequence: LT (5-295 K, cryostat), then 1st heat-up (293-1273 K), cooldown
  (1273-298 K) and 2nd heat-up (298-1023 K) on the micro-heater. The column
  "run" in the figure files uses these names.
- Temperature: 5 K to room temperature in a He-flow cryostat (cryostat heater,
  calibrated Cernox thermometer on the sample holder); room temperature to
  1273 K by Joule heating of the SiC membrane under vacuum, using the
  manufacturer's current-to-temperature calibration.
- Excitation: 514.5 nm cw laser, ~1 mW for Raman, <= 10 uW for PL, ~1 um spot,
  objective NA 0.82, grating spectrometer with Peltier-cooled CCD.
- raw/ Raman spectra are as recorded. raw/ PL spectra are as recorded, except
  that at high temperature the thermal emission of the heated membrane,
  measured with the laser blocked, has been subtracted.


raw/  MEASURED SPECTRA
----------------------
PL_encap_5-1273K.txt
    T(K), Energy(eV), PL_intensity(a.u.). Long format: the spectrometer was
    re-centred as the emission shifted, so each temperature has its own energy
    axis. 39 temperature steps.
    NOTE: the 1073 K step is excluded from all analyses in the paper. Although
    the heater current was increased from the 1023 K step, its X_A^0 peak did
    not shift, and it has the lowest signal-to-noise ratio of the
    high-temperature spectra, so a reliable temperature cannot be assigned to
    it (SI Sec. S4).
Raman_encap_LT_5-295K.txt              LT (cryostat), 15 temperatures
Raman_encap_heatup1_293-1273K.txt      1st heat-up on the micro-heater
Raman_encap_cooldown_1273-298K.txt     cooldown after the 1st heat-up
Raman_encap_heatup2_298-1023K.txt      2nd heat-up
Raman_nonencap_298-1273K.txt           non-encapsulated sample, 21 temperatures
    Raman_shift(cm-1) followed by one intensity column per temperature.
    Negative shifts are the anti-Stokes side.


figures/  VALUES PLOTTED IN EACH FIGURE
---------------------------------------
Fig1c_Raman_nonencap_298K.txt
    Non-encapsulated Raman spectrum at 298 K, background subtracted.
Fig1c_fit_peaks.txt, Fig1c_fit_curves.txt
    Lorentzian fit of the 298 K spectrum (ten peaks plus a constant offset,
    210-620 cm-1), red curves in Fig. 1(c).
Fig1d_PL_encap_5K.txt
    Encapsulated PL spectrum at 5.15 K.
Fig2a_Raman_map_nonencap.txt
    Non-encapsulated Raman spectra, background subtracted. Fig. 2(a) shows the
    250-500 cm-1 range.
Fig2b_FigS2a_Raman_map_encap.txt
    Encapsulated Raman spectra, background subtracted: 5-295 K from the
    LT run and 298-1273 K from the cooldown run.
Fig2c_FigS2b_A1g_position_vs_T.txt
    A1g(Gamma) peak position and fit uncertainty for both samples. SI Fig.
    S2(b) shows the encapsulated data by run.
Fig2c_A1g_linear_fits.txt
    Linear fits of the A1g position for T >= 100 K.
Fig3a_FigS3a_PL_spectra_normalized.txt
    PL spectra at all 38 temperatures (1073 K omitted), each normalized to
    its own maximum. Fig. 3(a) shows ten of them; SI Fig. S3(a) shows all of
    them as a map.
Fig3b_FigS3b_E0_vs_T.txt
    X_A^0 peak energy from Voigt fits (1073 K excluded).
Fig3b_TableS1_bandgap_model_parameters.txt
    Varshni, Passler and O'Donnell-Chen fits to E0(T): model equations and
    best-fit parameters (Table S1).
Fig3b_FigS3b_model_curves.txt
    The three model curves. Fig. 3(b) shows the Passler curve; SI Fig. S3(b)
    shows all three.
Fig3c_FigS5a_FWHM_vs_T.txt
    Total Voigt FWHM of X_A^0 and its fit uncertainty (1073 K excluded).
Fig3c_FigS5a_linewidth_fits.txt
    Linear fit 250-1000 K (Fig. 3(c)), phonon-scattering model 5-1000 K
    (SI Fig. S5(a)) and the 5-100 K slope used for the acoustic-phonon
    coefficient c1. Points above ~1100 K are not used in the fits: the
    low-energy tail of the emission extends beyond the acquisition window.
FigS1_E2g_2LA_positions.txt
    E2g, 2LA and merged E2g+2LA peak positions for both samples.
FigS1_linear_fits.txt
    Linear fits drawn in SI Fig. S1.
FigS4_Voigt_fits.txt
    Normalized PL data and Voigt fits (total, X_A^0 and X^- components) at all
    38 temperatures (1073 K omitted); SI Fig. S4 shows twelve of them. Below
    125 K only X_A^0 is fitted.
FigS5a_phonon_model_curve.txt
    Phonon-scattering model curve of SI Fig. S5(a) (parameters in
    Fig3c_FigS5a_linewidth_fits.txt).
FigS5a_Cadiz2017_literature.txt
    Linewidths reported for hBN-encapsulated WS2 monolayers by Cadiz et al.,
    Phys. Rev. X 7, 021026 (2017), Table I, shown as triangles in SI Fig.
    S5(a) at the midpoint of the quoted ranges.
FigS5b_XA0_integrated_intensity.txt
    Integrated X_A^0 PL intensity (1073 K excluded). Above ~800 K the
    integrated area is not reliable because the broadened peak extends beyond
    the low-energy edge of the fitting window.
FigS7_Raman_mode_intensities.txt
    Integrated intensity of the A1g mode and of the E2g+2LA band, both
    samples. Values are not comparable between the two samples.

SI Fig. S6 shows optical images and is not included.
