from setuptools import setup, find_packages

setup(name="domextract",
      version="0.0.2alpha",
      description="Web article extractor",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/domextract",
      packages=find_packages(),
      install_requires=[
          "beautifulsoup4==4.10.0",
          "mecab-python3==0.996.1",
          "numpy==1.19.5",
          "pandas==0.25.1",
          "requests==2.26.0",
          "scikit-learn==0.24.2"
      ],
      package_data={
          'domextract':["*"]
      }
)
