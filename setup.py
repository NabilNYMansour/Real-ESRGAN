import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="realesrgan_upscale",
    py_modules=["realesrgan_upscale"],
    version="1.0",
    description="",
    author="Sberbank AI, Xintao Wang, Nabil Mansour",
    url='https://github.com/ai-forever/Real-ESRGAN',
    packages=find_packages(include=['realesrgan_upscale']),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)