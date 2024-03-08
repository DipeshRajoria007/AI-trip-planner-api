JSON_FORMAT = """{
  "type": "object",
  "properties": {
    "itinerary": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "day": {
              "type": "string"
            },
            "activities": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "time": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "location": {
                      "type": "string"
                    },
                    "price": {
                      "type": "integer"
                    },
                    "duration": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "time",
                    "name",
                    "location",
                    "price",
                    "duration",
                    "description"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "time": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "location": {
                      "type": "string"
                    },
                    "price": {
                      "type": "integer"
                    },
                    "duration": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "time",
                    "name",
                    "location",
                    "price",
                    "duration",
                    "description"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "time": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "location": {
                      "type": "string"
                    },
                    "price": {
                      "type": "integer"
                    },
                    "duration": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "time",
                    "name",
                    "location",
                    "price",
                    "duration",
                    "description"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "time": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "location": {
                      "type": "string"
                    },
                    "price": {
                      "type": "integer"
                    },
                    "duration": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "time",
                    "name",
                    "location",
                    "price",
                    "duration",
                    "description"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "time": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "location": {
                      "type": "string"
                    },
                    "price": {
                      "type": "integer"
                    },
                    "duration": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "time",
                    "name",
                    "location",
                    "price",
                    "duration",
                    "description"
                  ]
                }
              ]
            }
          },
          "required": [
            "day",
            "activities"
          ]
        },
        {
          "type": "object",
          "properties": {
            "day": {
              "type": "string"
            },
            "activities": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "time": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "location": {
                      "type": "string"
                    },
                    "price": {
                      "type": "null"
                    },
                    "duration": {
                      "type": "null"
                    },
                    "description": {
                      "type": "null"
                    }
                  },
                  "required": [
                    "time",
                    "name",
                    "location",
                    "price",
                    "duration",
                    "description"
                  ]
                }
              ]
            }
          },
          "required": [
            "day",
            "activities"
          ]
        }
      ]
    }
  },
  "required": [
    "itinerary"
  ]
}"""

PROMPT_FOR_MANDATE = """You should always check if the place exist in the globe, if not then simply tell no place exist.
User is going to place:PLACE, for number of days:NUMBER_OF_DAYS, for a this type of trip: TRIP_TYPE. Your task is to
create a complete Trip Planner. Lets divide how you will give the trip planner step by step:
You should always check if the place exist in the globe, if not then simply tell no place exist
1.) First check if the place exists where the user is wanting to go, if not then tell the user that this does not present in globe !,
then check where the user is going , for how many days and which type of trip the user is planning.
2.) Take time to think and plan the trip on your own first.
3.) You should provide where the user will go on which day, on a single day time based trip planning, at what time user will visit at 
what site seeing area, also add a small comment about that area, where the user will have breakfast, shopping, dinner etc.
4.) Final Output is the json in the mentioned format:FORMAT. No extra text needed.
"""

PROMPT_FOR_ALL = """You should always check if the place exist in the globe, if not then simply tell no place exist.
User is going to place:PLACE, for number of days:NUMBER_OF_DAYS, for a this type of trip: TRIP_TYPE, user is 
starting the trip on TRIP_START, also the budget: BUDGET also the user have some preferences TRAVEL_PREFERENCE.
Your task is to
create a complete Trip Planner. Lets divide how you will give the trip planner step by step:
You should always check if the place exist in the globe, if not then simply tell no place exist
1.) First check if the place exists where the user is wanting to go, if not then tell the user that this does not present in globe !,
Then check where the user is going , for how many days and which type of trip the user is planning, about trip start and budget, also
the preferences of the user. Always be customised and personalised for the user.
2.) Take time to think and plan the trip on your own first.
3.) You should provide where the user will go on which day, on a single day time based trip planning, at what time user will visit at 
what site seeing area, also add a small comment about that area, where the user will have breakfast, shopping, dinner etc.
4.) Final Output is the json in the mentioned format:FORMAT. No extra text needed.
"""
