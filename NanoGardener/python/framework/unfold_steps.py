import json
import Steps_cfg as steps

output = { k:v for k, v in steps.Steps.items() if "VBSjjlnu" in k}

json.dumps(output, open("Steps_cfg_unfold.py", "w"), indent=4)