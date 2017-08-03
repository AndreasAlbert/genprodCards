COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2H2bbbar = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     2.50000000E+01   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.50800000E+03   # At
        12     1.50800000E+03   # Ab
        13     1.50800000E+03   # Atau
        23     2.00000000E+02   # MUE
        25     2.50000000E+01   # TB
        26     1.00000000E+03   # MA0
        27     1.00322671E+03   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95838375E+02   # MSf(1,1,1)
   1000011     5.02293635E+02   # MSf(1,2,1)
   2000011     5.01842018E+02   # MSf(2,2,1)
   1000002     1.49902834E+03   # MSf(1,3,1)
   2000002     1.49958985E+03   # MSf(2,3,1)
   1000001     1.50117603E+03   # MSf(1,4,1)
   2000001     1.50020494E+03   # MSf(2,4,1)
   1000014     4.95838375E+02   # MSf(1,1,2)
   1000013     5.02640084E+02   # MSf(1,2,2)
   2000013     5.01495040E+02   # MSf(2,2,2)
   1000004     1.49902888E+03   # MSf(1,3,2)
   2000004     1.49959042E+03   # MSf(2,3,2)
   1000003     1.50119986E+03   # MSf(1,4,2)
   2000003     1.50018109E+03   # MSf(2,4,2)
   1000016     9.97925696E+02   # MSf(1,1,3)
   1000015     9.97930750E+02   # MSf(1,2,3)
   2000015     1.00413388E+03   # MSf(2,2,3)
   1000006     8.76427249E+02   # MSf(1,3,3)
   2000006     1.13478079E+03   # MSf(2,3,3)
   1000005     9.94259418E+02   # MSf(1,4,3)
   2000005     1.00778084E+03   # MSf(2,4,3)
        25     1.24986406E+02   # Mh0
        35     9.99818368E+02   # MHH
        36     1.00000000E+03   # MA0
        37     1.00342454E+03   # MHp
   1000022     8.81217311E+01   # MNeu(1)
   1000023     1.51770777E+02   # MNeu(2)
   1000025    -2.10328954E+02   # MNeu(3)
   1000035     2.65908097E+02   # MNeu(4)
   1000024     1.48224451E+02   # MCha(1)
   1000037     2.66377906E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     7.01480357E-01   # Delta Mh0
        35     5.57777544E-03   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     1.06641411E-02   # Delta MHp
BLOCK NMIX
     1   1     9.31988478E-01   # ZNeu(1,1)
     1   2    -1.14406215E-01   # ZNeu(1,2)
     1   3     3.11018111E-01   # ZNeu(1,3)
     1   4    -1.46889171E-01   # ZNeu(1,4)
     2   1    -3.18015719E-01   # ZNeu(2,1)
     2   2    -6.93652772E-01   # ZNeu(2,2)
     2   3     5.10771151E-01   # ZNeu(2,3)
     2   4    -3.96010941E-01   # ZNeu(2,4)
     3   1     9.68557338E-02   # ZNeu(3,1)
     3   2    -1.34875686E-01   # ZNeu(3,2)
     3   3    -6.78023080E-01   # ZNeu(3,3)
     3   4    -7.16039258E-01   # ZNeu(3,4)
     4   1    -1.44507597E-01   # ZNeu(4,1)
     4   2     6.98258977E-01   # ZNeu(4,2)
     4   3     4.27393577E-01   # ZNeu(4,3)
     4   4    -5.55775752E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.07017863E-01   # UCha(1,1)
     1   2     7.94688187E-01   # UCha(1,2)
     2   1     7.94688187E-01   # UCha(2,1)
     2   2     6.07017863E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.94688187E-01   # VCha(1,1)
     1   2     6.07017863E-01   # VCha(1,2)
     2   1     6.07017863E-01   # VCha(2,1)
     2   2     7.94688187E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     6.94077482E-01   # USf(1,1)
     1   2     7.19900305E-01   # USf(1,2)
     2   1     7.19900305E-01   # USf(2,1)
     2   2    -6.94077482E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08251522E-01   # USf(1,1)
     1   2    -7.05960185E-01   # USf(1,2)
     2   1     7.05960185E-01   # USf(2,1)
     2   2     7.08251522E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     6.67964822E-01   # USf(1,1)
     1   2     7.44192849E-01   # USf(1,2)
     2   1     7.44192849E-01   # USf(2,1)
     2   2    -6.67964822E-01   # USf(2,2)
BLOCK ALPHA
              -4.10978365E-02   # Alpha
BLOCK DALPHA
               2.02982871E-05   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     2.50000000E+01   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50800000E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50800000E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50800000E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     7.34341041E-05   # Yf(1,1)
     2   2     1.51838424E-02   # Yf(2,2)
     3   3     2.55371598E-01   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.72448364E-05   # Yf(1,1)
     2   2     7.39228656E-03   # Yf(2,2)
     3   3     9.95601891E-01   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     8.40743677E-04   # Yf(1,1)
     2   2     1.33110713E-02   # Yf(2,2)
     3   3     5.53780613E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     3.85100369E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.50136765E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     8.35101165E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99984128E-01   # UASf(1,1)
     1   4    -5.63422645E-03   # UASf(1,4)
     2   2     8.34980634E-01   # UASf(2,2)
     2   5    -5.50279330E-01   # UASf(2,5)
     3   3     6.94077482E-01   # UASf(3,3)
     3   6     7.19900305E-01   # UASf(3,6)
     4   1     5.63422645E-03   # UASf(4,1)
     4   4     9.99984128E-01   # UASf(4,4)
     5   2     5.50279330E-01   # UASf(5,2)
     5   5     8.34980634E-01   # UASf(5,5)
     6   3     7.19900305E-01   # UASf(6,3)
     6   6    -6.94077482E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     1.00000000E+00   # UASf(1,1)
     1   4     1.42539883E-05   # UASf(1,4)
     2   2     9.99981335E-01   # UASf(2,2)
     2   5     6.10986751E-03   # UASf(2,5)
     3   3     7.08251522E-01   # UASf(3,3)
     3   6    -7.05960185E-01   # UASf(3,6)
     4   1    -1.42539883E-05   # UASf(4,1)
     4   4     1.00000000E+00   # UASf(4,4)
     5   2    -6.10986751E-03   # UASf(5,2)
     5   5     9.99981335E-01   # UASf(5,5)
     6   3     7.05960185E-01   # UASf(6,3)
     6   6     7.08251522E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99949630E-01   # UASf(1,1)
     1   4    -1.00368449E-02   # UASf(1,4)
     2   2     9.88183453E-01   # UASf(2,2)
     2   5    -1.53275777E-01   # UASf(2,5)
     3   3     6.67964822E-01   # UASf(3,3)
     3   6     7.44192849E-01   # UASf(3,6)
     4   1     1.00368449E-02   # UASf(4,1)
     4   4     9.99949630E-01   # UASf(4,4)
     5   2     1.53275777E-01   # UASf(5,2)
     5   5     9.88183453E-01   # UASf(5,5)
     6   3     7.44192849E-01   # UASf(6,3)
     6   6    -6.67964822E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.99999898E-01   # UH(1,1)
     1   2     4.51640379E-04   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -4.51640379E-04   # UH(2,1)
     2   2     9.99999898E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     3.95306353E-03   # Gamma(h0)
     2.33168729E-03   2        22        22   # BR(h0 -> photon photon)
     1.49039816E-03   2        22        23   # BR(h0 -> photon Z)
     2.70965064E-02   2        23        23   # BR(h0 -> Z Z)
     2.23898013E-01   2       -24        24   # BR(h0 -> W W)
     7.15670371E-02   2        21        21   # BR(h0 -> gluon gluon)
     5.32302468E-09   2       -11        11   # BR(h0 -> Electron electron)
     2.36777569E-04   2       -13        13   # BR(h0 -> Muon muon)
     6.80579527E-02   2       -15        15   # BR(h0 -> Tau tau)
     2.03909025E-07   2        -2         2   # BR(h0 -> Up up)
     2.82434959E-02   2        -4         4   # BR(h0 -> Charm charm)
     8.72280685E-07   2        -1         1   # BR(h0 -> Down down)
     2.19058558E-04   2        -3         3   # BR(h0 -> Strange strange)
     5.76857992E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     1.92709269E+01   # Gamma(HH)
    -3.49280339E-07   2        22        22   # BR(HH -> photon photon)
    -1.14439230E-06   2        22        23   # BR(HH -> photon Z)
    -1.36330416E-05   2        23        23   # BR(HH -> Z Z)
    -1.83033879E-05   2       -24        24   # BR(HH -> W W)
    -1.64147791E-05   2        21        21   # BR(HH -> gluon gluon)
    -5.15887851E-09   2       -11        11   # BR(HH -> Electron electron)
     2.29620033E-04   2       -13        13   # BR(HH -> Muon muon)
    -6.47888134E-02   2       -15        15   # BR(HH -> Tau tau)
    -3.59730084E-13   2        -2         2   # BR(HH -> Up up)
    -4.97942717E-08   2        -4         4   # BR(HH -> Charm charm)
    -3.00652044E-03   2        -6         6   # BR(HH -> Top top)
    -5.63056100E-07   2        -1         1   # BR(HH -> Down down)
    -1.41399558E-04   2        -3         3   # BR(HH -> Strange strange)
    -3.38764654E-01   2        -5         5   # BR(HH -> Bottom bottom)
    -1.40450325E-01   2  -1000024   1000024   # BR(HH -> Chargino1 chargino1)
    -9.53759698E-02   2  -1000037   1000024   # BR(HH -> Chargino2 chargino1)
    -9.53759698E-02   2  -1000024   1000037   # BR(HH -> Chargino1 chargino2)
    -3.01670030E-02   2  -1000037   1000037   # BR(HH -> Chargino2 chargino2)
    -1.41557372E-02   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)
    -4.15076487E-02   2   1000022   1000023   # BR(HH -> neutralino1 neutralino2)
    -2.81220964E-02   2   1000022   1000025   # BR(HH -> neutralino1 neutralino3)
    -2.26597848E-05   2   1000022   1000035   # BR(HH -> neutralino1 neutralino4)
    -2.45954378E-02   2   1000023   1000023   # BR(HH -> neutralino2 neutralino2)
    -1.52081429E-02   2   1000023   1000025   # BR(HH -> neutralino2 neutralino3)
    -4.66460765E-03   2   1000023   1000035   # BR(HH -> neutralino2 neutralino4)
    -5.52856840E-03   2   1000025   1000025   # BR(HH -> neutralino3 neutralino3)
    -7.23695652E-02   2   1000025   1000035   # BR(HH -> neutralino3 neutralino4)
    -2.53693879E-02   2   1000035   1000035   # BR(HH -> neutralino4 neutralino4)
    -1.03510266E-04   2        25        25   # BR(HH -> h0 h0)
DECAY        36     1.91106666E+01   # Gamma(A0)
     6.25259146E-07   2        22        22   # BR(A0 -> photon photon)
     1.32221507E-06   2        22        23   # BR(A0 -> photon Z)
     4.54854662E-05   2        21        21   # BR(A0 -> gluon gluon)
     5.09503891E-09   2       -11        11   # BR(A0 -> Electron electron)
     2.26778705E-04   2       -13        13   # BR(A0 -> Muon muon)
     6.39880633E-02   2       -15        15   # BR(A0 -> Tau tau)
     3.40809016E-13   2        -2         2   # BR(A0 -> Up up)
     4.71727335E-08   2        -4         4   # BR(A0 -> Charm charm)
     3.25979831E-03   2        -6         6   # BR(A0 -> Top top)
     5.56077613E-07   2        -1         1   # BR(A0 -> Down down)
     1.39647039E-04   2        -3         3   # BR(A0 -> Strange strange)
     3.34586999E-01   2        -5         5   # BR(A0 -> Bottom bottom)
     1.70754291E-01   2  -1000024   1000024   # BR(A0 -> Chargino1 chargino1)
     6.86965242E-02   2  -1000037   1000024   # BR(A0 -> Chargino2 chargino1)
     6.86965242E-02   2  -1000024   1000037   # BR(A0 -> Chargino1 chargino2)
     5.61603958E-02   2  -1000037   1000037   # BR(A0 -> Chargino2 chargino2)
     1.59103425E-02   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)
     4.93426196E-02   2   1000022   1000023   # BR(A0 -> neutralino1 neutralino2)
     2.12280059E-02   2   1000022   1000025   # BR(A0 -> neutralino1 neutralino3)
     1.70789722E-04   2   1000022   1000035   # BR(A0 -> neutralino1 neutralino4)
     3.09938136E-02   2   1000023   1000023   # BR(A0 -> neutralino2 neutralino2)
     1.01013791E-02   2   1000023   1000025   # BR(A0 -> neutralino2 neutralino3)
     5.71221005E-03   2   1000023   1000035   # BR(A0 -> neutralino2 neutralino4)
     5.70914583E-03   2   1000025   1000025   # BR(A0 -> neutralino3 neutralino3)
     5.01683526E-02   2   1000025   1000035   # BR(A0 -> neutralino3 neutralino4)
     4.40862954E-02   2   1000035   1000035   # BR(A0 -> neutralino4 neutralino4)
     1.99829703E-05   2        23        25   # BR(A0 -> Z h0)
     7.02935993E-37   2        25        25   # BR(A0 -> h0 h0)
DECAY        37     1.88917620E+01   # Gamma(Hp)
     5.49417484E-09   2       -11        12   # BR(Hp -> Electron nu_e)
     2.34893089E-04   2       -13        14   # BR(Hp -> Muon nu_mu)
     6.64430159E-02   2       -15        16   # BR(Hp -> Tau nu_tau)
     5.45327673E-07   2        -1         2   # BR(Hp -> Down up)
     6.30096083E-06   2        -3         2   # BR(Hp -> Strange up)
     3.62567848E-06   2        -5         2   # BR(Hp -> Bottom up)
     2.74066667E-08   2        -1         4   # BR(Hp -> Down charm)
     1.36513974E-04   2        -3         4   # BR(Hp -> Strange charm)
     5.07723293E-04   2        -5         4   # BR(Hp -> Bottom charm)
     2.38336731E-07   2        -1         6   # BR(Hp -> Down top)
     5.38498464E-06   2        -3         6   # BR(Hp -> Strange top)
     3.32654434E-01   2        -5         6   # BR(Hp -> Bottom top)
     6.71805323E-02   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)
     2.48430913E-03   2   1000022   1000037   # BR(Hp -> neutralino1 chargino2)
     1.21993270E-02   2   1000023   1000024   # BR(Hp -> neutralino2 chargino1)
     2.16341996E-01   2   1000023   1000037   # BR(Hp -> neutralino2 chargino2)
     8.01226891E-02   2   1000024   1000025   # BR(Hp -> chargino1 neutralino3)
     8.65443180E-02   2   1000025   1000037   # BR(Hp -> neutralino3 chargino2)
     1.33422506E-01   2   1000024   1000035   # BR(Hp -> chargino1 neutralino4)
     1.68923724E-03   2   1000035   1000037   # BR(Hp -> neutralino4 chargino2)
     2.05527982E-05   2        24        25   # BR(Hp -> W h0)
     4.37608985E-11   2        24        35   # BR(Hp -> W HH)
     3.38014489E-11   2        24        36   # BR(Hp -> W A0)
     2.81412711E-11   2  -1000011   1000012   # BR(Hp -> Selectron1 snu_e1)
     9.14101925E-07   2  -2000011   1000012   # BR(Hp -> Selectron2 snu_e1)
     2.60862777E-07   2  -1000013   1000014   # BR(Hp -> Smuon1 snu_mu1)
     6.49169128E-07   2  -2000013   1000014   # BR(Hp -> Smuon2 snu_mu1)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)
