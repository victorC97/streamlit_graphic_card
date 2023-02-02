import setuptools

setuptools.setup(
    name="streamlit-graphic-card",
    version="0.0.1",
    author="victorC97",
    author_email="victor.cour@telecomnancy.net",
    description="Graphic card component",
    long_description="Given a dataframe and two column of it, display a graphic card with a graph dataviz and statistics over it.",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
    setup_requires=['wheel']
)
