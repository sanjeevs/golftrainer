from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="golftrainer",
    version="0.0.1",
    description="Analyze a golf swing looking at critical points.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    url="https://github.com/sanjeevs/golftrainer",
    author="Sanjeev Singh",
    author_email="snjvsingh123@gmail.com",
    entry_points={
        'console_scripts' : [
            'golfmodel1=golftrainer.golfmodel1:main'
        ]
    },
    install_requires = ['opencv-python'],
    packages = ['golftrainer'],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    }
)