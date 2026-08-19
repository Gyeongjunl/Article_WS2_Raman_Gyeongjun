"""
compose_figures.py
Assemble the final multi-panel Figure 1, Figure 2, and Figure 3 PNGs for
main.tex. Pure image layout (no new data plotting) -- matches the panel
selection confirmed in "Figures for an article raman 20260804.pptx" (v3 of
Figure 2 and Figure 3).

Figure 1 (a,b,c,d):
  (a) figures/fig1a.png   -- hand-drawn schematic (static asset, transparent bg)
  (b) figures/fig1b.png   -- optical image, PPT-composited (static asset)
  (c) ../Analysis/Raman_non_encap/output/figures/plot_reference_single__stokes_298.15K.png
  (d) ../Analysis/PL_encap/output/figures/plot_reference_single__PL_5K.png
  (a),(b) are manual art, not analysis output -- never regenerated here.
  (c),(d) are pulled fresh from Analysis/ output every run.

Figure 2 (a,b,c):
  (a) ../Analysis/Raman_non_encap/output/figures/plot_raman__2Dmap_zoom_bgsub.png
  (b) ../Analysis/Raman_encap/output/figures/plot_raman__2Dmap_zoom.png
  (c) ../Analysis/Raman_encap/output/figures/fit_A1g__position_vs_T_encap_vs_nonencap.png
  NOTE: use the plain (non "_swapped") (a)/(b) filenames -- the "_swapped"
  ones have the opposite axis convention (energy/temperature transposed)
  from what's actually used in the paper; that mismatch cost a full review
  cycle to catch (2026-08-11).

Figure 3 (a,b):
  (a) ../Analysis/PL_encap/output/figures/plot_PL_3D_waterfall__waterfall.png
  (b) ../Analysis/PL_encap/output/figures/plot_PL__E0_model_Passler.png

Run from within Article_WS2_Raman_Gyeongjun/ (relative paths below assume this).

Output:
  figures/fig1.png
  figures/fig2.png
  figures/fig3.png
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Panel labels (a)(b)(c)(d) use Arial to match the rest of each plot (set by
# Analysis/plot_style.py's apply_origin_style, which this script doesn't call
# since it only composites pre-rendered PNGs). Peak-name annotations use STIX
# mathtext for a serif/formula look, also matching the rest of the figures.
plt.rcParams["font.family"] = "Arial"
plt.rcParams["mathtext.fontset"] = "stix"

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "..", "Analysis")
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

LABEL_FS = 15
LABEL_PAD = 0.006


def imshow_fill(ax, img_path):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.axis("off")


def place_label(fig, pos, label, pad_x=LABEL_PAD, pad_y=LABEL_PAD, fontsize=LABEL_FS):
    fig.text(pos.x0 + pad_x, pos.y1 - pad_y, label, transform=fig.transFigure,
              fontsize=fontsize, fontweight="bold", color="black", ha="left", va="top")


# main.tex places every composed figure at \includegraphics[width=\linewidth]
# -- same target print width for all three -- so a panel label at a fixed
# LABEL_FS pt in matplotlib does NOT come out the same size on the printed
# page across fig1/fig2/fig3: each composed PNG's native width (after
# bbox_inches="tight" cropping) differs, so \linewidth scales each by a
# different factor. fig1 (narrowest native width) is used as the reference;
# fig2/fig3's source fontsize is scaled UP by their own native-width ratio to
# fig1's, so all three read as the same size once placed at \linewidth.
# Native widths measured directly from the saved PNGs (PIL .size / dpi):
#   fig1: 10.273in   fig2: 12.613in   fig3: 13.053in
_FIG1_NATIVE_W_IN = 10.273
FIG1_LABEL_FS = LABEL_FS
FIG2_LABEL_FS = LABEL_FS * (12.613 / _FIG1_NATIVE_W_IN)
FIG3_LABEL_FS = LABEL_FS * (13.053 / _FIG1_NATIVE_W_IN)


# =============================================================================
# Figure 1 -- 2x2 grid. (a) schematic top-left, (b) optical image bottom-left
# (both static assets, untouched), (c) Raman reference top-right, (d) PL
# reference bottom-right (both regenerated fresh from Analysis/ output).
# fig1a.png has a transparent background -- white figure facecolor shows
# through it.
#
# Label alignment: panel images have different aspect ratios, and imshow's
# default aspect="equal" shrinks each axes' own box to preserve the image's
# proportions (letterboxing) -- so a label placed with ax.transAxes drifts
# per panel and (a)/(c), (b)/(d) end up at different heights. Fix: capture
# each axes' bounding box right after add_subplot (the fixed gridspec cell,
# before imshow shrinks it) and place labels against that with
# fig.transFigure instead -- guarantees (a)/(c) same y, (b)/(d) same y,
# (a)/(b) same x, (c)/(d) same x, by construction of the grid itself.
# =============================================================================
fig1 = plt.figure(figsize=(13, 8), facecolor="white")
gs1 = fig1.add_gridspec(2, 2, hspace=0.03, wspace=0.03)
ax1a = fig1.add_subplot(gs1[0, 0]); pos_a = ax1a.get_position()
ax1b = fig1.add_subplot(gs1[1, 0]); pos_b = ax1b.get_position()
ax1c = fig1.add_subplot(gs1[0, 1]); pos_c = ax1c.get_position()
ax1d = fig1.add_subplot(gs1[1, 1]); pos_d = ax1d.get_position()
for ax in (ax1a, ax1b, ax1c, ax1d):
    ax.set_facecolor("white")
imshow_fill(ax1a, f"{OUT}/fig1a.png")
imshow_fill(ax1b, f"{OUT}/fig1b.png")
imshow_fill(ax1c, f"{BASE}/Raman_non_encap/output/figures/plot_reference_single__stokes_298.15K.png")
imshow_fill(ax1d, f"{BASE}/PL_encap/output/figures/plot_reference_single__PL_5K.png")

FIG1_LABEL_PAD_X = {"(a)": LABEL_PAD, "(b)": LABEL_PAD, "(c)": -0.014, "(d)": -0.014}
for pos, label in [(pos_a, "(a)"), (pos_b, "(b)"), (pos_c, "(c)"), (pos_d, "(d)")]:
    place_label(fig1, pos, label, pad_x=FIG1_LABEL_PAD_X[label], fontsize=FIG1_LABEL_FS)

fig1.savefig(f"{OUT}/fig1.png", dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved -> {OUT}/fig1.png")

# =============================================================================
# Figure 2 -- (a),(b) top row; (c) bottom row, centered.
#
# Each panel's true pixel aspect ratio is preserved (no stretching). All
# three are sized from ONE shared ROW_HEIGHT_IN via their own aspect ratio
# (same approach as Figure 1/3) -- NOT via a gridspec with equal-height cells,
# because (a)/(b) (aspect ~1.44) and (c) (aspect ~1.24, a plain line plot)
# don't share an aspect ratio, so equal-height *cells* with default
# letterboxing left (c) visibly taller than (a)/(b) (whichever cell edge
# their own aspect happened to be constrained by). Explicit sizing makes the
# three panels' displayed heights identical by construction, not by luck.
#
# Peak-name labels are placed in DATA coordinates (raw image pixel columns/
# rows), not axes-fraction -- transAxes would be relative to the axes box,
# which is no longer the image's own letterboxed subregion once each axes is
# sized to exactly match its image (zero letterbox), but data coordinates
# always follow the image regardless. Plot-box pixel bounds measured directly
# from each raw source image:
#   non_encap: img 1999x1388, box x:[303,1737] y:[27,1169]
#   encap:     img 2005x1388, box x:[303,1701] y:[30,1169]
# col(v) = box_x0 + (v-250)/250*(box_x1-box_x0) for data value v in cm-1.
# Small pixel offsets below are leftward nudges applied during review.
# =============================================================================
ASPECT_2A = 1999 / 1388
ASPECT_2B = 2005 / 1388
ASPECT_2C = 1825 / 1469  # fit_A1g__position_vs_T_encap_vs_nonencap.png

ROW_HEIGHT_IN = 4.2  # shared true display height for (a),(b),(c)
GAP_X = 0.3
LEFT_MARGIN = 0.6
TOP_MARGIN = 0.3
ROW_GAP = 0.3
BOTTOM_MARGIN = 0.3

width_2a = ROW_HEIGHT_IN * ASPECT_2A
width_2b = ROW_HEIGHT_IN * ASPECT_2B
width_2c = ROW_HEIGHT_IN * ASPECT_2C
top_row_width = width_2a + GAP_X + width_2b
FIG2_W_IN = LEFT_MARGIN + top_row_width + LEFT_MARGIN
FIG2_H_IN = TOP_MARGIN + ROW_HEIGHT_IN + ROW_GAP + ROW_HEIGHT_IN + BOTTOM_MARGIN

fig2 = plt.figure(figsize=(FIG2_W_IN, FIG2_H_IN), facecolor="white")
a_x0_in = LEFT_MARGIN
b_x0_in = LEFT_MARGIN + width_2a + GAP_X
c_x0_in = (FIG2_W_IN - width_2c) / 2
row_top_y0_in = BOTTOM_MARGIN + ROW_HEIGHT_IN + ROW_GAP
row_bottom_y0_in = BOTTOM_MARGIN

ax_a = fig2.add_axes([a_x0_in / FIG2_W_IN, row_top_y0_in / FIG2_H_IN,
                       width_2a / FIG2_W_IN, ROW_HEIGHT_IN / FIG2_H_IN])
ax_b = fig2.add_axes([b_x0_in / FIG2_W_IN, row_top_y0_in / FIG2_H_IN,
                       width_2b / FIG2_W_IN, ROW_HEIGHT_IN / FIG2_H_IN])
ax_c = fig2.add_axes([c_x0_in / FIG2_W_IN, row_bottom_y0_in / FIG2_H_IN,
                       width_2c / FIG2_W_IN, ROW_HEIGHT_IN / FIG2_H_IN])
pos_a = ax_a.get_position()
pos_b = ax_b.get_position()
pos_c = ax_c.get_position()
for ax in (ax_a, ax_b, ax_c):
    ax.set_facecolor("white")
imshow_fill(ax_a, f"{BASE}/Raman_non_encap/output/figures/plot_raman__2Dmap_zoom_bgsub.png")
imshow_fill(ax_b, f"{BASE}/Raman_encap/output/figures/plot_raman__2Dmap_zoom.png")
imshow_fill(ax_c, f"{BASE}/Raman_encap/output/figures/fit_A1g__position_vs_T_encap_vs_nonencap.png")

NON_ENCAP_BOX = dict(x0=303, x1=1737, y0=27, y1=1169)
ENCAP_BOX = dict(x0=303, x1=1701, y0=30, y1=1169)


def col_for(box, v):
    return box["x0"] + (v - 250) / 250 * (box["x1"] - box["x0"])


E2G_COL = {"a": col_for(NON_ENCAP_BOX, 345) - 100, "b": col_for(ENCAP_BOX, 345) - 60}
A1G_COL = {"a": col_for(NON_ENCAP_BOX, 415) - 130, "b": col_for(ENCAP_BOX, 415) - 60}
E2G_ROW = {"a": NON_ENCAP_BOX["y0"] + 0.07 * (NON_ENCAP_BOX["y1"] - NON_ENCAP_BOX["y0"]),
           "b": ENCAP_BOX["y0"] + 0.50 * (ENCAP_BOX["y1"] - ENCAP_BOX["y0"])}
for ax, key in [(ax_a, "a"), (ax_b, "b")]:
    ax.text(E2G_COL[key], E2G_ROW[key], r"$E_{2g}^1 + 2LA$", color="white",
             fontsize=15, ha="center", va="center")
    ax.text(A1G_COL[key], E2G_ROW[key], r"$A_{1g}$", color="gold",
             fontsize=15, ha="center", va="center")
place_label(fig2, pos_a, "(a)", fontsize=FIG2_LABEL_FS)
place_label(fig2, pos_b, "(b)", fontsize=FIG2_LABEL_FS)
place_label(fig2, pos_c, "(c)", fontsize=FIG2_LABEL_FS)
fig2.savefig(f"{OUT}/fig2.png", dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved -> {OUT}/fig2.png")

# =============================================================================
# Figure 3 -- 1x2. Both (a) and (b)'s true pixel aspect ratios are preserved
# (no stretching). (a)'s column width is derived so that its top-spine-to-
# bottom-spine span, at the resulting scale, is IN INCHES IDENTICAL to (b)'s
# own top-spine-to-bottom-spine span at (b)'s fixed width -- only then can
# both the top line AND the bottom line align simultaneously without
# distorting either image (matching only one of the two, as done in an
# earlier pass, leaves the other off since a single rigid shift can't fix
# a scale mismatch).
#
# Both (a) and (b) are axis("off") raster images -- get_position() on either
# axes returns the FULL IMAGE's bounding box (including that image's own
# internal margins), NOT the visible plot's frame lines. So the real anchor
# rows were measured directly from each raw source image:
#   (a) in plot_PL_3D_waterfall__waterfall.png (2195x1425):
#       top="1" label/back-top frame row 118, bottom=floor front-edge row 1258
#   (b) in plot_PL__E0_model_Passler.png (1139x945):
#       top-spine row 18, bottom-spine (x-axis) row 809
# Verified post-hoc via the actual transData->transFigure transform (not
# hand-computed fractions -- those were off, more than once).
# =============================================================================
A_TOP_ROW, A_BOTTOM_ROW = 118, 1258  # 118 leaves room for the "1" tick label/break glyph above the row-137 frame line;
# 1258 (not 1239, which is a tick mark, not the box edge) is the true floor
# front-edge row, verified by sampling near-black-pixel extent at several
# columns in the middle of the plot (cols 500/900/1100/1300 all end at 1258)
A_BOTTOM_ROW_FULL = 1405  # extends past the frame line to include the x-axis
# tick numbers ("1.5"..."2.1") and "Photon Energy (eV)" title, which sit
# below row 1258 and would otherwise be cropped out entirely.
RAW_A_W = 2195  # plot_PL_3D_waterfall__waterfall.png width
B_TOP_ROW, B_BOTTOM_ROW = 18, 809  # top/bottom spine rows in plot_PL__E0_model_Passler.png
RAW_B_W, RAW_B_H = 1139, 945

FIG3_H_IN = 5.5
B_WIDTH_IN = 5.35   # panel (b) kept at its original width -- this fixes the shared scale
GAP_IN = 0.35
TOP_ANCHOR = 0.92   # figure-fraction where both panels' top-spine row lands

SCALE_B = B_WIDTH_IN / RAW_B_W
TARGET_SPAN_IN = SCALE_B * (B_BOTTOM_ROW - B_TOP_ROW)          # (b)'s true top-to-bottom span, in inches
SCALE_A = TARGET_SPAN_IN / (A_BOTTOM_ROW - A_TOP_ROW)            # scale for (a) that matches that span
A_WIDTH_IN = SCALE_A * RAW_A_W
A_FULL_HEIGHT_IN = SCALE_A * (A_BOTTOM_ROW_FULL - A_TOP_ROW)
B_FULL_HEIGHT_IN = SCALE_B * RAW_B_H
FIG3_W_IN = A_WIDTH_IN + GAP_IN + B_WIDTH_IN + 1.0  # +1.0in slack margin; bbox_inches="tight" trims the rest

fig3 = plt.figure(figsize=(FIG3_W_IN, FIG3_H_IN), facecolor="white")
a_x0 = 0.5 / FIG3_W_IN
a_w = A_WIDTH_IN / FIG3_W_IN
a_y1 = TOP_ANCHOR  # A_TOP_ROW is the ylim top -> lands exactly at the axes box top
a_y0 = a_y1 - A_FULL_HEIGHT_IN / FIG3_H_IN

b_x0 = (0.5 + A_WIDTH_IN + GAP_IN) / FIG3_W_IN
b_w = B_WIDTH_IN / FIG3_W_IN
# row 0 of (b) is at the box top; B_TOP_ROW=18 sits slightly below that, so
# nudge the box top up so row=18 (not row=0) lands at TOP_ANCHOR
b_y1 = TOP_ANCHOR + (B_TOP_ROW * SCALE_B) / FIG3_H_IN
b_y0 = b_y1 - B_FULL_HEIGHT_IN / FIG3_H_IN

ax3a = fig3.add_axes([a_x0, a_y0, a_w, a_y1 - a_y0])
ax3b = fig3.add_axes([b_x0, b_y0, b_w, b_y1 - b_y0])
for ax in (ax3a, ax3b):
    ax.set_facecolor("white")
    ax.axis("off")
imshow_fill(ax3a, f"{BASE}/PL_encap/output/figures/plot_PL_3D_waterfall__waterfall.png")
imshow_fill(ax3b, f"{BASE}/PL_encap/output/figures/plot_PL__E0_model_Passler.png")
ax3a.set_ylim(A_BOTTOM_ROW_FULL, A_TOP_ROW)  # crop to include the label margin; aspect stays "equal" -- no stretch
ax3b.set_ylim(RAW_B_H, 0)  # full (b) image, no crop

pos3a = ax3a.get_position()
pos3b = ax3b.get_position()
place_label(fig3, pos3a, "(a)", fontsize=FIG3_LABEL_FS)
place_label(fig3, pos3b, "(b)", fontsize=FIG3_LABEL_FS)
fig3.savefig(f"{OUT}/fig3.png", dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved -> {OUT}/fig3.png")
