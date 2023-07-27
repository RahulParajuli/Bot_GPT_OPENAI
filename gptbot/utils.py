
import json
import uuid

def is_unique_id(prompt_id):
    prompt_configs = prompt_configurations()
    for prompt_config in prompt_configs:
        if prompt_config["prompt_id"] == prompt_id:
            return False
    return True

def generate_unique_id():
    prompt_id =  str(uuid.uuid4())
    is_unique = is_unique_id(prompt_id)
    if not is_unique:
        prompt_id = generate_unique_id()
    return prompt_id

def prompt_configurations(config_path="configurations/prompts.json"):
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        return []
    
def update_prompt_configurations(config_path="configurations/prompts.json", new_config=[]):
    try:
        with open(config_path, "w") as f:
            json.dump(new_config, f)
            return True
    except Exception as e:
        return False
