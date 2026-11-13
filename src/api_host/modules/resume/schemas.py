from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, field_serializer

class ContactResponse(BaseModel):
    email: str
    mobile: str
    github: str
    linkedin: str
    website: str
    
class EducationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    institute: str
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    degree: str
    grade: str
    coursework: list[str]
    
class ExperienceResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    job_title: str = Field(alias="jobTitle")
    company_name: str = Field(alias="companyName")
    location: str
    start_date: datetime = Field(alias="startDate")
    end_date: datetime | None = Field(alias="endDate")
    description: list[str]
    
    @field_serializer("start_date", "end_date")
    def format_dates(self, value: datetime | None) -> str | None:
        if value is None:
            return None
        
        return value.strftime("%b %Y")
    
class ProjectResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    display_name: str = Field(alias="displayName")
    year: int
    short_desc: str = Field(alias="shortDescription")
    long_desc: str | None = Field(alias="longDescription")
    tech_stack: list[str] = Field(alias="techStack")
    repo_url: str = Field(alias="repoUrl")
    live_url: str | None = Field(alias="liveUrl")
    
    
class TechStackResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    languages: list[str]
    frameworks_and_platform: list[str] = Field(alias="frameworksAndPlatforms")
    databases: list[str]
    cloud_and_devops: list[str] = Field(alias="cloudAndDevOps")
    others: list[str]
    
class ResumeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    name: str
    professional_summary: str = Field(alias="professionalSummary")
    contact: ContactResponse
    education: EducationResponse
    experience: list[ExperienceResponse]
    project: list[ProjectResponse]
    techstack: TechStackResponse = Field(validation_alias="techstack", serialization_alias="techStack")