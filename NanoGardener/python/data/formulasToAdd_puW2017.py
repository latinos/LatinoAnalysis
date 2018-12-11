# formulas to be added, in python language
# call to branches have to be in the form event.branchName
# if you want to use logical operators, the have to be the python ones (i.e "and" not " and ")

formulas = {}

formulas['puW2017'] = '(  (event.run_period == 1.) * event.puW2017B \
                         +(event.run_period == 2.) * event.puW2017C \
                         +(event.run_period == 3.) * event.puW2017D \
                         +(event.run_period == 4.) * event.puW2017E \
                         +(event.run_period == 5.) * event.puW2017F )'

