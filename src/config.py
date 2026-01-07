from dotenv import load_dotenv
import os

load_dotenv()

GENIUS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")
def get_genius_token() -> str:
    """Retrieve the Genius API token from environment variables.
    
    Returns:
        str: The Genius API token.
    """
    return GENIUS_TOKEN