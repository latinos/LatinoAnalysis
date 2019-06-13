import os
import commands



####### Setting #########
##---Which list to check---##
inputfile='Summer16_102X_nAODv4.py'
#inputfile='fall17_102X_nAODv4.py'
#inputfile='Autumn18_102X_nAODv4_v16.py'


##---campaign string in DAS datasetname
campaign='RunIISummer16NanoAODv4'
#campaign='RunIIFall17NanoAODv4'
#campaign='RunIIAutumn18NanoAODv4'
#######End of Setting###########

print "@@"+inputfile+"@@"

f=open(inputfile,'r')
lines=f.readlines()


##updated sample list(dic) 
Samples={}

##line in nAODv4 list python commented out. 
commented_lines=[]
##For ambigious case.
#by_hand_list=[]

##--Collect commented lines--##
for line in lines:
    line_nospace=line.replace(" ","")
    #print line_nospace
    ###check unfinished samples###
    if "#Samples" in line_nospace:
        
        #print "+++commented"
        commented_lines.append(line)
        #line=line.replace('#','')
        ##---find 'samples' definition part of this line ---##

        for part in line_nospace.split("#"): 
            if part.startswith('Samples'):
                exec(part) ##define Samples dic 
            else : continue

f.close()
#print "@@key list@@"
#for key in Samples:
#    print key

fnew=open(inputfile+"_new.py",'w') ## new file for updated list -> check commented samples and fill datasetname if production is completed.
for line in lines:
    line_nospace=line.replace(" ","")
    ##Already has datasetname##
    if not "#Samples" in line_nospace:
        fnew.write(line)
        continue
    ###Private samples -> NOT in DAS###
    if 'private' in line.lower():
        fnew.write(line)
        continue
    if 'srmPrefix' in line:
        fnew.write(line)
        continue


    ##scan all unfinished sample and check whetehr this line corresponds to the sample 
    fnew.write(line)

    for key in Samples:
        if len(key.replace(' ',''))==0:
            continue
        if (not "#Samples['"+key+"']" in line_nospace) and (not '#Samples["'+key+'"]' in line_nospace) : continue
        full_datasetname=Samples[key]
        #print full_datasetname['nanoAOD']
        
        keyword_list=[]
        ###---Search samples with keyword -> old datasetname/Sample alias/
        if len(full_datasetname['nanoAOD'].split('/'))>1:
            keyword_list.append(full_datasetname['nanoAOD'].split('/')[1])
        keyword_list.append(key)
        if 'HZJ_H' in key and 'tautau' in key: keyword_list.append( key.replace('HZJ_H','ZH')  )
        elif 'HWminusJ_H' in key and 'tautau' in key: keyword_list.append( key.replace('HWminusJ_H','WminusH')  )
        elif 'HWplusJ_H' in key and 'tautau' in key: keyword_list.append( key.replace('HWplusJ_H','WplusH')  )
    
        ##To scan all jhugen version## --> remove jhugen version and search
        keyword_list_noV=[]
        for keyword in keyword_list:
            
            name_temp=[]
            for part in keyword.split('_'): ## <process>_<jhugen>_<mass> :
                if 'jhugen' in part.lower():
                    continue
                if 'M' in part: ##Mass -> search with *M400_*. if using M400, M4000 can be included
                    part=part+"_"
                name_temp.append(part)
            keyword='*'.join(name_temp)
            keyword_list_noV.append(keyword)##for example ) GluGluHTo2L2Nu*M400
            #print "keyword="+keyword
        keyword_list=keyword_list+keyword_list_noV
        output_list=[]
        for keyword in keyword_list:
            ##check das output
            search_phr=keyword+"*/*"+campaign+"*/NANOAODSIM"
            #For example : 
            #dasgoclient -query="dataset=/GGJets*/*Fall17*/MINI*"
            #print "####Checking-->>>"+keyword
            done=0
            output=''
            status=''
            dascheck='dasgoclient -timeout 5 -query="dataset=/'+search_phr+'"'
            #print dascheck
            #--get das output list
            while done==0:
                try:
                    status, output = commands.getstatusoutput(dascheck)
                    done=1
                except:
                    done=0
            if not '/' in output: ## if no output -> searching with next keyword
                continue
            if '*' in output : continue
            #print "ouput=>>>>>>"+output
            output_list=output_list+output.split('\n')
        output_list=list(set(output_list)) ##removing duplicates
        nsample=len(output_list)
        #print "nsample="+str(nsample)
        if nsample==0: continue
                        
        fnew.write("#--->Updated!#")
        fnew.write("##------choose one of the following samples-------##Noutput="+str(nsample)+"\n")
        print key+" updated :)"
        if nsample==1: ## only one corresponding sample




            msg_vjhugen_change=''
            msg_ext=''
            if 'jhugen' in key.lower():
                print "--> !!jhugen version is in latino sample alias...checking..."

        
                ##Check vJHUHen in DAS dataset name##
                vjhugen_das=''
                
                for part in output_list[0].split('_'):
                    if 'jhugen' in part.lower() : 
                        #print '->datasetname in DAS='+part 
                        vjhugen_das=part.lower().replace('jhugen','').replace('v','')
                ##Check vJHUHen in latino sample alias##
                vjhugen_alias=''
                for part in key.split('_'):
                    if 'jhugen' in part.lower() :
                    #print '->datasetname in latino alias='+part
                        vjhugen_alias=part.lower().replace('jhugen','').replace('v','')
                ##if the two versions are not matched##        
                if vjhugen_das!=vjhugen_alias :
                    print "!!!!!!!!!Version is not matched. Alias should be fixed!!!.."+vjhugen_alias+"->"+vjhugen_das
                    new_key=[]
                    for part in key.split('_'):
                        if 'jhugen' in part.lower() :
                            part=part.replace(vjhugen_alias,vjhugen_das)
                        new_key.append(part)
                    key='_'.join(new_key)
                    msg_vjhugen_change='vjhugen is changed :'+vjhugen_alias+"->"+vjhugen_das
                ##if the two version are matched
                else :
                    print '->OK'
            ##if extension sample
            if 'ext' in key:
                if not 'ext' in output_list[0] : continue ##das name has no ext tag -> pass
                msg_ext=' !!ext sample!! check extension tag exists!!'
            
            towrite="Samples['"+key+"'] = {'nanoAOD' :'"+output_list[0]+"'} ##!!"+msg_vjhugen_change+msg_ext+"!!\n"

            fnew.write(towrite)



        elif nsample>1:
            #print "!!!You should choose one of the sample and add it to new sample list python by hand"
            #print "##"+key
            #by_hand_list.append("##-----------"+key+" is updated##")
            #print output
            #fnew.write(line)
            #fnew.write("##UPDATED!!!BUT..------choose one of the following samples-------##")
            for output_i in output_list:
                towrite="Samples['"+key+"'] = {'nanoAOD' :'"+output_i+"'}\n"
                #by_hand_list.append(towrite)
                #print towrite
                fnew.write(towrite)
        fnew.write("##---------------------------------------------------------------##\n")

            #fnew.write(line)
        
                        



fnew.close()


#print "@@@@@@@@Choose one of the samples for each process@@@@@@@@@@"
#for byhand in by_hand_list:
#    print byhand+"\n"

print "!!!!!Please check ---->"+inputfile+"_new.py!!!!!"

        
