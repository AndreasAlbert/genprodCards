import sys
import os
import subprocess
import time
import datetime
import stat
import ROOT

def generate_sample_directories(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay):
    cwd = os.getcwd()
    if not os.path.exists(cwd+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay):
        os.makedirs(cwd+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay)
        
def generate_customizecards(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay): 
    
    if  Gstar_width == "Nar":
        Gstar_mass_width=Gstar_mass*0.01
    else:
        Gstar_mass_width=Gstar_mass*0.3
       
    if  Tp_width == "Nar":
        Tp_mass_width=Tp_mass*0.01
    else:
        Tp_mass_width=Tp_mass*0.3       
       
    script=""
    script+="""set param_card frblock 4 """+str(float(Tp_mass))+"""
set param_card mass 9000010 """+str(float(Gstar_mass))+"""
set param_card mass 9000001 """+str(float(Tp_mass))+"""
set param_card mass 9000002 """+str(float(Tp_mass))+"""
set param_card mass 9000003 """+str(float(Tp_mass))+"""
set param_card mass 9000004 """+str(float(Tp_mass))+"""
set param_card DECAY 9000001 """+str(Tp_mass_width)+"""
set param_card DECAY 9000002 """+str(Tp_mass_width)+"""
set param_card DECAY 9000003 """+str(Tp_mass_width)+"""
set param_card DECAY 9000004 """+str(Tp_mass_width)+"""
set param_card DECAY 9000010 """+str(Gstar_mass_width)
    
    
    f=open("ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"_customizecards.dat","w")
    f.write(script)
    f.close()
    
def generate_extramodels(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay):
    script="Gstar_UFO.zip"
    
    f=open("ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"_extramodels.dat","w")
    f.write(script)
    f.close()

def generate_madspin_card(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay):
    script="""set ms_dir ./madspingrid
set max_running_process 1
set Nevents_for_max_weigth 250
set max_weight_ps_point 400
decay t > w+ b, w+ > all all
decay t~ > w- b~, w- > all all
launch"""
    
    f=open("ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"_madspin_card.dat","w")
    f.write(script)
    f.close()

def generate_proc_card(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay):
    script="""set group_subprocesses Auto
import model Gstar_UFO"""

    if Tp_decay=="Ht":
        script+="""
generate p p > kkg ts > t~ t h
add process p p > kkg ts~ > t~ t h"""
    elif Tp_decay=="Zt":
        script+="""
generate p p > kkg ts > t~ t z
add process p p > kkg ts~ > t~ t z"""
    elif Tp_decay=="Wb":
        script+="""
generate p p > kkg ts > t~ w+ b
add process p p > kkg ts~ > w- b~ t"""
    script+="""
output ZpTpt_Zp"""+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality
    
    f=open("ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"_proc_card.dat","w")
    f.write(script)
    f.close()

    f=open("ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"_run_card.dat","w")
    f.write(script)
    f.close()
    

def generate_run_card(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay):
    script="""#*********************************************************************  
#                       MadGraph5_aMC@NLO                            *
#                                                                    *
#                     run_card.dat MadEvent                          *
#                                                                    *
#  This file is used to set the parameters of the run.               *
#                                                                    *
#  Some notation/conventions:                                        *
#                                                                    *
#   Lines starting with a '# ' are info or comments                  *
#                                                                    *
#   mind the format:   value    = variable     ! comment             *
#*********************************************************************
#
#*******************                                                 
# Running parameters
#*******************                                                 
#                                                                    
#*********************************************************************
# Tag name for the run (one word)                                    *
#*********************************************************************
  tag_1     = run_tag ! name of the run 
#*********************************************************************
# Run to generate the grid pack                                      *
#*********************************************************************
  .false.     = gridpack  !True = setting up the grid pack
#*********************************************************************
# Number of events and rnd seed                                      *
# Warning: Do not generate more than 1M events in a single run       *
# If you want to run Pythia, avoid more than 50k events in a run.    *
#*********************************************************************
  1000 = nevents ! Number of unweighted events requested 
      0       = iseed   ! rnd seed (0=assigned automatically=default))
#*********************************************************************
# Collider type and energy                                           *
# lpp: 0=No PDF, 1=proton, -1=antiproton, 2=photon from proton,      *
#                                         3=photon from electron     *
#*********************************************************************
        1     = lpp1    ! beam 1 type 
        1     = lpp2    ! beam 2 type
     6500     = ebeam1  ! beam 1 total energy in GeV
     6500     = ebeam2  ! beam 2 total energy in GeV
#*********************************************************************
# Beam polarization from -100 (left-handed) to 100 (right-handed)    *
#*********************************************************************
        0     = polbeam1 ! beam polarization for beam 1
        0     = polbeam2 ! beam polarization for beam 2
#*********************************************************************
# PDF CHOICE: this automatically fixes also alpha_s and its evol.    *
#*********************************************************************
# 'cteq6l1'    = pdlabel     ! PDF set (lhapdf for using lhapdf)
#  10042       = lhaid      ! PDF number used ONLY for LHAPDF
 'lhapdf'   = pdlabel   ! PDF set                                  
  263400    = lhaid     ! if pdlabel=lhapdf, this is the lhapdf number 
#*********************************************************************
# Renormalization and factorization scales                           *
#*********************************************************************
 F        = fixed_ren_scale  ! if .true. use fixed ren scale
 F        = fixed_fac_scale  ! if .true. use fixed fac scale
 91.1880  = scale            ! fixed ren scale
 91.1880  = dsqrt_q2fact1    ! fixed fact scale for pdf1
 91.1880  = dsqrt_q2fact2    ! fixed fact scale for pdf2
 1        = scalefact        ! scale factor for event-by-event scales
#*********************************************************************
# Matching - Warning! ickkw > 1 is still beta
#*********************************************************************
 0        = ickkw            ! 0 no matching, 1 MLM, 2 CKKW matching
 1        = highestmult      ! for ickkw=2, highest mult group
 1        = ktscheme         ! for ickkw=1, 1 Durham kT, 2 Pythia pTE
 1        = alpsfact         ! scale factor for QCD emission vx
 F        = chcluster        ! cluster only according to channel diag
 T        = pdfwgt           ! for ickkw=1, perform pdf reweighting
 5        = asrwgtflavor     ! highest quark flavor for a_s reweight
 T        = clusinfo         ! include clustering tag in output
 3.0      = lhe_version      ! Change the way clustering information pass to shower.
#*********************************************************************
#**********************************************************
#
#**********************************************************
# Automatic ptj and mjj cuts if xqcut > 0
# (turn off for VBF and single top processes)
#**********************************************************
   T  = auto_ptj_mjj  ! Automatic setting of ptj and mjj
#**********************************************************
#                                                                    
#**********************************
# BW cutoff (M+/-bwcutoff*Gamma)
#**********************************
  15  = bwcutoff      ! (M+/-bwcutoff*Gamma)
#**********************************************************
# Apply pt/E/eta/dr/mij cuts on decay products or not
# (note that etmiss/ptll/ptheavy/ht/sorted cuts always apply)
#**********************************************************
   F  = cut_decays    ! Cut decay products
#*************************************************************
# Number of helicities to sum per event (0 = all helicities)
# 0 gives more stable result, but longer run time (needed for
# long decay chains e.g.).
# Use >=2 if most helicities contribute, e.g. pure QCD.
#*************************************************************
   0  = nhel          ! Number of helicities used per event
#*******************                                                 
# Standard Cuts
#*******************                                                 
#                                                                    
#*********************************************************************
# Minimum and maximum pt's (for max, -1 means no cut)                *
#*********************************************************************
  10 = ptj       ! minimum pt for the jets
  10 = ptb       ! minimum pt for the b
  0  = pta       ! minimum pt for the photons
  0  = ptl       ! minimum pt for the charged leptons
  0  = misset    ! minimum missing Et (sum of neutrino's momenta)
  0  = ptheavy   ! minimum pt for one heavy final state
 1.0 = ptonium   ! minimum pt for the quarkonium states
 -1  = ptjmax    ! maximum pt for the jets
 -1  = ptbmax    ! maximum pt for the b
 -1  = ptamax    ! maximum pt for the photons
 -1  = ptlmax    ! maximum pt for the charged leptons
 -1  = missetmax ! maximum missing Et (sum of neutrino's momenta)
#*********************************************************************
# Minimum and maximum E's (in the center of mass frame)              *
#*********************************************************************
  0  = ej     ! minimum E for the jets 
  0  = eb     ! minimum E for the b 
  0  = ea     ! minimum E for the photons 
  0  = el     ! minimum E for the charged leptons 
 -1   = ejmax ! maximum E for the jets
 -1   = ebmax ! maximum E for the b
 -1   = eamax ! maximum E for the photons
 -1   = elmax ! maximum E for the charged leptons
#*********************************************************************
# Maximum and minimum absolute rapidity (for max, -1 means no cut)   *
#*********************************************************************
   5  = etaj    ! max rap for the jets
   5  = etab    ! max rap for the b
 2.5  = etaa    ! max rap for the photons
  -1  = etal    ! max rap for the charged leptons
 0.6  = etaonium ! max rap for the quarkonium states
   0  = etajmin ! min rap for the jets
   0  = etabmin ! min rap for the b
   0  = etaamin ! min rap for the photons
   0  = etalmin ! main rap for the charged leptons
#*********************************************************************
# Minimum and maximum DeltaR distance                                *
#*********************************************************************
 0   = drjj    ! min distance between jets
 0.01   = drbb    ! min distance between b's
 0   = drll    ! min distance between leptons
 0   = draa    ! min distance between gammas
 0.01   = drbj    ! min distance between b and jet
 0   = draj    ! min distance between gamma and jet
 0   = drjl    ! min distance between jet and lepton
 0   = drab    ! min distance between gamma and b 
 0   = drbl    ! min distance between b and lepton
 0   = dral    ! min distance between gamma and lepton
 -1  = drjjmax ! max distance between jets
 -1  = drbbmax ! max distance between b's
 -1  = drllmax ! max distance between leptons
 -1  = draamax ! max distance between gammas
 -1  = drbjmax ! max distance between b and jet
 -1  = drajmax ! max distance between gamma and jet
 -1  = drjlmax ! max distance between jet and lepton
 -1  = drabmax ! max distance between gamma and b
 -1  = drblmax ! max distance between b and lepton
 -1  = dralmax ! maxdistance between gamma and lepton
#*********************************************************************
# Minimum and maximum invariant mass for pairs                       *
# WARNING: for four lepton final state mmll cut require to have      *
#          different lepton masses for each flavor!                  *           
#*********************************************************************
 0   = mmjj    ! min invariant mass of a jet pair 
 0   = mmbb    ! min invariant mass of a b pair 
 0   = mmaa    ! min invariant mass of gamma gamma pair
 0   = mmll    ! min invariant mass of l+l- (same flavour) lepton pair
 -1  = mmjjmax ! max invariant mass of a jet pair
 -1  = mmbbmax ! max invariant mass of a b pair
 -1  = mmaamax ! max invariant mass of gamma gamma pair
 -1  = mmllmax ! max invariant mass of l+l- (same flavour) lepton pair
#*********************************************************************
# Minimum and maximum invariant mass for all letpons                 *
#*********************************************************************
 0   = mmnl    ! min invariant mass for all letpons (l+- and vl) 
 -1  = mmnlmax ! max invariant mass for all letpons (l+- and vl) 
#*********************************************************************
# Minimum and maximum pt for 4-momenta sum of leptons                *
#*********************************************************************
 0   = ptllmin  ! Minimum pt for 4-momenta sum of leptons(l and vl)
 -1  = ptllmax  ! Maximum pt for 4-momenta sum of leptons(l and vl)
#*********************************************************************
# Inclusive cuts                                                     *
#*********************************************************************
 0  = xptj ! minimum pt for at least one jet  
 0  = xptb ! minimum pt for at least one b 
 0  = xpta ! minimum pt for at least one photon 
 0  = xptl ! minimum pt for at least one charged lepton 
#*********************************************************************
# Control the pt's of the jets sorted by pt                          *
#*********************************************************************
 0   = ptj1min ! minimum pt for the leading jet in pt
 0   = ptj2min ! minimum pt for the second jet in pt
 0   = ptj3min ! minimum pt for the third jet in pt
 0   = ptj4min ! minimum pt for the fourth jet in pt
 -1  = ptj1max ! maximum pt for the leading jet in pt 
 -1  = ptj2max ! maximum pt for the second jet in pt
 -1  = ptj3max ! maximum pt for the third jet in pt
 -1  = ptj4max ! maximum pt for the fourth jet in pt
 0   = cutuse  ! reject event if fails any (0) / all (1) jet pt cuts
#*********************************************************************
# Control the pt's of leptons sorted by pt                           *
#*********************************************************************
 0   = ptl1min ! minimum pt for the leading lepton in pt
 0   = ptl2min ! minimum pt for the second lepton in pt
 0   = ptl3min ! minimum pt for the third lepton in pt
 0   = ptl4min ! minimum pt for the fourth lepton in pt
 -1  = ptl1max ! maximum pt for the leading lepton in pt 
 -1  = ptl2max ! maximum pt for the second lepton in pt
 -1  = ptl3max ! maximum pt for the third lepton in pt
 -1  = ptl4max ! maximum pt for the fourth lepton in pt
#*********************************************************************
# Control the Ht(k)=Sum of k leading jets                            *
#*********************************************************************
 0   = htjmin ! minimum jet HT=Sum(jet pt)
 -1  = htjmax ! maximum jet HT=Sum(jet pt)
 0   = ihtmin  !inclusive Ht for all partons (including b)
 -1  = ihtmax  !inclusive Ht for all partons (including b)
 0   = ht2min ! minimum Ht for the two leading jets
 0   = ht3min ! minimum Ht for the three leading jets
 0   = ht4min ! minimum Ht for the four leading jets
 -1  = ht2max ! maximum Ht for the two leading jets
 -1  = ht3max ! maximum Ht for the three leading jets
 -1  = ht4max ! maximum Ht for the four leading jets
#***********************************************************************
# Photon-isolation cuts, according to hep-ph/9801442                   *
# When ptgmin=0, all the other parameters are ignored                  *
# When ptgmin>0, pta and draj are not going to be used                 *
#***********************************************************************
   0 = ptgmin ! Min photon transverse momentum
 0.4 = R0gamma ! Radius of isolation code
 1.0 = xn ! n parameter of eq.(3.4) in hep-ph/9801442
 1.0 = epsgamma ! epsilon_gamma parameter of eq.(3.4) in hep-ph/9801442
 .true. = isoEM ! isolate photons from EM energy (photons and leptons)
#*********************************************************************
# WBF cuts                                                           *
#*********************************************************************
 0   = xetamin ! minimum rapidity for two jets in the WBF case  
 0   = deltaeta ! minimum rapidity for two jets in the WBF case 
#*********************************************************************
# KT DURHAM CUT                                                      *
#*********************************************************************
 -1    =  ktdurham        
 0.4  =  dparameter 
#*********************************************************************
# maximal pdg code for quark to be considered as a light jet         *
# (otherwise b cuts are applied)                                     *
#*********************************************************************
 4 = maxjetflavor    ! Maximum jet pdg code
#*********************************************************************
# Jet measure cuts                                                   *
#*********************************************************************
 0   = xqcut   ! minimum kt jet measure between partons
#*********************************************************************
#
#*********************************************************************
# Store info for systematics studies                                 *
# WARNING: If use_syst is T, matched Pythia output is                *
#          meaningful ONLY if plotted taking matchscale              *
#          reweighting into account!                                 *
#*********************************************************************"""

    
    f=open("ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"/ZpTpt_Zp"+str(Gstar_mass)+Gstar_width+"_Tp"+str(Tp_mass)+Tp_width+chirality+"_"+Tp_decay+"_run_card.dat","w")
    f.write(script)
    f.close()
    

#Gstar_mass_list=[1500,1500,1500, 1750,1750, 2000,2000,2000, 2250,2250, 2500,2500,2500, 3000,3000,3000, 3500,3500,3500, 4000,4000,4000]
#Tp_mass_list   =[ 800,1000,1200, 1000,1300, 1000,1300,1500, 1300,1500, 1300,1500,1800, 1500,2000,2500, 1800,2100,2500, 2100,2500,3000]
Gstar_mass_list=[1500]
Tp_mass_list   =[ 800]

Gstar_width_list=["Nar","WID"]
Tp_width_list=["Nar"]
chirality_list=["LH"]
Tp_decay_list=["Ht","Zt","Wb"]
    
    
for Gstar_mass,Tp_mass in zip(Gstar_mass_list,Tp_mass_list):
    for Gstar_width in Gstar_width_list:
        for Tp_width in Tp_width_list:
            for chirality in chirality_list:
                for Tp_decay in Tp_decay_list:
                    generate_sample_directories(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay)
                    generate_customizecards(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay)
                    generate_extramodels(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay)
                    generate_madspin_card(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay)
                    generate_proc_card(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay)
                    generate_run_card(Gstar_mass, Gstar_width, Tp_mass, Tp_width, chirality, Tp_decay)
                    
                    