# samples

#samples = {}
    
#                    
samples['ggH']  = {   'name': ['fileggh.root', 'file2ggh.root'],     #   file name    
                      'weight' : 'baseW',                            #   weight/cut 
                      'weights': ['1', '1'],                         #   additional cuts file dependent
                      'friend': ['filegghfriend.root', 'file2gghfriend.root'],     #   friend file names: e.g. additional variables!    
                  }


samples['ttbar'] = {  'name': ['filett.root'],    
                      'weight' : 'baseW', 
                      'weights': ['1'] 
                  }
