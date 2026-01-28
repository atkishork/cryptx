from setuptools import setup, find_packages

setup(
    name="cryptx",
    version="1.0.0",
    author="Kishor Kumar",
    description="CTF-focused encoder/decoder CLI tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/atkishork/cryptx",
    packages=find_packages(),
    py_modules=["cryptx"],
    entry_points={
        "console_scripts": [
            "cryptx=cryptx:main",
        ]
    },
    install_requires=[
        "base58",
        "base45",
        "pybase62"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
)
