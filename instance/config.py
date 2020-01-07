# !/usr/bin/env python

import os


defapp = "development"


class Config(object):
    """Top-Level configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
    SQLALCHEMY_DATABASE_URI = "sqlite:///gridscale.db"


class DevelopmentConfig(Config):
    """Development Configurations"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Configurations - Separate DB."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///gridscale.db"
    DEBUG = True


class StagingConfig(Config):
    """Staging Configurations"""
    DEBUG = True


class ProductionConfig(Config):
    """Production Configurations"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgres://gridscale:gridscale@localhost/gridscale"


app_config = {}
app_config['development'] = DevelopmentConfig
app_config['testing'] = TestingConfig
app_config['staging'] = StagingConfig
app_config['production'] = ProductionConfig
