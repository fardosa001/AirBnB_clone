#!/usr/bin/python3
"""review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
