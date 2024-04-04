import uuid
from uuid import UUID

from fastapi import FastAPI

from models.player import Player
from models.course import Course


app = FastAPI()

players = dict[UUID, Player] = {}
courses = dict[UUID, Course] = {}

@app.get("/players")
# @app.post("/players")
# @app.put("/players/{player_id}")
# @app.delete("/players/{player_id}")
# @app.get("/courses")
# @app.post("/courses")
# @app.put("/courses/{course_id}")
# @app.delete("/courses/{course_id}")