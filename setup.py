from setuptools import find_packages, setup


setup(
    name='btg',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pytest>=7.0.0",
        "python-dotenv>=0.19.0",
        "pymongo>=4.3.3",
        "pydantic-settings>=2.0.0"
    ],
    python_requires='>=3.8',
)
