from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="salve_ipc",
    version="0.1.0",
    description="A module that makes IPC for your code editor easy providing autocompletion and replacement suggestions",
    author="Moosems",
    author_email="moosems.j@gmail.com",
    url="https://github.com/Moosems/salve",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[line for line in open("requirements.txt").readlines()],
    python_requires=">=3.9",
    license="MIT license",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Typing :: Typed",
    ],
    packages=["src"],
    package_data={"src": ["./*"]},
)