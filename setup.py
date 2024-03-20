import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyballc", # Replace with your own username
    version="0.9.0",
    author="Wei Tian",
    author_email="jksr.tw@gmail.com",
    description='Python module for reading BAllC files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jksr/pyballc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
