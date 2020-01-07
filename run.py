#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from core import (create_app)

config_name = "development"
app = create_app(config_name)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000
        )
