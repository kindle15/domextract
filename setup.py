from setuptools import setup, find_packages

setup(name="domextract",
      version="0.0.1a",
      description="Web article extractor",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/domextract",
      packages=find_packages(),
      install_requires=[
          "numpy==1.14.3",
          "scikit-learn==0.19.1",
          "pandas==0.23.0",
          "bs4==0.0.1",
          "mecab-python3==0.7"
      ],
      package_data={
          'domextract':["*"]
      }
)
