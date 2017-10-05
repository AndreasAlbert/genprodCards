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
    11     1.13661330E+03   # ATOP
    12     1.13661330E+03   # ABOTTOM
    13     1.13661330E+03   # ATAU
    16     1.13661330E+03   # AMUON
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
    64     6.15399405E+01   # AKAPPA
    65    -2.00000000E+02   # MUEFF
# 
BLOCK MASS   # Mass spectrum 
#  PDG Code     mass             particle 
        25     9.00000000E+01   # lightest neutral scalar
        35     1.25300000E+02   # second neutral scalar
        45     5.76808195E+02   # third neutral scalar
        36     1.21440727E+02   # lightest pseudoscalar
        46     5.76897771E+02   # second pseudoscalar
        37     5.65608486E+02   # charged Higgs
   1000001     1.03816356E+03   #  ~d_L
   2000001     1.03719659E+03   #  ~d_R
   1000002     1.03601090E+03   #  ~u_L
   2000002     1.03654529E+03   #  ~u_R
   1000003     1.03816356E+03   #  ~s_L
   2000003     1.03719659E+03   #  ~s_R
   1000004     1.03601090E+03   #  ~c_L
   2000004     1.03654529E+03   #  ~c_R
   1000005     1.03577789E+03   #  ~b_1
   2000005     1.03958213E+03   #  ~b_2
   1000006     9.61529997E+02   #  ~t_1
   2000006     1.12597738E+03   #  ~t_2
   1000011     1.00077837E+03   #  ~e_L
   2000011     1.00067504E+03   #  ~e_R
   1000012     9.98544999E+02   #  ~nue_L
   1000013     1.00077837E+03   #  ~mu_L
   2000013     1.00067504E+03   #  ~mu_R
   1000014     9.98544999E+02   #  ~numu_L
   1000015     9.99259862E+02   #  ~tau_1
   2000015     1.00219456E+03   #  ~tau_2
   1000016     9.98544999E+02   #  ~nutau_L
   1000021     1.07903179E+03   #  ~g
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
     1     3.63805695E-04   # BR(b -> s gamma)
    11     4.02160550E-04   # (BR(b -> s gamma)+Theor.Err.)
    12     3.05781389E-04   # (BR(b -> s gamma)-Theor.Err.)
# Exp. 2 Sigma: 4.99E-01 < Delta M_d < 5.15E-01:
     2     6.23707738E-01   # Delta M_d in ps^-1
    21     1.08922956E+00   # Delta M_d +Theor.Err.
    22     1.67317103E-01   # Delta M_d -Theor.Err.
# Exp. 2 Sigma: 1.753E+01 < Delta Ms < 1.801E+01:
     3     2.16085944E+01   # Delta M_s in ps^-1
    31     2.85156356E+01   # Delta M_s +Theor.Err.
    32     1.48345721E+01   # Delta M_s -Theor.Err.
# Exp. 95% C.L.: BR(Bs->mu+mu-) < 4.5E-09:
     4     3.66103268E-09   # BR(Bs -> mu+mu-)
    41     6.21819510E-09   # BR(Bs -> mu+mu-)+Theor.Err.
    42     1.77718686E-09   # BR(Bs -> mu+mu-)-Theor.Err.
# Exp. 2 Sigma: 8.90E-05 < BR(B+ > tau+ + nu_tau) < 2.45E-04:
     5     1.31637756E-04   # BR(B+ -> tau+ + nu_tau)
    51     2.63327004E-04   # BR(B+ -> tau+ + nu_tau) + Theor.Err.
    52     5.68116968E-05   # BR(B+ -> tau+ + nu_tau) - Theor.Err.
# BSM contr. to the muon anomalous magn. moment:
     6    -8.32486773E-11   # Del_a_mu
    61     1.99485321E-10   # Del_a_mu + Theor.Err.
    62    -3.65982675E-10   # Del_a_mu - Theor.Err.
# Minimal Exp.-SM (2 sigma):  8.77306222E-10
# Maximal Exp.-SM (2 sigma):  4.61144414E-09
# 
BLOCK HMIX Q=  1.00000000E+03 # (STOP/SBOTTOM MASSES)
     1    -2.00000000E+02   # MUEFF
     2     2.57525562E+00   # TAN(BETA)
     3     2.41822895E+02   # V(Q)
     4     3.25992325E+05   # MA^2
     5     1.92834365E+04   # MP^2
# 
# 3*3 Higgs mixing
BLOCK NMHMIX
  1  1    -9.60131296E-02   # S_(1,1)
  1  2     1.34919701E-01   # S_(1,2)
  1  3     9.86193771E-01   # S_(1,3)
  2  1     3.76225962E-01   # S_(2,1)
  2  2     9.22191655E-01   # S_(2,2)
  2  3    -8.95353358E-02   # S_(2,3)
  3  1     9.21539747E-01   # S_(3,1)
  3  2    -3.62435132E-01   # S_(3,2)
  3  3     1.39302801E-01   # S_(3,3)
# 
# 3*3 Pseudoscalar Higgs mixing
BLOCK NMAMIX
  1  1     1.30764013E-01   # P_(1,1)
  1  2     5.02938513E-02   # P_(1,2)
  1  3     9.90136841E-01   # P_(1,3)
  2  1     9.24135452E-01   # P_(2,1)
  2  2     3.55436712E-01   # P_(2,2)
  2  3    -1.40103662E-01   # P_(2,3)
# 
# 3rd generation sfermion mixing
BLOCK STOPMIX  # Stop mixing matrix
  1  1    -7.08193366E-01   # Rst_(1,1)
  1  2     7.06018524E-01   # Rst_(1,2)
  2  1    -7.06018524E-01   # Rst_(2,1)
  2  2    -7.08193366E-01   # Rst_(2,2)
BLOCK SBOTMIX  # Sbottom mixing matrix
  1  1    -6.15124456E-01   # Rsb_(1,1)
  1  2     7.88430025E-01   # Rsb_(1,2)
  2  1    -7.88430025E-01   # Rsb_(2,1)
  2  2    -6.15124456E-01   # Rsb_(2,2)
BLOCK STAUMIX  # Stau mixing matrix
  1  1    -6.94546498E-01   # Rsl_(1,1)
  1  2     7.19447817E-01   # Rsl_(1,2)
  2  1    -7.19447817E-01   # Rsl_(2,1)
  2  2    -6.94546498E-01   # Rsl_(2,2)
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
  1  1     1.44554922E-01   # U-type fermions
  1  2    -2.67461630E-01   # D-type fermions
  1  3     9.14600053E-02   # W,Z bosons
  1  4     1.87673064E-01   # Gluons
  1  5     1.89003695E-01   # Photons
# H2
  2  1     9.88049496E-01   # U-type fermions
  2  2     1.04804425E+00   # D-type fermions
  2  3     9.95780779E-01   # W,Z bosons
  2  4     9.88555619E-01   # Gluons
  2  5     9.73408605E-01   # Photons
# H3
  3  1    -3.88318249E-01   # U-type fermions
  3  2     2.56711268E+00   # D-type fermions
  3  3    -7.46374802E-03   # W,Z bosons
  3  4     3.90431774E-01   # Gluons
  3  5     1.63256086E+00   # Photons
# A1
  4  1     5.38855607E-02   # U-type fermions
  4  2     3.64266390E-01   # D-type fermions
  4  3     0.00000000E+00   # W,Z bosons
  4  4     4.51807172E-02   # Gluons
  4  5     3.38241250E-01   # Photons
# A2
  5  1     3.80820041E-01   # U-type fermions
  5  2     2.57434348E+00   # D-type fermions
  5  3     0.00000000E+00   # W,Z bosons
  5  4     3.84597278E-01   # Gluons
  5  5     3.64009476E-01   # Photons
# 
# GAUGE AND YUKAWA COUPLINGS AT THE SUSY SCALE
BLOCK GAUGE Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.62459603E-01   # g1(Q,DR_bar)
     2     6.42566822E-01   # g2(Q,DR_bar)
     3     1.05976273E+00   # g3(Q,DR_bar)
BLOCK YU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     9.25551241E-01   # HTOP(Q,DR_bar)
BLOCK YD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     3.93488521E-02   # HBOT(Q,DR_bar)
BLOCK YE Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     2.78125730E-02   # HTAU(Q,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE SUSY SCALE
BLOCK AU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.13661330E+03   # ATOP
BLOCK AD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.13661330E+03   # ABOT
BLOCK AE Q=  1.00000000E+03 # (SUSY SCALE)
  2  2     1.13661330E+03   # AMUON
  3  3     1.13661330E+03   # ATAU
# 
# SOFT MASSES AT THE SUSY SCALE
BLOCK MSOFT Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    21     2.36942392E+05   # M_HD^2
    22     2.69316666E+04   # M_HU^2
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
     4     6.15399405E+01   # AKAPPA
     5    -2.00000000E+02   # MUEFF
    10    -7.91930569E+02   # MS^2
# 
# GAUGE AND YUKAWA COUPLINGS AT THE GUT SCALE
BLOCK GAUGE Q=  1.96152991E+16 # (GUT SCALE)
     1     7.11402404E-01   # g1(MGUT,DR_bar), GUT normalization
     2     7.11402404E-01   # g2(MGUT,DR_bar)
     3     7.02978760E-01   # g3(MGUT,DR_bar)
BLOCK YU Q=  1.96152991E+16 # (GUT SCALE)
  3  3     8.29138658E-01   # HTOP(MGUT,DR_bar)
BLOCK YD Q=  1.96152991E+16 # (GUT SCALE)
  3  3     1.80986089E-02   # HBOT(MGUT,DR_bar)
BLOCK YE Q=  1.96152991E+16 # (GUT SCALE)
  3  3     2.17551430E-02   # HTAU(MGUT,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE GUT SCALE
BLOCK AU Q=  1.96152991E+16 # (GUT SCALE)
  3  3     1.02320867E+04   # ATOP
BLOCK AD Q=  1.96152991E+16 # (GUT SCALE)
  3  3     4.16430051E+03   # ABOT
BLOCK AE Q=  1.96152991E+16 # (GUT SCALE)
  2  2     2.03342377E+03   # AMUON
  3  3     2.05926586E+03   # ATAU
# 
# SOFT MASSES SQUARED AT THE GUT SCALE
BLOCK MSOFT Q=  1.96152991E+16 # (GUT SCALE)
     1     7.30396961E+02   # M1
     2     7.87277972E+02   # M2
     3     4.67823591E+02   # M3
    21     5.38813903E+06   # M_HD^2
    22     4.09231972E+07   # M_HU^2
    31     7.64396071E+05   # M_eL^2
    32     7.64396071E+05   # M_muL^2
    33     7.65464937E+05   # M_tauL^2
    34     9.24089839E+05   # M_eR^2
    35     9.24089839E+05   # M_muR^2
    36     9.26235928E+05   # M_tauR^2
    41     5.33788131E+04   # M_q1L^2
    42     5.33788131E+04   # M_q2L^2
    43     1.11905083E+07   # M_q3L^2
    44     2.54268483E+05   # M_uR^2
    45     2.54268483E+05   # M_cR^2
    46     2.29941024E+07   # M_tR^2
    47     2.56847440E+05   # M_dR^2
    48     2.56847440E+05   # M_sR^2
    49     2.61240689E+05   # M_bR^2
# 
# NMSSM SPECIFIC PARAMETERS AT THE GUT SCALE
BLOCK NMSSMRUN Q=  1.96152991E+16 # (GUT SCALE)
     1     1.14613205E+00   # LAMBDA(MGUT,DR_bar)
     2     2.70925789E-01   # KAPPA(MGUT,DR_bar)
     3     5.31992482E+03   # ALAMBDA
     4     2.74711955E+03   # AKAPPA
    10     1.13032177E+07   # MS^2
# 
# FINE-TUNING parameter d(ln Mz^2)/d(ln PS^2)
         1     3.24563668E+00   # PS=MHU
         2     4.22678786E+00   # PS=MHD
         3     2.22267237E-03   # PS=MS
         4    -4.71617149E+00   # PS=ALAMBDA
         5     3.45442216E-03   # PS=AKAPPA
         6    -0.00000000E+00   # PS=XIF
         7     0.00000000E+00   # PS=XIS
         8     0.00000000E+00   # PS=MUP
         9    -0.00000000E+00   # PS=MSP
        10    -0.00000000E+00   # PS=M3H
        11     7.16043231E-01   # PS=LAMBDA
        12    -3.74388272E-01   # PS=KAPPA
        13     6.82979665E-01   # PS=HTOP
        14    -6.83144791E-01   # PS=G
        15     4.71617149E+00   # MAX
        16                  4   # IMAX
# 
# REDUCED CROSS SECTIONS AT LHC
        11     8.69320223E-03   # VBF -> H1 -> tautau
        12     0.00000000E+00   # ggF -> H1 -> ZZ
        13     4.28016683E-03   # ggF -> H1 -> WW
        14     1.82794951E-02   # ggF -> H1 -> gammagamma
        15     4.34132954E-03   # VBF -> H1 -> gammagamma
        21     1.02447703E+00   # VBF -> H2 -> tautau
        22     9.11475922E-01   # ggF -> H2 -> ZZ
        23     9.11475922E-01   # ggF -> H2 -> WW
        24     8.71030651E-01   # ggF -> H2 -> gammagamma
        25     8.83809566E-01   # VBF -> H2 -> gammagamma
        31     5.05242465E-03   # VBF -> H3 -> tautau
        32     1.16869259E-04   # ggF -> H3 -> ZZ
        33     1.16869259E-04   # ggF -> H3 -> WW
        34     5.59178501E+00   # ggF -> H3 -> gammagamma
        35     2.04349743E-03   # VBF -> H3 -> gammagamma
# HIGGS + TOP BRANCHING RATIOS IN SLHA FORMAT
# Info about decay package
BLOCK DCINFO   # Program information
     1   NMSSMTools # Decay package
     2   3.2.0      # Version number
#           PDG          Width
DECAY        25     1.53645107E-04   # Lightest neutral Higgs scalar
     1.95815810E-02    2          21        21   # BR(H_1 -> gluon gluon)
     3.07031756E-04    2          13       -13   # BR(H_1 -> muon muon)
     8.66410881E-02    2          15       -15   # BR(H_1 -> tau tau)
     6.63422114E-04    2           3        -3   # BR(H_1 -> s sbar)
     1.16640854E-02    2           4        -4   # BR(H_1 -> c cbar)
     8.80472118E-01    2           5        -5   # BR(H_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_1 -> t tbar)
     2.76394249E-05    2          24       -24   # BR(H_1 -> W+ W-)
     0.00000000E+00    2          23        23   # BR(H_1 -> Z Z)
     6.43033944E-04    2          22        22   # BR(H_1 -> gamma gamma)
     0.00000000E+00    2          23        22   # BR(H_1 -> Z gamma)
DECAY        35     4.21272108E-03   # 2nd neutral Higgs scalar
     5.08424376E-02    2          21        21   # BR(H_2 -> gluon gluon)
     2.39378915E-04    2          13       -13   # BR(H_2 -> muon muon)
     6.76265273E-02    2          15       -15   # BR(H_2 -> tau tau)
     5.03707470E-04    2           3        -3   # BR(H_2 -> s sbar)
     2.70599808E-02    2           4        -4   # BR(H_2 -> c cbar)
     6.40673628E-01    2           5        -5   # BR(H_2 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_2 -> t tbar)
     1.88661632E-01    2          24       -24   # BR(H_2 -> W+ W-)
     2.07636905E-02    2          23        23   # BR(H_2 -> Z Z)
     2.11516829E-03    2          22        22   # BR(H_2 -> gamma gamma)
     1.51384920E-03    2          23        22   # BR(H_2 -> Z gamma)
DECAY        45     7.39974416E+00   # 3rd neutral Higgs scalar
     6.97258453E-04    2          21        21   # BR(H_3 -> gluon gluon)
     3.76395682E-06    2          13       -13   # BR(H_3 -> muon muon)
     1.06456855E-03    2          15       -15   # BR(H_3 -> tau tau)
     5.92732787E-06    2           3        -3   # BR(H_3 -> s sbar)
     1.13608034E-04    2           4        -4   # BR(H_3 -> c cbar)
     7.83124530E-03    2           5        -5   # BR(H_3 -> b bbar)
     3.81044343E-01    2           6        -6   # BR(H_3 -> t tbar)
     4.21968762E-04    2          24       -24   # BR(H_3 -> W+ W-)
     2.04098007E-04    2          23        23   # BR(H_3 -> Z Z)
     3.03280178E-06    2          22        22   # BR(H_3 -> gamma gamma)
     7.90522528E-07    2          23        22   # BR(H_3 -> Z gamma)
     2.52344176E-02    2          25        25   # BR(H_3 -> H_1 H_1)
     1.27483782E-01    2          25        35   # BR(H_3 -> H_1 H_2)
     1.15440786E-03    2          35        35   # BR(H_3 -> H_2 H_2)
     1.16139111E-04    2          36        36   # BR(H_3 -> A_1 A_1)
     1.31034095E-01    2          23        36   # BR(H_3 -> A_1 Z)
     1.00715912E-01    2     1000022   1000022   # BR(H_3 -> neu_1 neu_1)
     1.12553209E-01    2     1000022   1000023   # BR(H_3 -> neu_1 neu_2)
     1.02794132E-02    2     1000022   1000025   # BR(H_3 -> neu_1 neu_3)
     8.44608214E-03    2     1000022   1000035   # BR(H_3 -> neu_1 neu_4)
     2.15401583E-02    2     1000023   1000023   # BR(H_3 -> neu_2 neu_2)
     4.68427177E-02    2     1000023   1000025   # BR(H_3 -> neu_2 neu_3)
     1.47178725E-02    2     1000023   1000035   # BR(H_3 -> neu_2 neu_4)
     5.92220114E-03    2     1000025   1000025   # BR(H_3 -> neu_3 neu_3)
     2.43441967E-03    2     1000025   1000035   # BR(H_3 -> neu_3 neu_4)
     1.34567423E-04    2     1000024  -1000024   # BR(H_3 -> cha_1 cha_1bar)
DECAY        36     3.53865643E-04   # Lightest pseudoscalar
     2.78445327E-03    2          21        21   # BR(A_1 -> gluon gluon)
     3.33659615E-04    2          13       -13   # BR(A_1 -> muon muon)
     9.43347902E-02    2          15       -15   # BR(A_1 -> tau tau)
     6.93244407E-04    2           3        -3   # BR(A_1 -> s sbar)
     1.09459908E-03    2           4        -4   # BR(A_1 -> c cbar)
     9.00292211E-01    2           5        -5   # BR(A_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(A_1 -> t tbar)
     4.66819688E-04    2          22        22   # BR(A_1 -> gamma gamma)
     2.22614491E-07    2          23        22   # BR(A_1 -> Z gamma)
DECAY        46     8.80619142E+00   # 2nd pseudoscalar
     9.55603091E-04    2          21        21   # BR(A_2 -> gluon gluon)
     3.18114769E-06    2          13       -13   # BR(A_2 -> muon muon)
     8.99765347E-04    2          15       -15   # BR(A_2 -> tau tau)
     5.05885713E-06    2           3        -3   # BR(A_2 -> s sbar)
     1.52947836E-04    2           4        -4   # BR(A_2 -> c cbar)
     6.67771725E-03    2           5        -5   # BR(A_2 -> b bbar)
     4.50676833E-01    2           6        -6   # BR(A_2 -> t tbar)
     3.99624663E-06    2          22        22   # BR(A_2 -> gamma gamma)
     1.17750062E-06    2          23        22   # BR(A_2 -> Z gamma)
     2.09990583E-02    2          36        25   # BR(A_2 -> A_1 H_1)
     1.09650965E-01    2          36        35   # BR(A_2 -> A_1 H_2)
     1.14387978E-01    2          23        25   # BR(A_2 -> Z H_1)
     2.24531669E-03    2          23        35   # BR(A_2 -> Z H_2)
     1.18838958E-01    2     1000022   1000022   # BR(A_2 -> neu_1 neu_1)
     6.55830057E-03    2     1000022   1000023   # BR(A_2 -> neu_1 neu_2)
     8.25804726E-02    2     1000022   1000025   # BR(A_2 -> neu_1 neu_3)
     8.22443179E-03    2     1000022   1000035   # BR(A_2 -> neu_1 neu_4)
     7.75750844E-03    2     1000023   1000023   # BR(A_2 -> neu_2 neu_2)
     1.98410204E-02    2     1000023   1000025   # BR(A_2 -> neu_2 neu_3)
     1.91429083E-03    2     1000023   1000035   # BR(A_2 -> neu_2 neu_4)
     3.35645530E-02    2     1000025   1000025   # BR(A_2 -> neu_3 neu_3)
     1.36815010E-02    2     1000025   1000035   # BR(A_2 -> neu_3 neu_4)
     3.79364871E-04    2     1000024  -1000024   # BR(A_2 -> cha_1 cha_1bar)
DECAY        37     8.12746234E+00   # Charged Higgs
     3.44705136E-06    2         -13        14   # BR(H+ -> muon nu_muon)
     9.74973596E-04    2         -15        16   # BR(H+ -> tau nu_tau)
     2.62918874E-07    2           2        -3   # BR(H+ -> u sbar)
     1.05131453E-05    2           4        -3   # BR(H+ -> c sbar)
     1.11353085E-07    2           2        -5   # BR(H+ -> u bbar)
     1.11448083E-05    2           4        -5   # BR(H+ -> c bbar)
     4.65514165E-01    2           6        -5   # BR(H+ -> t bbar)
     1.20655740E-01    2          24        25   # BR(H+ -> W+ H_1)
     2.36363436E-03    2          24        35   # BR(H+ -> W+ H_2)
     1.15979669E-01    2          24        36   # BR(H+ -> W+ A_1)
     2.30557408E-01    2     1000024   1000022   # BR(H+ -> cha_1 neu_1)
     1.87067345E-02    2     1000024   1000023   # BR(H+ -> cha_1 neu_2)
     2.99194036E-02    2     1000024   1000025   # BR(H+ -> cha_1 neu_3)
     1.53027927E-02    2     1000024   1000035   # BR(H+ -> cha_1 neu_4)
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
DECAY   1000037     2.89338195E+00   # chargino2
#                    chargino2 2-body decays
#          BR         NDA      ID1       ID2
     2.60443695E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     1.03239452E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     1.95567692E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     1.82849187E-01    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     3.53098648E-02    2     1000035        24   # BR(~chi_2+ -> ~chi_40  W+)
     5.55005688E-03    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  H_1 )
     2.16633724E-01    2     1000024        35   # BR(~chi_2+ -> ~chi_1+  H_2 )
     4.06328028E-04    2     1000024        36   # BR(~chi_2+ -> ~chi_1+  A_1 )
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1
#         PDG            Width
DECAY   1000023     2.84312197E-01   # neutralino2
#                    neutralino2 2-body decays
#          BR         NDA      ID1       ID2
     5.96607661E-01    2     1000022        23   # BR(~chi_20 -> ~chi_10   Z )
     3.04739825E-01    2     1000022        25   # BR(~chi_20 -> ~chi_10   H_1 )
     9.77177348E-02    2     1000022        35   # BR(~chi_20 -> ~chi_10   H_2 )
     9.34779145E-04    2     1000022        36   # BR(~chi_20 -> ~chi_10   A_1 )
#         PDG            Width
DECAY   1000025     1.72102368E-01   # neutralino3
#                    neutralino3 2-body decays
#          BR         NDA      ID1       ID2
     3.67309411E-01    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     9.31601624E-02    2     1000022        25   # BR(~chi_30 -> ~chi_10   H_1 )
     1.40148937E-02    2     1000022        35   # BR(~chi_30 -> ~chi_10   H_2 )
     5.25515533E-01    2     1000022        36   # BR(~chi_30 -> ~chi_10   A_1 )
#         PDG            Width
DECAY   1000035     7.84993674E-02   # neutralino4
#                    neutralino4 2-body decays
#          BR         NDA      ID1       ID2
     4.31461357E-01    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     2.27130892E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.27130892E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     3.26854193E-03    2     1000022        25   # BR(~chi_40 -> ~chi_10   H_1 )
     8.86817749E-04    2     1000022        35   # BR(~chi_40 -> ~chi_10   H_2 )
     1.10121500E-01    2     1000022        36   # BR(~chi_40 -> ~chi_10   A_1 )
#         PDG            Width
DECAY   1000045     2.89789249E+00   # neutralino5
#                    neutralino5 2-body decays
#          BR         NDA      ID1       ID2
     6.33030700E-02    2     1000022        23   # BR(~chi_50 -> ~chi_10   Z )
     7.93099049E-02    2     1000023        23   # BR(~chi_50 -> ~chi_20   Z )
     1.12579463E-01    2     1000025        23   # BR(~chi_50 -> ~chi_30   Z )
     6.89264202E-03    2     1000035        23   # BR(~chi_50 -> ~chi_40   Z )
     2.58452210E-01    2     1000024       -24   # BR(~chi_50 -> ~chi_1+   W-)
     2.58452210E-01    2    -1000024        24   # BR(~chi_50 -> ~chi_1-   W+)
     1.54545331E-03    2     1000022        25   # BR(~chi_50 -> ~chi_10   H_1 )
     3.32082314E-02    2     1000022        35   # BR(~chi_50 -> ~chi_10   H_2 )
     7.52065680E-04    2     1000022        36   # BR(~chi_50 -> ~chi_10   A_1 )
     2.17167228E-03    2     1000023        25   # BR(~chi_50 -> ~chi_20   H_1 )
     8.96596418E-02    2     1000023        35   # BR(~chi_50 -> ~chi_20   H_2 )
     6.83583300E-08    2     1000023        36   # BR(~chi_50 -> ~chi_20   A_1 )
     1.14226091E-03    2     1000025        25   # BR(~chi_50 -> ~chi_30   H_1 )
     6.51659285E-02    2     1000025        35   # BR(~chi_50 -> ~chi_30   H_2 )
     1.54672805E-04    2     1000025        36   # BR(~chi_50 -> ~chi_30   A_1 )
     5.82714516E-04    2     1000035        25   # BR(~chi_50 -> ~chi_40   H_1 )
     2.66169017E-02    2     1000035        35   # BR(~chi_50 -> ~chi_40   H_2 )
     1.08889113E-05    2     1000035        36   # BR(~chi_50 -> ~chi_40   A_1 )
#         PDG            Width
DECAY   1000021     1.50492085E+00   # gluino
#                    gluino 2-body decays
#          BR         NDA      ID1       ID2
     4.14806170E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     4.14806170E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     4.34270721E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     4.34270721E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     4.58721269E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     4.58721269E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     4.47621889E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     4.47621889E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     4.14806170E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     4.14806170E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     4.34270721E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     4.34270721E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     4.58721269E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     4.58721269E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     4.47621889E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     4.47621889E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     5.05940575E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     5.05940575E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.44072421E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.44072421E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
#                    gluino 3-body decays
#           BR         NDA      ID1       ID2       ID3
     1.78398938E-02    3     1000022         6        -6   # BR(~g -> ~chi_10 t  tb)
     2.93188338E-02    3     1000023         6        -6   # BR(~g -> ~chi_20 t  tb)
     3.20861735E-02    3     1000025         6        -6   # BR(~g -> ~chi_30 t  tb)
     1.02021843E-02    3     1000035         6        -6   # BR(~g -> ~chi_40 t  tb)
     1.83956771E-03    3     1000045         6        -6   # BR(~g -> ~chi_50 t  tb)
     1.57974377E-02    3     1000024         5        -6   # BR(~g -> ~chi_1+ b  tb)
     1.57974377E-02    3    -1000024         6        -5   # BR(~g -> ~chi_1- t  bb)
     2.44249691E-03    3     1000037         5        -6   # BR(~g -> ~chi_2+ b  tb)
     2.44249691E-03    3    -1000037         6        -5   # BR(~g -> ~chi_2- t  bb)
     3.14295022E-05    3     1000006        -5       -24   # BR(~g -> ~t_1    bb W-)
     3.14295022E-05    3    -1000006         5        24   # BR(~g -> ~t_1*   b  W+)
#         PDG            Width
DECAY   1000011     5.78662403E+00   # selectron_L
#                    selectron_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06853323E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)   
     1.09569568E-03    2     1000023        11   # BR(~e_L -> ~chi_20 e-)   
     1.30819980E-03    2     1000025        11   # BR(~e_L -> ~chi_30 e-)  
     2.02128203E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)  
     2.59433476E-01    2     1000045        11   # BR(~e_L -> ~chi_50 e-)  
     1.25739953E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.35601833E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#         PDG            Width
DECAY   2000011     4.32983866E+00   # selectron_R
#                    selectron_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457496E-03    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     5.09644915E-03    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     4.35807383E-02    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     9.48925405E-01    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
     1.02832976E-04    2     1000045        11   # BR(~e_R -> ~chi_50 e-)
#         PDG            Width
DECAY   1000013     5.78662403E+00   # smuon_L
#                    smuon_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06853323E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.09569568E-03    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.30819980E-03    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.02128203E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     2.59433476E-01    2     1000045        13   # BR(~mu_L -> ~chi_50 mu-)
     1.25739953E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.35601833E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#         PDG            Width
DECAY   2000013     4.32983866E+00   # smuon_R
#                    smuon_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457496E-03    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     5.09644915E-03    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     4.35807383E-02    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     9.48925405E-01    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
     1.02832976E-04    2     1000045        13   # BR(~mu_R -> ~chi_50 mu-)
#         PDG            Width
DECAY   1000015     5.03148840E+00   # stau_1
#                    stau1 2-body decays
#          BR         NDA      ID1       ID2
     1.14216997E-03    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     4.79647518E-04    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     2.71122710E-02    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     5.31284575E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.43325762E-01    2     1000045        15   # BR(~tau_1 -> ~chi_50  tau-)
     8.82543233E-04    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     2.95773031E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   2000015     4.34590503E+00   # stau_2
#                    stau_2 2-body decays
#          BR         NDA      ID1       ID2
     1.37399146E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     9.20714106E-03    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     1.68760193E-02    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     5.99548356E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     1.79539706E-01    2     1000045        15   # BR(~tau_2 -> ~chi_50  tau-)
     2.39234895E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     3.70602144E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
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
DECAY   1000002     5.73690105E+00   # sup_L
#                    sup_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251773E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.97343582E-03    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     5.95852778E-04    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     2.97748109E-02    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     3.11048066E-01    2     1000045         2   # BR(~u_L -> ~chi_50 u)
     3.75280130E-02    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.17084569E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#         PDG            Width
DECAY   2000002     1.99702767E+00   # sup_R
#                    sup_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404072E-03    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     5.02648425E-03    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     4.29887116E-02    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     9.49644059E-01    2     1000035         2   # BR(~u_R -> ~chi_40 u)
     1.16703912E-04    2     1000045         2   # BR(~u_R -> ~chi_50 u)
#         PDG            Width
DECAY   1000001     5.64341612E+00   # sdown_L
#                    sdown_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434162E-03    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     5.79758632E-03    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     7.45741594E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     1.34387643E-02    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     3.21776483E-01    2     1000045         1   # BR(~d_L -> ~chi_50 d)
     1.31720070E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.49293689E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#         PDG            Width
DECAY   2000001     4.99627919E-01   # sdown_R
#                    sdown_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360754E-03    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     5.02599175E-03    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     4.29845406E-02    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     9.49649027E-01    2     1000035         1   # BR(~d_R -> ~chi_40 d)
     1.16832591E-04    2     1000045         1   # BR(~d_R -> ~chi_50 d)
#         PDG            Width
DECAY   1000004     5.73690105E+00   # scharm_L
#                    scharm_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251773E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.97343582E-03    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     5.95852778E-04    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     2.97748109E-02    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     3.11048066E-01    2     1000045         4   # BR(~c_L -> ~chi_50 c)
     3.75280130E-02    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.17084569E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#         PDG            Width
DECAY   2000004     1.99702767E+00   # scharm_R
#                    scharm_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404072E-03    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     5.02648425E-03    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     4.29887116E-02    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     9.49644059E-01    2     1000035         4   # BR(~c_R -> ~chi_40 c)
     1.16703912E-04    2     1000045         4   # BR(~c_R -> ~chi_50 c)
#         PDG            Width
DECAY   1000003     5.64341612E+00   # sstrange_L
#                    sstrange_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434162E-03    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     5.79758632E-03    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     7.45741594E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     1.34387643E-02    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     3.21776483E-01    2     1000045         3   # BR(~s_L -> ~chi_50 s)
     1.31720070E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.49293689E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#         PDG            Width
DECAY   2000003     4.99627919E-01   # sstrange_R
#                    sstrange_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360754E-03    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     5.02599175E-03    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     4.29845406E-02    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     9.49649027E-01    2     1000035         3   # BR(~s_R -> ~chi_40 s)
     1.16832591E-04    2     1000045         3   # BR(~s_R -> ~chi_50 s)
#         PDG            Width
DECAY   1000006     2.19407747E+01   # stop1
#                    stop1 2-body decays
#          BR         NDA      ID1       ID2
     1.09848701E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     1.96142419E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     2.17504690E-01    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     8.77641707E-02    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.58153437E-02    2     1000045         6   # BR(~t_1 -> ~chi_50 t )
     2.51894158E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     9.10305179E-02    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#         PDG            Width
DECAY   2000006     3.20876203E+01   # stop2
#                    stop2 2-body decays
#          BR         NDA      ID1       ID2
     1.11134191E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.29489661E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     2.08025878E-01    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     2.99625236E-02    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     2.13349826E-02    2     1000045         6   # BR(~t_2 -> ~chi_50 t )
     3.27000103E-01    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.69765302E-02    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.08240119E-08    2     1000006        25   # BR(~t_2 -> ~t_1    H1 )
     3.72868578E-07    2     1000006        35   # BR(~t_2 -> ~t_1    H2 )
     1.02269189E-12    2     1000006        36   # BR(~t_2 -> ~t_1    A1 )
     3.37060675E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
     1.34421888E-03    2     1000005        24   # BR(~t_2 -> ~b_1    W+)
     1.02540104E-03    2     2000005        24   # BR(~t_2 -> ~b_2    W+)
#         PDG            Width
DECAY   1000005     7.88780010E+00   # sbottom1
#                    sbottom1 2-body decays
#          BR         NDA      ID1       ID2
     5.94727896E-04    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.58879659E-04    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     1.03931684E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     3.90223636E-02    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     7.88086248E-02    2     1000045         5   # BR(~b_1 -> ~chi_50 b )
     7.01617061E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     1.69405175E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
#         PDG            Width
DECAY   2000005     1.27428461E+01   # sbottom2
#                    sbottom2 2-body decays
#          BR         NDA      ID1       ID2
     6.43939555E-04    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     4.83554195E-03    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     6.50783760E-04    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.82291522E-02    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     8.44752578E-02    2     1000045         5   # BR(~b_2 -> ~chi_50 b )
     7.08865678E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     1.81714075E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
#
# Dummy alpha block (for Prospino compatibility only - not used)
BLOCK ALPHA
	0.1000E+00
"""

  f = open("%s/src/WorkingPoint_mH1_90_mH2_125p3_MSUSY_1000.slha" % os.environ['CMSSW_BASE'],"w")
  f.write(slhacontent)
  f.close()
  
  return process