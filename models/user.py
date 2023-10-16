#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """inherits from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
