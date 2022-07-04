import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notion-database-bot",
    version="0.0.2",
    author="Oliver Liu",
    author_email="zhliu0106@gmail.com",
    description="A package for synchronizing data in Notion Database through Notion official api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhliu0106/Notion-Database-Bot",
    # packages=setuptools.find_packages(),
    packages=["notion-database-bot"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)