### ChatGPTBOT Flask API Documentation

This is the documentation for the ChatGPT Flask API, which provides endpoints for creating, updating, fetching, and deleting prompts to interact with the ChatGPT language model.

## Installation
- Create a virtual environment and activate it.
`python -m venv venv`
`source venv/bin/activate`

- Install the dependencies.
`pip install -r requirements.txt`

- Run the app.
`python main.py`

## Endpoints

http://localhost:5000/

### 1. Create Prompt

##### POST /create

This endpoint allows you to create a new prompt and store it in prompt configuration. The prompt should be provided in the request body as JSON data under the key prompt. 

**Input :** 
<code>POST /create
Content-Type: application/json
{
  "prompt": "Your prompt goes here."
}
</code>

### 2. Fetch Response By Prompt ID

##### GET /fetch/<<string:prompt_id>>

This endpoint retrieves the response for a given prompt based on its ID from the Openai language model.

**Input :** 
<code>GET /fetch/your-prompt-id</code>

### 3. Update Response By Prompt ID

##### PUT /update

This endpoint allows you to update an existing prompt and get a new response from the language model. You need to provide the prompt ID and the updated prompt in the request body as JSON data.

**Input :** 
<code>PUT /update
Content-Type: application/json

{
  "prompt_id": "your-prompt-id",
  "new_prompt": "Your updated prompt goes here."
}
</code>

### 4. Delete Response By Prompt ID

##### DELETE /remove/<<string:prompt_id>>

This endpoint allows you to delete a prompt and its associated response from the ChatGPT language model.

**Input :** 
<code>DELETE /remove/your-prompt-id</code>


## postman collection
GPT API Task.postman_collection.json