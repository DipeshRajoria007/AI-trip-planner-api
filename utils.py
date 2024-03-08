from openai import OpenAI
from constants import OPENAI_MODEL, TEMPERATURE, ERROR_LOG, ERROR_LOG_FOR_INPUT
from prompts import PROMPT_FOR_MANDATE, PROMPT_FOR_ALL, JSON_FORMAT
from fastapi import HTTPException
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEXT_MODEL_ENGINE = 'gpt-4-1106-preview'


def create_open_ai_query(input_query, system_message=None, model_engine=TEXT_MODEL_ENGINE):
    openai_url = f"{OPENAI_API_BASE_URL}/chat/completions"
    headers = {'Authorization': f'Bearer {OPENAI_API_KEY}', 'Content-Type': 'application/json'}
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": input_query})
    payload = {
        'model': model_engine,
        'messages': messages,
        'response_format': {"type": "json_object"}
    }
    response = requests.post(openai_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200 and 'choices' in response.json():
        content_text = response.json()['choices'][0]['message']['content'].strip()
        return {"success": True, "data": content_text, "response_json": response.json()}
    return {"success": False, "error": response.text}


def get_response_openai(
    where_to,
    number_of_days,
    itinerary_type,
    when_your_trip_start="",
    travel_preference="",
    budget=""
):
    if where_to and number_of_days and itinerary_type:
        final_prompt_mandate = (
            "Strictly adhere to the mentioned JSON format" +
            f"FORMAT:```{JSON_FORMAT}```" + f"PLACE:```{where_to}``` , NUMBER_OF_DAYS:```{number_of_days}```,"
                                            f" TRIP_TYPE: ```{itinerary_type}```"
            + PROMPT_FOR_MANDATE
        )
    elif (
        where_to
        and number_of_days
        and itinerary_type
        and (when_your_trip_start or travel_preference or budget)
    ):
        final_prompt_mandate = (
             "Strictly adhere to the mentioned JSON format" +
             f"FORMAT:```{JSON_FORMAT}```" + f"""PLACE:```{where_to}``` , NUMBER_OF_DAYS:```{number_of_days}```, 
             TRIP_TYPE: ```{itinerary_type}```, TRIP_START: ```{when_your_trip_start}```, TRAVEL_PREFERENCE:```{travel_preference}```, 
             BUDGET:```{budget}""" + PROMPT_FOR_ALL
        )
    else:
        raise HTTPException(401, ERROR_LOG_FOR_INPUT)
    
    response = create_open_ai_query(final_prompt_mandate)
    print(response["data"])
    if response["success"]:
        return {"success": True, "data": response["data"]}
    else:
        print("Error in creating campaigns from openAI:", str(e))
        return {"success": False, "error": HTTPException(503, ERROR_LOG)}
