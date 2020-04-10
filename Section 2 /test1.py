# -*- coding: utf-8 -*-

import requests


response = requests.get("http://www.google.com")

data = response.text