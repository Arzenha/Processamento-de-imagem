from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processamento_de_imagem",
    version="0.0.1",
    author="Ronald Brasil",
    description="Processamento de imagem usando scikit-image",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/Arzenha/Processamento-de-imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    )