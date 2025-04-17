from kappa import kappa
import numpy
import xspec
import pyatomdb


# These are globals to hold the model data
kappamodelobject = kappa.KappaSession(
                   elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                             13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                             23, 24, 25, 26, 28])
kappavmodelobject = False
kappavvmodelobject = False

kappamodelobject.abund_xspectoatomdb = {}
kappamodelobject.abund_xspectoatomdb['angr'] = 'AG89'
kappamodelobject.abund_xspectoatomdb['aspl'] = 'Asplund09'
kappamodelobject.abund_xspectoatomdb['feld'] = 'Feldman'
kappamodelobject.abund_xspectoatomdb['aneb'] = 'AE82'
kappamodelobject.abund_xspectoatomdb['grsa'] = 'GS98'
kappamodelobject.abund_xspectoatomdb['wilm'] = 'Wilm00'
kappamodelobject.abund_xspectoatomdb['lodd'] = 'Lodd03'

kappamodelobject.thermal_broadening = True



pykappaInfo = ("kT            \"keV\"   1.0 0.00862 0.00862 86. 86. 0.01",
             "kappa         \"\"      3.0 2.0 2.0 100. 1000. 0.01",
             "abund         \"\"      1.0 0.0 0.0 10.0 10.0 0.01",
             "Velocity         \"km/s\"      100 0.0 0.0 3000.0 3000.0 1.0")

pyvkappaInfo = ("kT            \"keV\"   1.0 0.00862 0.00862 86. 86. 0.01",
              "kappa         \"\"      3.0 2.0 2.0 100. 1000. 0.01",
              "H             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "He            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "C             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "N             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "O             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "F             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Ne            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Mg            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Al            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Si            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "S             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Ar            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Ca            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Fe            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Ni            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
              "Velocity         \"km/s\"      100 0.0 0.0 3000.0 3000.0 1.0")


pyvvkappaInfo = ("kT            \"keV\"   1.0 0.00862 0.00862 86. 86. 0.01",
               "kappa         \"\"      3.0 2.0 2.0 100. 1000. 0.01",
               "H             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "He            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Li            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Be            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "B             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "C             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "N             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "O             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "F             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Ne            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Na            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Mg            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Al            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Si            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "P             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "S             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Cl            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Ar            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "K             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Ca            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Sc            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Ti            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "V             \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Cr            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Mn            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Fe            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Ni            \"\"      1.0 0.0 0.0 10.0 10.0 -0.01",
               "Velocity         \"km/s\"      100 0.0 0.0 3000.0 3000.0 1.0")


def pykappa(engs, params, flux):
  """
  Kaapa model for data

  PARAMETERS
  ----------
  engs : list[float]
    The energy bin edges (from xspec)
  params : list[float]
    The parameter list. See kappaInfo for definition
  flux : list[float]
    The array to fill with return values

  RETURNS
  -------
  None
    Fills out the flux array with photon cm3 s-1 bin-1 x 1e14

  USAGE
  -----
    # load the model into XSPEC
    xspec.AllModels.addPyMod(kappa, kappaInfo, 'add')
    # make a model
    m = xspec.Model('kappa')
  """

  # This is the call that will return everything. So set everything!
  ebins = numpy.array(engs)
  kappamodelobject.set_response(ebins, raw=True)
  # kappa model has the 14 main elements
  elarray = kappamodelobject.elements
  abund = numpy.zeros(len(elarray))



  if len(params)==5:
    # kappa case
    elarray=[2,6,7,8,10,12,13,14,16,18,20,26,28]
    abund = float(params[2])
  elif len(params)==19:
    # vkappa case
    elarray=[1,2,6,7,8,9,10,12,13,14,16,18,20,26,28]
    abund = numpy.array(params[2:17])
  elif len(params)==31:
    # vvkappa case
    elarray=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,\
             20,21,22,23,24,25,26,28]
    abund = numpy.array(params[2:29])
    

  T = float(params[0])
  k = float(params[1])
  Velocity = float(params[-2])
  # params[-1] is the norm

  kappamodelobject.velocity_broadening = Velocity

  # correct abundance set if required
  abund_str = xspec.Xset.abund.split(":")[0]
       
  if kappamodelobject.abund_xspectoatomdb[abund_str] != \
     kappamodelobject.abundset:
    kappamodelobject.set_abundset(kappamodelobject.abund_xspectoatomdb[abund_str])

  # set the abundance

  kappamodelobject.set_abund(elarray, abund)

  spec = kappamodelobject.return_spectrum(T, k)

  flux[:] = spec*1e14


def pyvkappa(engs, params, flux):
  pykappa(engs,params,flux)

def pyvvkappa(engs, params, flux):
  pykappa(engs,params,flux)


xspec.AllModels.addPyMod(pykappa, pykappaInfo, 'add')
xspec.AllModels.addPyMod(pyvkappa, pyvkappaInfo, 'add')
xspec.AllModels.addPyMod(pyvvkappa, pyvvkappaInfo, 'add')
print("")
print("Models kappa, vkappa, and vvkappa ready for use")
