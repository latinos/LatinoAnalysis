import json
import Steps_cfg as steps

output = { k:v for k, v in steps.Steps.items() if "VBSjjlnuSkim2017v5" in k}
for k, v in output.items():
    print(v)
    v["onlySample"] = ""

json.dump(output, open("Steps_cfg_unfold.json", "w"), indent=4)