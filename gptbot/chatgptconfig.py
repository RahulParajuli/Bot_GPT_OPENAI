
from config import OPENAI_API_KEY
from gptbot.utils import generate_unique_id, prompt_configurations, update_prompt_configurations
import openai

class ChatGPTBotAPI:
    def __init__(self, api_key:str=OPENAI_API_KEY):
        openai.api_key
        self.config = prompt_configurations()
        
    def create_prompt(self, prompt):
        prompt_config = {}
        prompt_id = generate_unique_id()
        prompt_config["prompt_id"] = prompt_id
        prompt_config["prompt"] = prompt
        prompt_config["response"] = ""
        self.config.append(prompt_config)
        update_status = update_prompt_configurations(new_config=self.config)
        if update_status:
            response = {
                "error" : "false",
                "prompt_id" : prompt_id,
                "prompt" : prompt,
                "message" : "Prompt created successfully"
            }
        else : 
            response = {
                "error" : "true",
                "message" : "Prompt creation failed"
            }
        return response
      
    def generate_openai_response(self, prompt):
        if prompt == "":
            return "Empty Prompt"
        try:
            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.8,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            )
            generated_text = response.choices[0].text.strip()
            
            return generated_text  
        except Exception as e:
            return ""
        
    def get_response(self, prompt_index):
        response = {
            "error" : "true",
            "message" : "Prompt not found"
        }
        for id, prompt in enumerate(self.config):
            if prompt["prompt_id"] == prompt_index:
                if not prompt.get("response", ""):
                    result =  self.generate_openai_response(prompt.get("prompt", ""))
                else:
                    result = prompt.get("response", "")
                if not result:
                    return  {
                        "error" : "true",
                        "message" : "Gpt response fetch failed"
                    }
                self.config[id]["response"] = result
                update_status = update_prompt_configurations(new_config=self.config)
                if update_status:
                    response = {
                        "error" : "false",
                        "prompt_id" : prompt_index,
                        "prompt" : prompt.get("prompt", ""),
                        "response" : result,
                        "message" : "Prompt Respone Recieved"
                    }
                else : 
                    response = {
                        "error" : "true",
                        "message" : "Gpt response store failed"
                    }
        return response
    
    def update_prompt(self, prompt_index, new_prompt):
        response = {
            "error" : "true",
            "message" : "Prompt not found"
        }
        for idx, prompt_config in enumerate(self.config):
            if prompt_config["prompt_id"] == prompt_index:
                self.config[idx]["prompt"] = new_prompt
                self.config[idx]["response"] = ""
                # return (self.config[idx], self.config[idx]["prompt"])
                update_status = update_prompt_configurations(new_config=self.config)
                if update_status:
                    response = self.config[idx]
                else : 
                    response = {
                        "error" : "true",
                        "message" : "Error updating prompt"
                    }
        return response
        
    def delete_prompt(self, prompt_index):
        response = {
            "error" : "true",
            "message" : "Prompt not found"
        }
        for idx, prompt_config in enumerate(self.config):
            if prompt_config["prompt_id"] == prompt_index:
                del self.config[idx]
                update_status = update_prompt_configurations(new_config=self.config)
                if update_status:
                    response = {
                        "error" : "false",
                        "message" : "Prompt deleted successfully"
                    }
                else : 
                    response = {
                        "error" : "true",
                        "message" : "Error updating prompt"
                    }
                break
        return response