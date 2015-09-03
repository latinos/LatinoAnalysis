#
# isolation and id scale factors for leptons
#

# isoidScaleFactors = {}

isoidScaleFactors['ele'] = [
                          #   pt           eta         down   value  up
                          (( 0.0, 10.0   ), (0.0, 1.5), ( 0.980, 0.986, 0.999 ) ),
                          (( 0.0, 10.0   ), (1.5, 4.5), ( 0.980, 0.986, 0.999 ) ),
                          ((10.0, 20000.0), (0.0, 4.5), ( 0.985, 0.989, 0.999 ) ),
                         ]

isoidScaleFactors['mu'] = [
                          #   pt           eta           value   down    up
                          (( 0.0, 10.0   ), (0.0, 4.5), ( 0.980, 0.986, 0.999 ) ),
                          ((10.0, 20000.0), (0.0, 4.5), ( 0.985, 0.989, 0.999 ) ),
                         ]
