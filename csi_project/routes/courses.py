from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

from ..coursetablehandler import *

coursesrouter = APIRouter(
    prefix='/courses'
)

class CourseFilter(BaseModel):
    course_id: Optional[str] = None
    name: Optional[str] = None
    teacher: Optional[str] = None
    description: Optional[str] = None

coursesrouter.get('/')
def getcourses(filter):
    results = find_courses(filter)

    if results:
        courses = []
        for row in results:
            courses.append({
                "courseID": row[0],
                "courseNAME": row[1],
                "toughtBY": row[2],
                "descrip": row[3]
            })
        return {"courses": courses}
    else:
        return {"message": "No courses found"}
