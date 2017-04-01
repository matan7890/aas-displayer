from setuptools import setup, find_packages

setup(
    name="aas_displayer",
    version="0.0.1",
    author="Matan Merom",
    description=("A demonstration of how to load an AAS file and print the dialogue texts to the screen on the right "
                 "time."),
    requires=['win-unicode-console'],
    packages=find_packages(),
)
