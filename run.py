#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from core import (create_app)
from flask_twisted import Twisted

config_name = "production"
# config_name = "development"
app = create_app(config_name)

twisted = Twisted(app)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000
        )
