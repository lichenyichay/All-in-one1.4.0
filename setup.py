# coding:UTF-8
import setuptools

setuptools.setup(
    name="All-in-one",
    version="2.3.0",
    author="Chay",
    author_email="lichenyi_2020@qq.com",
    url="https://github.com/lichenyichay/All-in-one1.4.0/tree/2.3.0",
    description="All-in-one",
    long_description="多功能一体机",
    python_requires=">=3.0.0",
    # packages=setuptools.find_packages("src"),
    packages_dir={"": "src"},
    packages_data={"": ["*.txt", "*.info", "*.properties"], "": ["data/*.*"]},
    exclude=["*.test", "*.test.*", "test.*", "test"],
    classifiers=['Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2",
                 "Programming Language :: Python :: 3"
                 ]
)
