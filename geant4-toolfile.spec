### RPM external geant4-toolfile 1.0
Requires: geant4
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/geant4.xml
<tool name="GEANT4" version="@TOOL_VERSION@">
  <info url="http://wwwinfo.cern.ch/asd/geant4/geant4.html"/>
  <lib name="G4digits_hits"/>
  <lib name="G4error_propagation"/>
  <lib name="G4event"/>
  <lib name="G4FR"/>
  <lib name="G4geometry"/>
  <lib name="G4global"/>
  <lib name="G4graphics_reps"/>
  <lib name="G4intercoms"/>
  <lib name="G4interfaces"/>
  <lib name="G4materials"/>
  <lib name="G4modeling"/>
  <lib name="G4parmodels"/>
  <lib name="G4particles"/>
  <lib name="G4persistency"/>
  <lib name="G4physicslists"/>
  <lib name="G4processes"/>
  <lib name="G4RayTracer"/>
  <lib name="G4readout"/>
  <lib name="G4run"/>
  <lib name="G4tracking"/>
  <lib name="G4track"/>
  <lib name="G4Tree"/>
  <lib name="G4visHepRep"/>
  <lib name="G4vis_management"/>
  <lib name="G4visXXX"/>
  <lib name="G4VRML"/>
  <client>
    <environment name="GEANT4_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$GEANT4_BASE/lib"/>
    <environment name="G4LIB" value="$LIBDIR"/>
    <environment name="INCLUDE" default="$GEANT4_BASE/include"/>
  </client>
  <flags cppdefines="G4USE_STD_NAMESPACE GNU_GCC G4V9"/>
  <runtime name="G4LEVELGAMMADATA" value="$GEANT4_BASE/data/PhotonEvaporation2.0" type="path"/>
  <runtime name="G4NEUTRONHPDATA" value="$GEANT4_BASE/data/G4NDL3.13" type="path"/>
  <runtime name="G4RADIOACTIVEDATA" value="$GEANT4_BASE/data/RadioactiveDecay3.2" type="path"/>
  <runtime name="G4LEDATA" value="$GEANT4_BASE/data/G4EMLOW6.2" type="path"/>
  <runtime name="G4NEUTRONXS" value="$GEANT4_BASE/data/G4NEUTRONXS1.0" type="path"/>
  <use name="clhep"/>
</tool>

EOF_TOOLFILE

cat << \EOF_TOOLFILE >%i/etc/scram.d/geant4core.xml
<tool name="geant4core" version="@TOOL_VERSION@">
  <info url="http://wwwinfo.cern.ch/asd/geant4/geant4.html"/>
  <lib name="G4digits_hits"/>
  <lib name="G4error_propagation"/>
  <lib name="G4event"/>
  <lib name="G4geometry"/>
  <lib name="G4global"/>
  <lib name="G4graphics_reps"/>
  <lib name="G4intercoms"/>
  <lib name="G4interfaces"/>
  <lib name="G4materials"/>
  <lib name="G4parmodels"/>
  <lib name="G4particles"/>
  <lib name="G4persistency"/>
  <lib name="G4physicslists"/>
  <lib name="G4processes"/>
  <lib name="G4readout"/>
  <lib name="G4run"/>
  <lib name="G4tracking"/>
  <lib name="G4track"/>
  <client>
    <environment name="GEANT4_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$GEANT4_BASE/lib"/>
    <environment name="G4LIB" value="$LIBDIR"/>
    <environment name="INCLUDE" default="$GEANT4_BASE/include"/>
  </client>
  <flags cppdefines="G4USE_STD_NAMESPACE GNU_GCC G4V9"/>
  <runtime name="G4LEVELGAMMADATA" value="$GEANT4_BASE/data/PhotonEvaporation2.0" type="path"/>
  <runtime name="G4NEUTRONHPDATA" value="$GEANT4_BASE/data/G4NDL3.13" type="path"/>
  <runtime name="G4RADIOACTIVEDATA" value="$GEANT4_BASE/data/RadioactiveDecay3.2" type="path"/>
  <runtime name="G4LEDATA" value="$GEANT4_BASE/data/G4EMLOW6.2" type="path"/>
  <runtime name="G4NEUTRONXS" value="$GEANT4_BASE/data/G4NEUTRONXS1.0" type="path"/>
  <use name="clhep"/>
</tool>
EOF_TOOLFILE

cat << \EOF_TOOLFILE >%i/etc/scram.d/geant4vis.xml
<tool name="geant4vis" version="@TOOL_VERSION@">
  <info url="http://wwwinfo.cern.ch/asd/geant4/geant4.html"/>
  <lib name="G4FR"/>
  <lib name="G4modeling"/>
  <lib name="G4RayTracer"/>
  <lib name="G4Tree"/>
  <lib name="G4visHepRep"/>
  <lib name="G4vis_management"/>
  <lib name="G4visXXX"/>
  <lib name="G4VRML"/>
  <use name="geant4core"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post
