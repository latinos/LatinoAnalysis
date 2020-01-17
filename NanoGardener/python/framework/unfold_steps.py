import json

steps = exec("Steps_cfg.py")

output = { k:v for k, v in steps.Steps.items() if "VBSjjlnu" in k}

json.dumps(output, open("Steps_cfg_unfold.py", "w"), indent=4)