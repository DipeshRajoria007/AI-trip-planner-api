from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from utils import get_response_openai, create_open_ai_query
from pydantic import BaseModel


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TripPlannerRequest(BaseModel):
    where_to: str
    number_of_days: str
    itinerary_type: str
    when_your_trip_start: str
    travel_preference: str
    budget: str


class WanderLustRequest(BaseModel):
    prompt: str


@app.post("/trip_planner_api")
def trip_planner(trip_planner: TripPlannerRequest):
    where_to = trip_planner.where_to
    number_of_days = trip_planner.number_of_days
    itinerary_type = trip_planner.itinerary_type
    when_your_trip_start = trip_planner.when_your_trip_start
    travel_preference = trip_planner.travel_preference
    budget = trip_planner.budget
    response = get_response_openai(where_to, number_of_days, itinerary_type, when_your_trip_start=when_your_trip_start,
                                   travel_preference=travel_preference, budget=budget)
    if response["success"]:
        return JSONResponse(
            content={
                "success": True,
                "response": response["data"]
            })
    else:
        return JSONResponse(
                content={
                    "success": False,
                    "error": response["error"]
                }
        )


@app.post("/wanderlust")
def trip_planner(wander_lust: WanderLustRequest):
    prompt = wander_lust.prompt
    if prompt:
        response = create_open_ai_query(prompt)
        if response["success"]:
            return JSONResponse(
                content={
                    "success": True,
                    "response": response["data"]
                })
        else:
            return JSONResponse(
                    content={
                        "success": False,
                        "error": response["error"]
                    }
            )
    else:
        return JSONResponse(
                content={
                    "success": False,
                    "error": "Please provide valid inputs"
                }
        )
