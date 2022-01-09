import setuptools

setuptools.setup(
    name="TestProject",
    packages=setuptools.find_packages(exclude=["TestProject_tests"]),
    install_requires=[
        "dagster==0.13.12",
        "dagit==0.13.12",
        "pytest",
    ],
)
