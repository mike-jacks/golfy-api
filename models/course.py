from uuid import UUID

from pydantic import BaseModel

class Course(BaseModel):
    id: UUID
    name: str
    location: str
    holes: int

class CourseRequest(BaseModel):
    name: str
    location: str
    holes: int

class CourseResponse(BaseModel):
    id: UUID