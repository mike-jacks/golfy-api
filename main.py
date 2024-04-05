from uuid import uuid4 as new_uuid
from uuid import UUID

from fastapi import FastAPI, HTTPException, status

from models.player import Player, PlayerRequest, PlayerResponse
from models.course import Course, CourseRequest, CourseResponse


app = FastAPI()

players: dict[UUID, Player] = {}
courses: dict[UUID, Course] = {}

@app.get("/players")
async def get_players() -> list[Player]:
    return list(players.values())

@app.post("/players")
async def create_player(player_detail: PlayerRequest) -> PlayerResponse:
    player_id = new_uuid()
    player = Player(id=player_id, **player_detail.model_dump())
    players[player_id] = player
    return PlayerResponse(id = player_id)

@app.put("/players/{player_id}")
async def update_player(player_id: UUID, player_detail: PlayerRequest) -> PlayerResponse:
    if player_id not in players.keys():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{player_id} not found.")
    players[player_id] = Player(id=player_id, **player_detail.model_dump())
    return PlayerResponse(id=player_id)
    
@app.delete("/players/{player_id}")
async def delete_player(player_id: UUID) -> PlayerResponse:
    if player_id not in players.keys():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{player_id} not found.")
    players.pop(player_id)
    return PlayerResponse(id=player_id)

@app.get("/courses")
async def get_courses() -> list[Course]:
    return list(courses.values())

@app.post("/courses")
async def create_course(course_detail: CourseRequest) -> CourseResponse:
    course_id = new_uuid()
    course = Course(id=course_id, **course_detail.model_dump())
    courses[course_id] = course
    return CourseResponse(id=course_id)

@app.put("/courses/{course_id}")
async def update_course(course_id: UUID, course_detail: CourseRequest) -> CourseResponse:
    if course_id not in courses.keys():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail=f"{course_id} not found.")
    courses[course_id] = Course(id=course_id, **course_detail.model_dump())
    return CourseResponse(id=course_id)

@app.delete("/courses/{course_id}")
async def delete_course(course_id: UUID) -> CourseResponse:
    if course_id not in courses.keys():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{course_id} not found.")
    courses.pop(course_id)
    return CourseResponse(id=course_id)