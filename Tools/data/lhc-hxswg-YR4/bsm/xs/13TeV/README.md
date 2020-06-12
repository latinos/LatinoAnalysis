Comment about 4 and 5 TeV cross sections:

As these are not available in the Yellow Report 4 (https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV) for ggH @ NNLO+NNLL and for VBF @ NNLO, these were computed by myself. I document here how to obtain them:

### ggH

The ggH cross section was obtained using iHixs 2.0 (https://github.com/dulatf/ihixs). This is NOT the same tool that was used to compute the values listed in the YR4. However, in the YR4 values the top and bottom mass effects are only up to NLO, while the cross sections themselves are at NNLO+NNLL (QCD only) accuracy. The NNLO corrections are not valid for MH > 400 GeV. iHixs contains fixed order numbers for large Higgs masses.

Follow the documentation on the GitHub page to install iHixs. Additionaly it requires LHAPDF v6, Boost v1.6 and Cuba v4.2 to run. The first two are available on lxplus, while Cuba (http://www.feynarts.de/cuba/) can be installed separately with no problems.

An example command to run the program:

    ./ihixs -i default.card

# References:
iHixs 2:
    https://arxiv.org/abs/1802.00827

Cuba 4.2:
    http://www.feynarts.de/cuba/

### VBF

The VBF NNLO cross section was obtained using proVBFH-inclusive v2.0.2 (https://provbfh.hepforge.org/). It contains exactly the same ingredients as VBF@NNLO but is available publicly. When trying to use this yourself, follow the documention, which includes instructions on installing HOPPET, which is also needed to compile.

Additionaly, the code needs to be changed in the last lines of `src/matrix_element.f90`:

    !----------------------------------------------------------------------
      ! Defines which scale to use for scale_choice = 3,
      ! which can be any function of Q1, Q2 and ptH
      real(dp) function mixed_scale(Q1,Q2,ptH)
        real(dp), intent(in) :: Q1, Q2, ptH
    !    mixed_scale = ((mh*0.5d0)**4d0+(mh*ptH*0.5d0)**2d0)**(0.25d0)
        mixed_scale = mw
      end function mixed_scale

An example command to run the program:

    ./provbfh_incl -nnlo -sqrts 13000 -pdf PDF4LHC15_nnlo_30_pdfas -scale-choice 3 -mh 1000 -pdfuncert -7scaleuncert

The cross sections obtained like this for masses of 3 TeV pr lower deviate by less than 0.5% from the YR4 cross sections. Deviations can happen due to choosing a different generator seed, or by choosing a different number of calls/iterations for the grid initialisation / integration. 
Only the PDF+alphaS error has been computed! The values listed at 4 and 5 TeV for only PDF and only alphaS are just the same values as for 3 TeV!

# References:
This program is based on the following publications:

    Phys.Rev.Lett. 117 (2016) no.7, 072001 [arXiv:1606.00840]
    Phys.Rev.Lett. 115 (2015) no.8, 082002 [arXiv:1506.02660] 

The Higgs pair production implementation is based on:

    Phys.Rev. D99 (2019) no.7, 074028 [arXiv:1811.07918]
    Phys.Rev. D98 (2018) no.11, 114016 [arXiv:1811.07906] 
