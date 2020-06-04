import json
import sys
import Steps_cfg as steps

output = { k:v for k, v in steps.Steps.items() if sys.argv[1] in k}
#output = steps.Steps


json.dump(output, open("Steps_cfg_unfold.json", "w"), indent=4)