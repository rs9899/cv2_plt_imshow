import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="cv2_plt_imshow", # Replace with your own username
    version="0.0.1",
    author="Rupesh",
    author_email="rupesh95903@gmail.com",
    description="Using matplotlib_imshow for images read by cv2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rs9899/cv2_plt_imshow",
    keywords="cv2 imshow pyplot cv2_imshow matplotlib",
    packages=setuptools.find_packages(),
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['matplotlib>=3.2.2','opencv-python>=4.2.0.34'],
    python_requires='>=3.6',
    project_urls={  
        'Bug Reports': 'https://github.com/rs9899/cv2_plt_imshow/issues',
        'Source': 'https://github.com/rs9899/cv2_plt_imshow',
    }
)