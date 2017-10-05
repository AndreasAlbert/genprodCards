import FWCore.ParameterSet.Config as cms
import os
def customise(process):

  slhacontent = """# NMSSMTools OUTPUT IN SLHA FORMAT
# Info about spectrum calculator
BLOCK SPINFO   # Program information
     1   NMSSMTools # Spectrum calculator
     2   3.2.0      # Version number
     8   1          # Higgs mass precision
     3   # Muon magn. mom. more than 2 sigma away
# Input parameters
BLOCK MODSEL
    3     1         # NMSSM PARTICLE CONTENT
BLOCK SMINPUTS
     1     1.27920000E+02   # ALPHA_EM^-1(MZ)
     2     1.16639000E-05   # GF
     3     1.17200000E-01   # ALPHA_S(MZ)
     4     9.11870000E+01   # MZ
     5     4.20000000E+00   # MB(MB)
     6     1.73300000E+02   # MTOP (POLE MASS)
     7     1.77700000E+00   # MTAU
# SMINPUTS Beyond SLHA:
# MW:     0.80420000E+02
# MS:     0.19000000E+00
# MC:     0.14000000E+01
# VUS:     0.22000000E+00
# VCB:     0.40000000E-01
# VUB:     0.40000000E-02
BLOCK MINPAR
     3     2.60000000E+00   # TANBETA(MZ)
BLOCK EXTPAR
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    11     1.15269780E+03   # ATOP
    12     1.15269780E+03   # ABOTTOM
    13     1.15269780E+03   # ATAU
    16     1.15269780E+03   # AMUON
    31     1.00000000E+03   # LEFT SELECTRON
    32     1.00000000E+03   # LEFT SMUON
    33     1.00000000E+03   # LEFT STAU
    34     1.00000000E+03   # RIGHT SELECTRON
    35     1.00000000E+03   # RIGHT SMUON
    36     1.00000000E+03   # RIGHT STAU
    41     1.00000000E+03   # LEFT 1ST GEN. SQUARKS
    42     1.00000000E+03   # LEFT 2ND GEN. SQUARKS
    43     1.00000000E+03   # LEFT 3RD GEN. SQUARKS
    44     1.00000000E+03   # RIGHT U-SQUARKS
    45     1.00000000E+03   # RIGHT C-SQUARKS
    46     1.00000000E+03   # RIGHT T-SQUARKS
    47     1.00000000E+03   # RIGHT D-SQUARKS
    48     1.00000000E+03   # RIGHT S-SQUARKS
    49     1.00000000E+03   # RIGHT B-SQUARKS
    61     6.00000000E-01   # LAMBDA
    62     1.20000000E-01   # KAPPA
    63    -5.10000000E+02   # ALAMBDA
    64     2.59359313E+02   # AKAPPA
    65    -2.00000000E+02   # MUEFF
# 
BLOCK MASS   # Mass spectrum 
#  PDG Code     mass             particle 
        25     2.00000000E+01   # lightest neutral scalar
        35     1.25300000E+02   # second neutral scalar
        45     5.76499640E+02   # third neutral scalar
        36     1.94710599E+02   # lightest pseudoscalar
        46     5.77302004E+02   # second pseudoscalar
        37     5.65383962E+02   # charged Higgs
   1000001     1.03816356E+03   #  ~d_L
   2000001     1.03719659E+03   #  ~d_R
   1000002     1.03601090E+03   #  ~u_L
   2000002     1.03654529E+03   #  ~u_R
   1000003     1.03816356E+03   #  ~s_L
   2000003     1.03719659E+03   #  ~s_R
   1000004     1.03601090E+03   #  ~c_L
   2000004     1.03654529E+03   #  ~c_R
   1000005     1.03575966E+03   #  ~b_1
   2000005     1.03960025E+03   #  ~b_2
   1000006     9.60261936E+02   #  ~t_1
   2000006     1.12701225E+03   #  ~t_2
   1000011     1.00077837E+03   #  ~e_L
   2000011     1.00067504E+03   #  ~e_R
   1000012     9.98544999E+02   #  ~nue_L
   1000013     1.00077837E+03   #  ~mu_L
   2000013     1.00067504E+03   #  ~mu_R
   1000014     9.98544999E+02   #  ~numu_L
   1000015     9.99245569E+02   #  ~tau_1
   2000015     1.00220881E+03   #  ~tau_2
   1000016     9.98544999E+02   #  ~nutau_L
   1000021     1.07902751E+03   #  ~g
   1000022    -9.78138073E+01   # neutralino(1)
   1000023    -2.27083370E+02   # neutralino(2)
   1000025     2.27948047E+02   # neutralino(3)
   1000035     3.03709218E+02   # neutralino(4)
   1000045     6.21809001E+02   # neutralino(5)
   1000024    -2.07786084E+02   # chargino(1)
   1000037     6.21777058E+02   # chargino(2)
# 
# Low energy observables
BLOCK LOWEN
# Exp. 2 Sigma: 3.03E-04 < BR(b -> s gamma) < 4.01E-04:
     1     3.63714683E-04   # BR(b -> s gamma)
    11     4.02139233E-04   # (BR(b -> s gamma)+Theor.Err.)
    12     3.05623742E-04   # (BR(b -> s gamma)-Theor.Err.)
# Exp. 2 Sigma: 4.99E-01 < Delta M_d < 5.15E-01:
     2     6.23721057E-01   # Delta M_d in ps^-1
    21     1.08925949E+00   # Delta M_d +Theor.Err.
    22     1.67319629E-01   # Delta M_d -Theor.Err.
# Exp. 2 Sigma: 1.753E+01 < Delta Ms < 1.801E+01:
     3     2.16090411E+01   # Delta M_s in ps^-1
    31     2.85163999E+01   # Delta M_s +Theor.Err.
    32     1.48347859E+01   # Delta M_s -Theor.Err.
# Exp. 95% C.L.: BR(Bs->mu+mu-) < 4.5E-09:
     4     3.66142274E-09   # BR(Bs -> mu+mu-)
    41     6.21885759E-09   # BR(Bs -> mu+mu-)+Theor.Err.
    42     1.77737621E-09   # BR(Bs -> mu+mu-)-Theor.Err.
# Exp. 2 Sigma: 8.90E-05 < BR(B+ > tau+ + nu_tau) < 2.45E-04:
     5     1.31637610E-04   # BR(B+ -> tau+ + nu_tau)
    51     2.63326712E-04   # BR(B+ -> tau+ + nu_tau) + Theor.Err.
    52     5.68116338E-05   # BR(B+ -> tau+ + nu_tau) - Theor.Err.
# BSM contr. to the muon anomalous magn. moment:
     6    -7.36575244E-11   # Del_a_mu
    61     2.11944894E-10   # Del_a_mu + Theor.Err.
    62    -3.59259943E-10   # Del_a_mu - Theor.Err.
# Minimal Exp.-SM (2 sigma):  8.77306222E-10
# Maximal Exp.-SM (2 sigma):  4.61144414E-09
# 
BLOCK HMIX Q=  1.00000000E+03 # (STOP/SBOTTOM MASSES)
     1    -2.00000000E+02   # MUEFF
     2     2.57525562E+00   # TAN(BETA)
     3     2.41822895E+02   # V(Q)
     4     3.25992325E+05   # MA^2
     5     4.30217611E+04   # MP^2
# 
# 3*3 Higgs mixing
BLOCK NMHMIX
  1  1    -1.10350226E-01   # S_(1,1)
  1  2     9.05942318E-02   # S_(1,2)
  1  3     9.89755279E-01   # S_(1,3)
  2  1     3.71463278E-01   # S_(2,1)
  2  2     9.27429264E-01   # S_(2,2)
  2  3    -4.34740648E-02   # S_(2,3)
  3  1     9.21866509E-01   # S_(3,1)
  3  2    -3.62860367E-01   # S_(3,2)
  3  3     1.35994459E-01   # S_(3,3)
# 
# 3*3 Pseudoscalar Higgs mixing
BLOCK NMAMIX
  1  1     1.41283767E-01   # P_(1,1)
  1  2     5.43399103E-02   # P_(1,2)
  1  3     9.88473214E-01   # P_(1,3)
  2  1     9.22591121E-01   # P_(2,1)
  2  2     3.54842739E-01   # P_(2,2)
  2  3    -1.51395844E-01   # P_(2,3)
# 
# 3rd generation sfermion mixing
BLOCK STOPMIX  # Stop mixing matrix
  1  1    -7.08179172E-01   # Rst_(1,1)
  1  2     7.06032761E-01   # Rst_(1,2)
  2  1    -7.06032761E-01   # Rst_(2,1)
  2  2    -7.08179172E-01   # Rst_(2,2)
BLOCK SBOTMIX  # Sbottom mixing matrix
  1  1    -6.16021600E-01   # Rsb_(1,1)
  1  2     7.87729261E-01   # Rsb_(1,2)
  2  1    -7.87729261E-01   # Rsb_(2,1)
  2  2    -6.16021600E-01   # Rsb_(2,2)
BLOCK STAUMIX  # Stau mixing matrix
  1  1    -6.94668570E-01   # Rsl_(1,1)
  1  2     7.19329950E-01   # Rsl_(1,2)
  2  1    -7.19329950E-01   # Rsl_(2,1)
  2  2    -6.94668570E-01   # Rsl_(2,2)
# 
# Gaugino-Higgsino mixing
BLOCK NMIX  # 5*5 Neutralino Mixing Matrix
  1  1    -4.40029145E-02   # N_(1,1)
  1  2     4.58056753E-02   # N_(1,2)
  1  3    -1.40922328E-02   # N_(1,3)
  1  4     4.28128247E-01   # N_(1,4)
  1  5     9.01372951E-01   # N_(1,5)
  2  1    -6.84791003E-02   # N_(2,1)
  2  2     8.00337876E-02   # N_(2,2)
  2  3    -7.08726134E-01   # N_(2,3)
  2  4     6.22764805E-01   # N_(2,4)
  2  5    -3.14287243E-01   # N_(2,5)
  3  1    -2.00332521E-01   # N_(3,1)
  3  2     6.77415257E-02   # N_(3,2)
  3  3     6.99124361E-01   # N_(3,3)
  3  4     6.16063116E-01   # N_(3,4)
  3  5    -2.94905632E-01   # N_(3,5)
  4  1     9.76225036E-01   # N_(4,1)
  4  2     3.68650304E-02   # N_(4,2)
  4  3     9.32201135E-02   # N_(4,3)
  4  4     1.87574227E-01   # N_(4,4)
  4  5    -4.18517399E-02   # N_(4,5)
  5  1    -1.50305121E-02   # N_(5,1)
  5  2     9.92747948E-01   # N_(5,2)
  5  3     6.61923090E-03   # N_(5,3)
  5  4    -1.18963645E-01   # N_(5,4)
  5  5     5.42516847E-03   # N_(5,5)
# 
BLOCK UMIX  # Chargino U Mixing Matrix
  1  1     9.83153370E-03   # U_(1,1)
  1  2    -9.99951669E-01   # U_(1,2)
  2  1     9.99951669E-01   # U_(2,1)
  2  2     9.83153370E-03   # U_(2,2)
# 
BLOCK VMIX  # Chargino V Mixing Matrix
  1  1     1.67489961E-01   # V_(1,1)
  1  2    -9.85873781E-01   # V_(1,2)
  2  1     9.85873781E-01   # V_(2,1)
  2  2     1.67489961E-01   # V_(2,2)
# 
# Higgs reduced couplings
# (as compared to a SM Higgs with same mass)
BLOCK REDCOUP
# H1
  1  1     9.70639721E-02   # U-type fermions
  1  2    -3.07400158E-01   # D-type fermions
  1  3     4.49423058E-02   # W,Z bosons
  1  4     1.69867382E-01   # Gluons
  1  5     1.68546185E-01   # Photons
# H2
  2  1     9.93661145E-01   # U-type fermions
  2  2     1.03477695E+00   # D-type fermions
  2  3     9.98959574E-01   # W,Z bosons
  2  4     9.95074621E-01   # Gluons
  2  5     9.80819065E-01   # Photons
# H3
  3  1    -3.88773853E-01   # U-type fermions
  3  2     2.56802294E+00   # D-type fermions
  3  3    -7.74333878E-03   # W,Z bosons
  3  4     3.90877509E-01   # Gluons
  3  5     1.62108860E+00   # Photons
# A1
  4  1     5.82205669E-02   # U-type fermions
  4  2     3.93571032E-01   # D-type fermions
  4  3     0.00000000E+00   # W,Z bosons
  4  4     5.05826771E-02   # Gluons
  4  5     3.14481579E-01   # Photons
# A2
  5  1     3.80183649E-01   # U-type fermions
  5  2     2.57004147E+00   # D-type fermions
  5  3     0.00000000E+00   # W,Z bosons
  5  4     3.83961281E-01   # Gluons
  5  5     3.68580223E-01   # Photons
# 
# GAUGE AND YUKAWA COUPLINGS AT THE SUSY SCALE
BLOCK GAUGE Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.62459603E-01   # g1(Q,DR_bar)
     2     6.42566822E-01   # g2(Q,DR_bar)
     3     1.05976273E+00   # g3(Q,DR_bar)
BLOCK YU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     9.25551242E-01   # HTOP(Q,DR_bar)
BLOCK YD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     3.93503665E-02   # HBOT(Q,DR_bar)
BLOCK YE Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     2.78125732E-02   # HTAU(Q,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE SUSY SCALE
BLOCK AU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.15269780E+03   # ATOP
BLOCK AD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.15269780E+03   # ABOT
BLOCK AE Q=  1.00000000E+03 # (SUSY SCALE)
  2  2     1.15269780E+03   # AMUON
  3  3     1.15269780E+03   # ATAU
# 
# SOFT MASSES AT THE SUSY SCALE
BLOCK MSOFT Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    21     2.36941805E+05   # M_HD^2
    22     2.69114655E+04   # M_HU^2
    31     1.00000000E+03   # M_eL
    32     1.00000000E+03   # M_muL
    33     1.00000000E+03   # M_tauL
    34     1.00000000E+03   # M_eR
    35     1.00000000E+03   # M_muR
    36     1.00000000E+03   # M_tauR
    41     1.00000000E+03   # M_q1L
    42     1.00000000E+03   # M_q2L
    43     1.00000000E+03   # M_q3L
    44     1.00000000E+03   # M_uR
    45     1.00000000E+03   # M_cR
    46     1.00000000E+03   # M_tR
    47     1.00000000E+03   # M_dR
    48     1.00000000E+03   # M_sR
    49     1.00000000E+03   # M_bR
# 
# NMSSM SPECIFIC PARAMETERS THE SUSY SCALE
BLOCK NMSSMRUN Q=  1.00000000E+03 # (SUSY SCALE)
     1     6.00000000E-01   # LAMBDA(Q,DR_bar)
     2     1.20000000E-01   # KAPPA(Q,DR_bar)
     3    -5.10000000E+02   # ALAMBDA
     4     2.59359313E+02   # AKAPPA
     5    -2.00000000E+02   # MUEFF
    10     7.12082415E+03   # MS^2
# 
# GAUGE AND YUKAWA COUPLINGS AT THE GUT SCALE
BLOCK GAUGE Q=  1.96152990E+16 # (GUT SCALE)
     1     7.11402404E-01   # g1(MGUT,DR_bar), GUT normalization
     2     7.11402404E-01   # g2(MGUT,DR_bar)
     3     7.02978759E-01   # g3(MGUT,DR_bar)
BLOCK YU Q=  1.96152990E+16 # (GUT SCALE)
  3  3     8.29138699E-01   # HTOP(MGUT,DR_bar)
BLOCK YD Q=  1.96152990E+16 # (GUT SCALE)
  3  3     1.80993069E-02   # HBOT(MGUT,DR_bar)
BLOCK YE Q=  1.96152990E+16 # (GUT SCALE)
  3  3     2.17551441E-02   # HTAU(MGUT,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE GUT SCALE
BLOCK AU Q=  1.96152990E+16 # (GUT SCALE)
  3  3     1.03234207E+04   # ATOP
BLOCK AD Q=  1.96152990E+16 # (GUT SCALE)
  3  3     4.19818532E+03   # ABOT
BLOCK AE Q=  1.96152990E+16 # (GUT SCALE)
  2  2     2.05616818E+03   # AMUON
  3  3     2.08228863E+03   # ATAU
# 
# SOFT MASSES SQUARED AT THE GUT SCALE
BLOCK MSOFT Q=  1.96152990E+16 # (GUT SCALE)
     1     7.30619716E+02   # M1
     2     7.87550057E+02   # M2
     3     4.67970460E+02   # M3
    21     5.50177647E+06   # M_HD^2
    22     4.16715720E+07   # M_HU^2
    31     7.64568214E+05   # M_eL^2
    32     7.64568214E+05   # M_muL^2
    33     7.65651269E+05   # M_tauL^2
    34     9.24335813E+05   # M_eR^2
    35     9.24335813E+05   # M_muR^2
    36     9.26510353E+05   # M_tauR^2
    41     5.39219515E+04   # M_q1L^2
    42     5.39219515E+04   # M_q2L^2
    43     1.13879882E+07   # M_q3L^2
    44     2.54537122E+05   # M_uR^2
    45     2.54537122E+05   # M_cR^2
    46     2.33967325E+07   # M_tR^2
    47     2.57209357E+05   # M_dR^2
    48     2.57209357E+05   # M_sR^2
    49     2.61669572E+05   # M_bR^2
# 
# NMSSM SPECIFIC PARAMETERS AT THE GUT SCALE
BLOCK NMSSMRUN Q=  1.96152990E+16 # (GUT SCALE)
     1     1.14613216E+00   # LAMBDA(MGUT,DR_bar)
     2     2.70925807E-01   # KAPPA(MGUT,DR_bar)
     3     5.38675278E+03   # ALAMBDA
     4     3.00068739E+03   # AKAPPA
    10     1.15587414E+07   # MS^2
# 
# FINE-TUNING parameter d(ln Mz^2)/d(ln PS^2)
         1     3.22958104E+00   # PS=MHU
         2     4.33509380E+00   # PS=MHD
         3     1.14166884E-01   # PS=MS
         4    -4.85538736E+00   # PS=ALAMBDA
         5    -8.31652176E-02   # PS=AKAPPA
         6    -0.00000000E+00   # PS=XIF
         7    -0.00000000E+00   # PS=XIS
         8     0.00000000E+00   # PS=MUP
         9     0.00000000E+00   # PS=MSP
        10    -0.00000000E+00   # PS=M3H
        11     7.64645682E-01   # PS=LAMBDA
        12    -4.18583786E-01   # PS=KAPPA
        13     6.80111221E-01   # PS=HTOP
        14    -6.86117506E-01   # PS=G
        15     4.85538736E+00   # MAX
        16                  4   # IMAX
# 
# REDUCED CROSS SECTIONS AT LHC
        11     2.09249627E-03   # VBF -> H1 -> tautau
        12     0.00000000E+00   # ggF -> H1 -> ZZ
        13     0.00000000E+00   # ggF -> H1 -> WW
        14     8.98729527E-03   # ggF -> H1 -> gammagamma
        15     6.29100059E-04   # VBF -> H1 -> gammagamma
        21     6.80090605E-02   # VBF -> H2 -> tautau
        22     6.28904325E-02   # ggF -> H2 -> ZZ
        23     6.28904325E-02   # ggF -> H2 -> WW
        24     6.06306056E-02   # ggF -> H2 -> gammagamma
        25     6.11049556E-02   # VBF -> H2 -> gammagamma
        31     5.46473321E-03   # VBF -> H3 -> tautau
        32     1.26605488E-04   # ggF -> H3 -> ZZ
        33     1.26605488E-04   # ggF -> H3 -> WW
        34     5.54925737E+00   # ggF -> H3 -> gammagamma
        35     2.17776004E-03   # VBF -> H3 -> gammagamma
# HIGGS + TOP BRANCHING RATIOS IN SLHA FORMAT
# Info about decay package
BLOCK DCINFO   # Program information
     1   NMSSMTools # Decay package
     2   3.2.0      # Version number
#           PDG          Width
DECAY        25     5.56251565E-05   # Lightest neutral Higgs scalar
     4.65035245E-03    2          21        21   # BR(H_1 -> gluon gluon)
     2.48905407E-04    2          13       -13   # BR(H_1 -> muon muon)
     6.71055058E-02    2          15       -15   # BR(H_1 -> tau tau)
     7.81156551E-04    2           3        -3   # BR(H_1 -> s sbar)
     4.19560625E-03    2           4        -4   # BR(H_1 -> c cbar)
     9.23004830E-01    2           5        -5   # BR(H_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_1 -> t tbar)
     0.00000000E+00    2          24       -24   # BR(H_1 -> W+ W-)
     0.00000000E+00    2          23        23   # BR(H_1 -> Z Z)
     1.36431291E-05    2          22        22   # BR(H_1 -> gamma gamma)
     0.00000000E+00    2          23        22   # BR(H_1 -> Z gamma)
DECAY        35     6.22588005E-02   # 2nd neutral Higgs scalar
     3.48575933E-03    2          21        21   # BR(H_2 -> gluon gluon)
     1.57899989E-05    2          13       -13   # BR(H_2 -> muon muon)
     4.46080556E-03    2          15       -15   # BR(H_2 -> tau tau)
     3.32409223E-05    2           3        -3   # BR(H_2 -> s sbar)
     1.85279812E-03    2           4        -4   # BR(H_2 -> c cbar)
     4.22698481E-02    2           5        -5   # BR(H_2 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_2 -> t tbar)
     1.28473593E-02    2          24       -24   # BR(H_2 -> W+ W-)
     1.41395251E-03    2          23        23   # BR(H_2 -> Z Z)
     1.45309602E-04    2          22        22   # BR(H_2 -> gamma gamma)
     1.03070442E-04    2          23        22   # BR(H_2 -> Z gamma)
     9.33372066E-01    2          25        25   # BR(H_2 -> H_1 H_1)
DECAY        45     7.35676002E+00   # 3rd neutral Higgs scalar
     7.02530933E-04    2          21        21   # BR(H_3 -> gluon gluon)
     3.78660757E-06    2          13       -13   # BR(H_3 -> muon muon)
     1.07097485E-03    2          15       -15   # BR(H_3 -> tau tau)
     5.96346415E-06    2           3        -3   # BR(H_3 -> s sbar)
     1.14466967E-04    2           4        -4   # BR(H_3 -> c cbar)
     7.87984687E-03    2           5        -5   # BR(H_3 -> b bbar)
     3.83711077E-01    2           6        -6   # BR(H_3 -> t tbar)
     4.56038793E-04    2          24       -24   # BR(H_3 -> W+ W-)
     2.20569241E-04    2          23        23   # BR(H_3 -> Z Z)
     3.02758934E-06    2          22        22   # BR(H_3 -> gamma gamma)
     7.92282078E-07    2          23        22   # BR(H_3 -> Z gamma)
     2.02215895E-02    2          25        25   # BR(H_3 -> H_1 H_1)
     1.40145350E-01    2          25        35   # BR(H_3 -> H_1 H_2)
     1.08612457E-04    2          35        35   # BR(H_3 -> H_2 H_2)
     1.39303590E-05    2          36        36   # BR(H_3 -> A_1 A_1)
     1.19818631E-01    2          23        36   # BR(H_3 -> A_1 Z)
     1.01647466E-01    2     1000022   1000022   # BR(H_3 -> neu_1 neu_1)
     1.13454867E-01    2     1000022   1000023   # BR(H_3 -> neu_1 neu_2)
     1.01328557E-02    2     1000022   1000025   # BR(H_3 -> neu_1 neu_3)
     8.47413033E-03    2     1000022   1000035   # BR(H_3 -> neu_1 neu_4)
     2.13928935E-02    2     1000023   1000023   # BR(H_3 -> neu_2 neu_2)
     4.70599618E-02    2     1000023   1000025   # BR(H_3 -> neu_2 neu_3)
     1.47247905E-02    2     1000023   1000035   # BR(H_3 -> neu_2 neu_4)
     6.04807385E-03    2     1000025   1000025   # BR(H_3 -> neu_3 neu_3)
     2.41735033E-03    2     1000025   1000035   # BR(H_3 -> neu_3 neu_4)
     1.70422698E-04    2     1000024  -1000024   # BR(H_3 -> cha_1 cha_1bar)
DECAY        36     1.07056062E-03   # Lightest pseudoscalar
     4.97629714E-03    2          21        21   # BR(A_1 -> gluon gluon)
     2.06426030E-04    2          13       -13   # BR(A_1 -> muon muon)
     5.83775686E-02    2          15       -15   # BR(A_1 -> tau tau)
     3.92673415E-04    2           3        -3   # BR(A_1 -> s sbar)
     1.13671757E-03    2           4        -4   # BR(A_1 -> c cbar)
     5.09463127E-01    2           5        -5   # BR(A_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(A_1 -> t tbar)
     6.62411834E-04    2          22        22   # BR(A_1 -> gamma gamma)
     2.73328094E-06    2          23        22   # BR(A_1 -> Z gamma)
     4.24782045E-01    2          23        25   # BR(A_1 -> Z H_1)
DECAY        46     8.71890427E+00   # 2nd pseudoscalar
     9.62128755E-04    2          21        21   # BR(A_2 -> gluon gluon)
     3.20450923E-06    2          13       -13   # BR(A_2 -> muon muon)
     9.06373020E-04    2          15       -15   # BR(A_2 -> tau tau)
     5.09546397E-06    2           3        -3   # BR(A_2 -> s sbar)
     1.53996261E-04    2           4        -4   # BR(A_2 -> c cbar)
     6.72651370E-03    2           5        -5   # BR(A_2 -> b bbar)
     4.54051945E-01    2           6        -6   # BR(A_2 -> t tbar)
     4.13970418E-06    2          22        22   # BR(A_2 -> gamma gamma)
     1.18584618E-06    2          23        22   # BR(A_2 -> Z gamma)
     1.52147414E-02    2          36        25   # BR(A_2 -> A_1 H_1)
     1.04376996E-01    2          36        35   # BR(A_2 -> A_1 H_2)
     1.19990690E-01    2          23        25   # BR(A_2 -> Z H_1)
     1.06416113E-03    2          23        35   # BR(A_2 -> Z H_2)
     1.20995746E-01    2     1000022   1000022   # BR(A_2 -> neu_1 neu_1)
     6.83578593E-03    2     1000022   1000023   # BR(A_2 -> neu_1 neu_2)
     8.19308541E-02    2     1000022   1000025   # BR(A_2 -> neu_1 neu_3)
     8.25750845E-03    2     1000022   1000035   # BR(A_2 -> neu_1 neu_4)
     7.12048557E-03    2     1000023   1000023   # BR(A_2 -> neu_2 neu_2)
     2.00143166E-02    2     1000023   1000025   # BR(A_2 -> neu_2 neu_3)
     1.96457564E-03    2     1000023   1000035   # BR(A_2 -> neu_2 neu_4)
     3.52007509E-02    2     1000025   1000025   # BR(A_2 -> neu_3 neu_3)
     1.40488480E-02    2     1000025   1000035   # BR(A_2 -> neu_3 neu_4)
     1.69958477E-04    2     1000024  -1000024   # BR(A_2 -> cha_1 cha_1bar)
DECAY        37     8.06129934E+00   # Charged Higgs
     3.47396342E-06    2         -13        14   # BR(H+ -> muon nu_muon)
     9.82585462E-04    2         -15        16   # BR(H+ -> tau nu_tau)
     2.64983862E-07    2           2        -3   # BR(H+ -> u sbar)
     1.05958415E-05    2           4        -3   # BR(H+ -> c sbar)
     1.12237601E-07    2           2        -5   # BR(H+ -> u bbar)
     1.12333367E-05    2           4        -5   # BR(H+ -> c bbar)
     4.69133956E-01    2           6        -5   # BR(H+ -> t bbar)
     1.26570719E-01    2          24        25   # BR(H+ -> W+ H_1)
     1.11769104E-03    2          24        35   # BR(H+ -> W+ H_2)
     1.05581521E-01    2          24        36   # BR(H+ -> W+ A_1)
     2.32254426E-01    2     1000024   1000022   # BR(H+ -> cha_1 neu_1)
     1.88263405E-02    2     1000024   1000023   # BR(H+ -> cha_1 neu_2)
     3.01311952E-02    2     1000024   1000025   # BR(H+ -> cha_1 neu_3)
     1.53758845E-02    2     1000024   1000035   # BR(H+ -> cha_1 neu_4)
DECAY         6     1.38766019E+00   # Top Quark
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#         PDG            Width
DECAY        24     2.08500000E+00   # W+ (measured)
     1.16500000E-01    2         -11        12   # BR(W+ -> e+ nu_e)
     1.16500000E-01    2         -13        14   # BR(W+ -> mu+ nu_mu)
     1.12000000E-01    2         -15        16   # BR(W+ -> tau+ nu_tau)
     3.65000000E-01    2           2        -1   # BR(W+ -> u db)
     3.10000000E-01    2           4        -3   # BR(W+ -> c sb)
#         PDG            Width
DECAY        23     2.49520000E+00   # Z (measured)
     2.00000000E-01    2         -12        12   # BR(Z -> invisible)
     3.36500000E-02    2         -11        11   # BR(Z -> e+ e-)
     3.36500000E-02    2         -13        13   # BR(Z -> mu+ mu-)
     3.37000000E-02    2         -15        15   # BR(Z -> tau+ tau-)
     1.11000000E-01    2           2        -2   # BR(Z -> u ub)
     1.58500000E-01    2           1        -1   # BR(Z -> d db)
     1.58500000E-01    2           3        -3   # BR(Z -> s sb)
     1.20000000E-01    2           4        -4   # BR(Z -> c cb)
     1.51000000E-01    2           5        -5   # BR(Z -> b bb)
#         PDG            Width
DECAY   1000024     1.95835259E-01   # chargino1
#                    chargino1 2-body decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        24   # BR(~chi_1+ -> ~chi_10  W+)
#         PDG            Width
DECAY   1000037     2.89305455E+00   # chargino2
#                    chargino2 2-body decays
#          BR         NDA      ID1       ID2
     2.60473169E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     1.03251136E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     1.95589823E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     1.82869879E-01    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     3.53138607E-02    2     1000035        24   # BR(~chi_2+ -> ~chi_40  W+)
     2.76615813E-03    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  H_1 )
     2.19281770E-01    2     1000024        35   # BR(~chi_2+ -> ~chi_1+  H_2 )
     4.54204900E-04    2     1000024        36   # BR(~chi_2+ -> ~chi_1+  A_1 )
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1
#         PDG            Width
DECAY   1000023     3.19158058E-01   # neutralino2
#                    neutralino2 2-body decays
#          BR         NDA      ID1       ID2
     5.31469693E-01    2     1000022        23   # BR(~chi_20 -> ~chi_10   Z )
     3.73655483E-01    2     1000022        25   # BR(~chi_20 -> ~chi_10   H_1 )
     9.48748235E-02    2     1000022        35   # BR(~chi_20 -> ~chi_10   H_2 )
#         PDG            Width
DECAY   1000025     1.01789457E-01   # neutralino3
#                    neutralino3 2-body decays
#          BR         NDA      ID1       ID2
     6.21035037E-01    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     3.54028175E-01    2     1000022        25   # BR(~chi_30 -> ~chi_10   H_1 )
     2.49367885E-02    2     1000022        35   # BR(~chi_30 -> ~chi_10   H_2 )
#         PDG            Width
DECAY   1000035     9.94344796E-02   # neutralino4
#                    neutralino4 2-body decays
#          BR         NDA      ID1       ID2
     3.40620716E-01    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.79310349E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     1.79310349E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     3.93398257E-03    2     1000022        25   # BR(~chi_40 -> ~chi_10   H_1 )
     5.98467393E-04    2     1000022        35   # BR(~chi_40 -> ~chi_10   H_2 )
     2.87068534E-02    2     1000022        36   # BR(~chi_40 -> ~chi_10   A_1 )
     9.60053926E-04    2     1000023        25   # BR(~chi_40 -> ~chi_20   H_1 )
     2.66559228E-01    2     1000025        25   # BR(~chi_40 -> ~chi_30   H_1 )
#         PDG            Width
DECAY   1000045     2.89752872E+00   # neutralino5
#                    neutralino5 2-body decays
#          BR         NDA      ID1       ID2
     6.33110174E-02    2     1000022        23   # BR(~chi_50 -> ~chi_10   Z )
     7.93198619E-02    2     1000023        23   # BR(~chi_50 -> ~chi_20   Z )
     1.12593597E-01    2     1000025        23   # BR(~chi_50 -> ~chi_30   Z )
     6.89350736E-03    2     1000035        23   # BR(~chi_50 -> ~chi_40   Z )
     2.58484657E-01    2     1000024       -24   # BR(~chi_50 -> ~chi_1+   W-)
     2.58484657E-01    2    -1000024        24   # BR(~chi_50 -> ~chi_1-   W+)
     9.51171782E-04    2     1000022        25   # BR(~chi_50 -> ~chi_10   H_1 )
     3.37868995E-02    2     1000022        35   # BR(~chi_50 -> ~chi_10   H_2 )
     7.91410865E-04    2     1000022        36   # BR(~chi_50 -> ~chi_10   A_1 )
     1.15524275E-03    2     1000023        25   # BR(~chi_50 -> ~chi_20   H_1 )
     9.07397995E-02    2     1000023        35   # BR(~chi_50 -> ~chi_20   H_2 )
     5.61674673E-05    2     1000023        36   # BR(~chi_50 -> ~chi_20   A_1 )
     3.88956924E-04    2     1000025        25   # BR(~chi_50 -> ~chi_30   H_1 )
     6.57767506E-02    2     1000025        35   # BR(~chi_50 -> ~chi_30   H_2 )
     8.10994501E-05    2     1000025        36   # BR(~chi_50 -> ~chi_30   A_1 )
     2.64177170E-04    2     1000035        25   # BR(~chi_50 -> ~chi_40   H_1 )
     2.69143369E-02    2     1000035        35   # BR(~chi_50 -> ~chi_40   H_2 )
     6.68853518E-06    2     1000035        36   # BR(~chi_50 -> ~chi_40   A_1 )
#         PDG            Width
DECAY   1000021     1.50801032E+00   # gluino
#                    gluino 2-body decays
#          BR         NDA      ID1       ID2
     4.13776813E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     4.13776813E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     4.33195157E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     4.33195157E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     4.57587727E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     4.57587727E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     4.46514657E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     4.46514657E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     4.13776813E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     4.13776813E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     4.33195157E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     4.33195157E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     4.57587727E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     4.57587727E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     4.46514657E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     4.46514657E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     5.05116460E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     5.05116460E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.42857445E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.42857445E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
#                    gluino 3-body decays
#           BR         NDA      ID1       ID2       ID3
     1.81114474E-02    3     1000022         6        -6   # BR(~g -> ~chi_10 t  tb)
     2.97914272E-02    3     1000023         6        -6   # BR(~g -> ~chi_20 t  tb)
     3.25937528E-02    3     1000025         6        -6   # BR(~g -> ~chi_30 t  tb)
     1.03859633E-02    3     1000035         6        -6   # BR(~g -> ~chi_40 t  tb)
     1.88938380E-03    3     1000045         6        -6   # BR(~g -> ~chi_50 t  tb)
     1.60633468E-02    3     1000024         5        -6   # BR(~g -> ~chi_1+ b  tb)
     1.60633468E-02    3    -1000024         6        -5   # BR(~g -> ~chi_1- t  bb)
     2.50182037E-03    3     1000037         5        -6   # BR(~g -> ~chi_2+ b  tb)
     2.50182037E-03    3    -1000037         6        -5   # BR(~g -> ~chi_2- t  bb)
     3.65843808E-05    3     1000006        -5       -24   # BR(~g -> ~t_1    bb W-)
     3.65843808E-05    3    -1000006         5        24   # BR(~g -> ~t_1*   b  W+)
#         PDG            Width
DECAY   1000011     5.78663706E+00   # selectron_L
#                    selectron_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06852865E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)   
     1.09569419E-03    2     1000023        11   # BR(~e_L -> ~chi_20 e-)   
     1.30819802E-03    2     1000025        11   # BR(~e_L -> ~chi_30 e-)  
     2.02127955E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)  
     2.59433558E-01    2     1000045        11   # BR(~e_L -> ~chi_50 e-)  
     1.25739778E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.35602002E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#         PDG            Width
DECAY   2000011     4.32983424E+00   # selectron_R
#                    selectron_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457556E-03    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     5.09644981E-03    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     4.35807439E-02    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     9.48925398E-01    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
     1.02832816E-04    2     1000045        11   # BR(~e_R -> ~chi_50 e-)
#         PDG            Width
DECAY   1000013     5.78663706E+00   # smuon_L
#                    smuon_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06852865E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.09569419E-03    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.30819802E-03    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.02127955E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     2.59433558E-01    2     1000045        13   # BR(~mu_L -> ~chi_50 mu-)
     1.25739778E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.35602002E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#         PDG            Width
DECAY   2000013     4.32983424E+00   # smuon_R
#                    smuon_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457556E-03    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     5.09644981E-03    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     4.35807439E-02    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     9.48925398E-01    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
     1.02832816E-04    2     1000045        13   # BR(~mu_R -> ~chi_50 mu-)
#         PDG            Width
DECAY   1000015     5.03156171E+00   # stau_1
#                    stau1 2-body decays
#          BR         NDA      ID1       ID2
     1.14186114E-03    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     4.79057689E-04    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     2.71053734E-02    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     5.31167221E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.43366746E-01    2     1000045        15   # BR(~tau_1 -> ~chi_50  tau-)
     8.82058020E-04    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     2.95857683E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   2000015     4.34604804E+00   # stau_2
#                    stau_2 2-body decays
#          BR         NDA      ID1       ID2
     1.37428613E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     9.20766468E-03    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     1.68827618E-02    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     5.99655563E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     1.79483897E-01    2     1000045        15   # BR(~tau_2 -> ~chi_50  tau-)
     2.39284185E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     3.70486882E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   1000012     5.82409806E+00   # snu_eL
#                    snu_eL 2-body decays
#          BR         NDA      ID1       ID2
     3.44541021E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     8.91602588E-03    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     2.06692014E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     1.53093689E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     2.64584107E-01    2     1000045        12   # BR(~nu_eL -> ~chi_50 nu_e)
     3.61604589E-02    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.13131108E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#         PDG            Width
DECAY   1000014     5.82409806E+00   # snu_muL
#                    snu_muL 2-body decays
#          BR         NDA      ID1       ID2
     3.44541021E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     8.91602588E-03    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     2.06692014E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     1.53093689E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     2.64584107E-01    2     1000045        14   # BR(~nu_muL -> ~chi_50 nu_mu)
     3.61604589E-02    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.13131108E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#         PDG            Width
DECAY   1000016     5.83820352E+00   # snu_tauL
#                    sbu_tauL 2-body decays
#          BR         NDA      ID1       ID2
     3.43708589E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     8.89448421E-03    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     2.06192633E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     1.52723805E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     2.63944855E-01    2     1000045        16   # BR(~nu_tauL -> ~chi_50 nu_tau)
     3.84961084E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.11884398E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#         PDG            Width
DECAY   1000002     5.73689798E+00   # sup_L
#                    sup_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251693E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.97343563E-03    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     5.95852739E-04    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     2.97748093E-02    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     3.11048068E-01    2     1000045         2   # BR(~u_L -> ~chi_50 u)
     3.75280104E-02    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.17084572E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#         PDG            Width
DECAY   2000002     1.99702649E+00   # sup_R
#                    sup_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404067E-03    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     5.02648420E-03    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     4.29887112E-02    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     9.49644060E-01    2     1000035         2   # BR(~u_R -> ~chi_40 u)
     1.16703919E-04    2     1000045         2   # BR(~u_R -> ~chi_50 u)
#         PDG            Width
DECAY   1000001     5.64341306E+00   # sdown_L
#                    sdown_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434144E-03    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     5.79758592E-03    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     7.45741542E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     1.34387635E-02    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     3.21776483E-01    2     1000045         1   # BR(~d_L -> ~chi_50 d)
     1.31720061E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.49293690E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#         PDG            Width
DECAY   2000001     4.99627621E-01   # sdown_R
#                    sdown_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360748E-03    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     5.02599170E-03    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     4.29845402E-02    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     9.49649028E-01    2     1000035         1   # BR(~d_R -> ~chi_40 d)
     1.16832598E-04    2     1000045         1   # BR(~d_R -> ~chi_50 d)
#         PDG            Width
DECAY   1000004     5.73689798E+00   # scharm_L
#                    scharm_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251693E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.97343563E-03    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     5.95852739E-04    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     2.97748093E-02    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     3.11048068E-01    2     1000045         4   # BR(~c_L -> ~chi_50 c)
     3.75280104E-02    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.17084572E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#         PDG            Width
DECAY   2000004     1.99702649E+00   # scharm_R
#                    scharm_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404067E-03    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     5.02648420E-03    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     4.29887112E-02    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     9.49644060E-01    2     1000035         4   # BR(~c_R -> ~chi_40 c)
     1.16703919E-04    2     1000045         4   # BR(~c_R -> ~chi_50 c)
#         PDG            Width
DECAY   1000003     5.64341306E+00   # sstrange_L
#                    sstrange_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434144E-03    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     5.79758592E-03    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     7.45741542E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     1.34387635E-02    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     3.21776483E-01    2     1000045         3   # BR(~s_L -> ~chi_50 s)
     1.31720061E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.49293690E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#         PDG            Width
DECAY   2000003     4.99627621E-01   # sstrange_R
#                    sstrange_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360748E-03    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     5.02599170E-03    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     4.29845402E-02    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     9.49649028E-01    2     1000035         3   # BR(~s_R -> ~chi_40 s)
     1.16832598E-04    2     1000045         3   # BR(~s_R -> ~chi_50 s)
#         PDG            Width
DECAY   1000006     2.18936978E+01   # stop1
#                    stop1 2-body decays
#          BR         NDA      ID1       ID2
     1.09913481E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     1.96163658E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     2.17644430E-01    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     8.77837195E-02    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.56473773E-02    2     1000045         6   # BR(~t_1 -> ~chi_50 t )
     2.52077716E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     9.07696178E-02    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#         PDG            Width
DECAY   2000006     3.21980391E+01   # stop2
#                    stop2 2-body decays
#          BR         NDA      ID1       ID2
     1.10844904E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.28910021E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     2.07549028E-01    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     2.98898792E-02    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     2.13141744E-02    2     1000045         6   # BR(~t_2 -> ~chi_50 t )
     3.26156678E-01    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.69379015E-02    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     6.25042689E-08    2     1000006        25   # BR(~t_2 -> ~t_1    H1 )
     3.95658329E-07    2     1000006        35   # BR(~t_2 -> ~t_1    H2 )
     3.55217490E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
     1.57606022E-03    2     1000005        24   # BR(~t_2 -> ~b_1    W+)
     1.29914739E-03    2     2000005        24   # BR(~t_2 -> ~b_2    W+)
#         PDG            Width
DECAY   1000005     7.91279840E+00   # sbottom1
#                    sbottom1 2-body decays
#          BR         NDA      ID1       ID2
     5.94547650E-04    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.60819323E-04    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     1.03673768E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     3.88333243E-02    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     7.88300445E-02    2     1000045         5   # BR(~b_1 -> ~chi_50 b )
     7.01757596E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     1.69456291E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
#         PDG            Width
DECAY   2000005     1.27182607E+01   # sbottom2
#                    sbottom2 2-body decays
#          BR         NDA      ID1       ID2
     6.44127456E-04    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     4.84361774E-03    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     6.47700874E-04    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.83053292E-02    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     8.44701357E-02    2     1000045         5   # BR(~b_2 -> ~chi_50 b )
     7.08769139E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     1.81711663E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
#
# Dummy alpha block (for Prospino compatibility only - not used)
BLOCK ALPHA
	0.1000E+00
"""

  f = open("%s/src/WorkingPoint_mH1_20_mH2_125p3_MSUSY_1000.slha" % os.environ['CMSSW_BASE'],"w")
  f.write(slhacontent)
  f.close()
  
  return process