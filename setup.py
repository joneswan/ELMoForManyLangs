import setuptools

setuptools.setup(
    name="elmoformanylangs",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=[
        "torch",
        "h5py",
        "numpy",
        "overrides",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
