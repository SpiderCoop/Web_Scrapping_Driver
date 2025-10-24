from setuptools import setup, find_packages

setup(
    name="driver_configuration",  # Nombre del paquete (debe coincidir con la carpeta del módulo)
    version="0.1.0",  # Versión inicial del paquete
    author="David Jiménez Cooper",
    author_email="david.jimenez.cooper@gmail.com",
    description="Un paquete para configurar de manera rapida y sencilla el driver de selenium",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SpiderCoop/Web_Scrapping_Driver",  # URL de tu repositorio en GitHub
    packages=find_packages(),  # Detecta automáticamente los submódulos
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "selenium",
        "webdriver-manager",
    ],
    python_requires=">=3.6",  # Versión mínima de Python compatible
)
