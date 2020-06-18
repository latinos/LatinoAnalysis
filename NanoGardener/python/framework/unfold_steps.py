import json
import sys
import Steps_cfg as steps

if len(sys.argv)>1:
    output = { k:v for k, v in steps.Steps.items() if sys.argv[1] in k}
else:
    output = steps.Steps

for k, item in output.items():
    if "onlySample" in item:  item.pop("onlySample")


json.dump(output, open("Steps_cfg_unfold.json", "w"), indent=4)