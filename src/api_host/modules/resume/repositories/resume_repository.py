from supabase import Client

class ResumeRepository:
    def __init__(self, client: Client):
        self.client = client
        
    def get_by_id(self, resume_id: int) -> dict | None:
        response = (
            self.client.from_("resume")
                .select("""
                        name,
                        professional_summary,
                        contact(email, mobile, github, linkedin, website),
                        education(institute, start_date, end_date, degree, grade, coursework),
                        experience(job_title, company_name, location, start_date, end_date, description, is_deleted),
                        project(display_name, year, short_desc, long_desc, tech_stack, repo_url, live_url, sorter, is_deleted),
                        techstack(languages, frameworks_and_platforms, databases, cloud_and_devops, others)     
                """)
                .eq("id", resume_id)
                .eq("experience.is_deleted", False)
                .eq("project.is_deleted", False)
                .execute()
        )
        
        if not response.data:
            return None
        
        return response.data[0]