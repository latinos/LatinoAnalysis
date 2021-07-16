#!/bin/bash


## 2016
basedir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7

for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESHFdo_suffix JESFlavorQCDdo_suffix JESRelativedo_suffix ; do 
  diff -qr ${basedir}__JESdo_suffix/ ${basedir}__${iSyst}/ | grep -v differ | grep JESdo | awk '{print $4}'> ${iSyst}2016.txt  ;
  cat ${iSyst}2016.txt | while read line; do ln -s ${basedir}__JESdo_suffix/${line} ${basedir}__${iSyst}/${line}; done
done

for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESHFup_suffix JESFlavorQCDup_suffix JESRelativeup_suffix ; do 
  diff -qr ${basedir}__JESup_suffix/ ${basedir}__${iSyst}/ | grep -v differ | grep JESup | awk '{print $4}'> ${iSyst}2016.txt  ;
  cat ${iSyst}2016.txt | while read line; do ln -s ${basedir}__JESup_suffix/${line} ${basedir}__${iSyst}/${line}; done
done


## 2017
basedir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7

for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESHFdo_suffix JESFlavorQCDdo_suffix JESRelativedo_suffix ; do 
  diff -qr ${basedir}__JESdo_suffix/ ${basedir}__${iSyst}/ | grep -v differ | grep JESdo | awk '{print $4}'> ${iSyst}2017.txt  ;
  cat ${iSyst}2017.txt | while read line; do ln -s ${basedir}__JESdo_suffix/${line} ${basedir}__${iSyst}/${line}; done
done

for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESHFup_suffix JESFlavorQCDup_suffix JESRelativeup_suffix ; do 
  diff -qr ${basedir}__JESup_suffix/ ${basedir}__${iSyst}/ | grep -v differ | grep JESup | awk '{print $4}'> ${iSyst}2017.txt  ;
  cat ${iSyst}2017.txt | while read line; do ln -s ${basedir}__JESup_suffix/${line} ${basedir}__${iSyst}/${line}; done
done


## 2018
basedir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7

for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESHFdo_suffix JESFlavorQCDdo_suffix JESRelativedo_suffix ; do 
  diff -qr ${basedir}__JESdo_suffix/ ${basedir}__${iSyst}/ | grep -v differ | grep JESdo | awk '{print $4}'> ${iSyst}2018.txt  ;
  cat ${iSyst}2018.txt | while read line; do ln -s ${basedir}__JESdo_suffix/${line} ${basedir}__${iSyst}/${line}; done
done

for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESHFup_suffix JESFlavorQCDup_suffix JESRelativeup_suffix ; do 
  diff -qr ${basedir}__JESup_suffix/ ${basedir}__${iSyst}/ | grep -v differ | grep JESup | awk '{print $4}'> ${iSyst}2018.txt  ;
  cat ${iSyst}2018.txt | while read line; do ln -s ${basedir}__JESup_suffix/${line} ${basedir}__${iSyst}/${line}; done
done


