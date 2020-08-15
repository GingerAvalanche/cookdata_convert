import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cookdata_convert",
    version="0.0.3",
    author="Ginger",
    author_email="chodness@gmail.com",
    description="CookData converter for LoZ:BotW",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GingerAvalanche/",
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["cookdata_convert = cookdata_convert.__main__:main",]},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.7.4",
    install_requires=["oead>=0.11.2",],
)