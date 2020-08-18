import setuptools

setuptools.setup(
    name="paddock",
    version="0.1.0",
    description="iRacing Web SDK based off of ir_webstats",
    url="https://github.com/mikeholler/unofficial-iracing-web-sdk",
    author="Mike Holler",
    license="MIT",
    packages=setuptools.find_packages(),
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
