import setuptools

setuptools.setup(
    name="streamlit-lchart-card",
    version="0.0.2",
    author="victorC97",
    author_email="victor.cour@telecomnancy.net",
    description="Chart card component",
    long_description="Given a dataframe and two column of it, display a card with a line chart dataviz and statistics over it.",
    long_description_content_type="text/plain",
    url="https://github.com/victorC97/streamlit_graphic_card",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
    setup_requires=['wheel']
)
