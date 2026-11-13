from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.development"
    )
    
    supabase_url: str
    supabase_service_role_key: str
    supabase_anon_key: str
    github_pat: str
    github_owner: str
    github_repo: str
    github_workflow_file_path: str
    telegram_bot_token: str
    telegram_chat_id: str
    
    
@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()