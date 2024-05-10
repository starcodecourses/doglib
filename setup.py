from setuptools import setup, find_packages

setup(
    name="doglib",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "gc",
        "numpy",
        "sphinx",
    ],
    author="Starcode",
    description="Doglib ist eine Python-Bibliothek, die speziell entwickelt wurde, um Schülerinnen die grundlegenden Arbeitsprinzipien von Python-Bibliotheken auf einfache und unterhaltsame Weise zu erklären.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=""
)