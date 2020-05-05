import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zipmigo", # Replace with your own username
    version="1.0.1",
    author="Kathryn Aszklar",
    author_email="kea2143@columbia.edu",
    description="Simple package to download & unzip archives within notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaszklar/zipmigo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['tqdm>=4.38', 'requests>=2.22.0']
)
