import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv() 

class GlobalConfig(BaseSettings): 
    title: str = os.environ.get("TITLE")
    version: str = "1.0.0"  
    description: str = os.environ.get("DESCRIPTION") 
    openapi_prefix: str = os.environ.get("OPENAPI_PREFIX")  
    docs_url: str = "/docs"  
    redoc_url: str = "/redoc"  
    openapi_url: str = "/openapi.json"
    api_prefix: str = "/api" 
  
  
settings = GlobalConfig()