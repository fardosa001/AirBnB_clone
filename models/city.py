#!/usr/bin/python3
"""inherits from BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    state_id = ""
    name = ""
