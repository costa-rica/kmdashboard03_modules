from setuptools import setup

setup (
    name="km03-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "KM Dashboard modules includes models and config for KM applications",
    packages=['km03_config','km03_models'],
    python_requires=">=3.6",
    )