import combPlots

## example of config
## ---------------------------------------------------------------------------------------------------
plotName = "COMBCR_ULTIMATE_preAppV02"
PlotDic = {}
PlotDic['Keys'] = ["muF","muV"]
PlotDic['AxisTitle'] = ["#mu_{F}","#mu_{V}"]
PlotDic['MinPlt'] = [0,0]
PlotDic['MaxPlt'] = [2.,2.]
PlotDic['Min'] = [0,0]
PlotDic['Max'] = [2,2]
PlotDic['LegTitle'] = ""
LimFiles = {'Exp' : "higgsCombineHWW_COMBCR_ULTIMATE_preAppV02_H0PH_LScanSM3_doNotGiveUp_900.root"}
## ---------------------------------------------------------------------------------------------------

cP = combPlots.combPlot("contours")
cP.MDF2D(plotName,PlotDic,LimFiles)
