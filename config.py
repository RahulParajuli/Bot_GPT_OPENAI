import os
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# Get the values
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")