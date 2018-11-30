import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emailid_finder_pkg",
    version="0.0.1",
    author="team",
    author_email="",
    description="This will find the email-id is 'fake' or 'not'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uthum/emailid_finder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)