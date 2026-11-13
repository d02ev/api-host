from api_host.core.database import get_supabase_client
from api_host.modules.resume.repositories.resume_repository import ResumeRepository

def test_fetch_existing_resume():
    client = get_supabase_client()
    repository = ResumeRepository(client)
    resume_id = 1
    
    result = repository.get_by_id(resume_id)
        
    assert result is not None
    assert "name" in result
    assert "professional_summary" in result
    assert "contact" in result
    assert "education" in result
    assert "experience" in result
    assert "project" in result
    assert "techstack" in result
    
def test_fetch_nonexistent_resume():
    client = get_supabase_client()
    repository = ResumeRepository(client)
    
    result = repository.get_by_id(-1)
    
    assert result is None