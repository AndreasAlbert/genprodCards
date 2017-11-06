#!/usr/bin/env python

masswidth = (
  (115, 0.00312),
  (120, 0.00351),
  (124, 0.00394),
  (125, 0.00407),
  (126, 0.00421),
  (130, 0.00491),
  (135, 0.00618),
  (140, 0.00817),
  (145, 0.0114),
  (150, 0.0173),
  (155, 0.0309),
  (160, 0.0831),
  (165, 0.246),
  (170, 0.38),
  (175, 0.501),
  (180, 0.631),
  (190, 1.04),
  (200, 1.43),
  (210, 1.85),
  (230, 2.82),
  (250, 4.04),
  (270, 5.55),
  (300, 8.43),
  (350, 15.2),
  (400, 29.2),
  (450, 46.8),
  (500, 68.0),
  (550, 93.0),
  (600, 123.0),
  (700, 199.0),
  (750, 247.0),
  (800, 304.0),
  (900, 449.0),
  (1000, 647.0),
  (1500, 750.0),
  (2000, 1000.0),
  (2500, 1250.0),
  (3000, 1500.0),
)

with open("HWJ_HanythingJ_NNPDF31_13TeV_template.input") as f:
  template = f.read()

for mass, width in masswidth:
  for sign, W in ("plus", 24), ("minus", -24):
    with open("HW{}J_HanythingJ_NNPDF31_13TeV_M{}.input".format(sign, mass), "w") as f:
      f.write(template.format(mass=mass, width=width, W=W))
