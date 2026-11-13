from supabase import create_client, Client
from api_host.core.config import get_settings
from functools import lru_cache

@lru_cache(maxsize=1)
def get_supabase_client() -> Client:
    settings = get_settings()
    supabase_client = create_client(settings.supabase_url, settings.supabase_service_role_key)
    
    return supabase_client