from setuptools import setup

with open("README.md","r")as fh:
    long_description = fh.read()

setup(
    name="emailid_finder",
    version="0.0.1",
    description="This will find the email-id is 'True' or 'Flase'",
    long_description=long_description,
    url="https://github.com/teamtact/fake-email-identifier",
    long_description_content_type="text/markdown",
    py_modules=["emailid_finder"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
