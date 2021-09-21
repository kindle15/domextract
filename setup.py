from setuptools import setup, find_packages

setup(name="domextract",
      version="0.0.3",
      description="Web article extractor",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/domextract",
      packages=find_packages(),
      install_requires=[
          "beautifulsoup4==4.10.0",
          "mecab-python3",
          "numpy==1.19.5",
          "pandas",
          "requests",
          "scikit-learn==0.24.2"
      ],
      package_data={
          'domextract':["*"]
      }
)
