import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatsapp-web",
    version="0.0.1",
    author="fantaso",
    author_email="fantaso.code@gmail.com",
    description="A Python library to automate easily whatsapp web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fantaso/whatsapp-web",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment :: Mozilla",
        "Natural Language :: English",
        "Topic :: Communications :: Chat",
    ],
    python_requires='>=3.6',
)
