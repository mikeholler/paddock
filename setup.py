import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'paddock', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setuptools.setup(
    name="paddock",
    version="0.1.0",
    description="iRacing Web SDK based off of ir_webstats",
    url="https://github.com/mikeholler/paddock",
    author="Mike Holler",
    license="MIT",
    packages=setuptools.find_packages(
        exclude=[
            "tests", "*.tests", "*.tests.*",
            "integration_tests", "*.integration_tests", "*.integration_tests.*",
        ]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "decorator>=4.4.3,<5",
        "requests>=2.24,<3",
    ],
)
