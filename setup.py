import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read()

setuptools.setup(
    name="ophpy",
    version="0.0.2",
    author="YoungRok Kim",
    author_email="faller825@khu.ac.kr",
    description="Open source project about Computer Generated Hologram",
    long_description=long_description,
    url="https://github.com/robin9804/openholo_py",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'matplotlib', 'pillow','plyfile', 'numba'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7', 
)
