import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ibom-openscopeproject",
    version="0.0.1",
    author="openscopeproject",
    author_email="author@example.com",
    description="Interactive HTML Bom tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openscopeproject/InteractiveHtmlBom",
    py_modules=["InteractiveHtmlBom.generate_interactive_bom"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)