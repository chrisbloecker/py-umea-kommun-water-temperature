import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-umea-kommun-water-temperature",
    version="0.1.0",
    author="Christopher Blöcker",
    author_email="mail@chrisbloecker.se",
    description="A library to retrieve water temperature information from Umeå kommun",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisbloecker/py-umea-kommun-water-temperature",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests"]
)
