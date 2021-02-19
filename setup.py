import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rgb-control",
    version="0.0.1",
    author="Alexandr Kuzhel",
    author_email="alexkuzhel.biz@gmail.com",
    description="The script allows you to set the RGB backlight color on A4Tech Bloody keyboards.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["rgb-control=rgb_control.main:main"],
    },
    url="https://github.com/apo5tol/bloody_keyboard_rgb_control",
    packages=setuptools.find_packages(),
    install_requires=[
        "pyusb==1.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)