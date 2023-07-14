#!/usr/bin/python3

import os
import json
from models.engine.file_storage import FileStorage
""" importing file_storage.py"""

storage = FileStorage()
storage.reload()
