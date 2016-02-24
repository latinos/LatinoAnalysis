
extern"C" {
  void pwhg_cphto_reweight_(double *mh, double *gh, double *mt, int *BWflag, double *m, double *w);
}

       
double getCPSweight(double mh,double gh,double mt,double m,int BWflag){
/*
c     INPUT
c     mh : Higgs boson mass (used in the POWHEG BOX generation)
c     gh : Higgs boson width (used in the POWHEG BOX generation)
c     mt : top quark mass
c     BWflag : 0    if the sample to reweight was produced with fixed Higgs width
c              1    if the sample to reweight was produced with running Higgs 
c                   width (this is the default in the POWHEG BOX)
c     m : virtuality of the produced Higgs boson resonance
c     OUTPUT
c     w : the reweighting factor 
*/
      double  w;

      pwhg_cphto_reweight_(&mh, &gh, &mt, &BWflag, &m, &w); 

      return w;
}
