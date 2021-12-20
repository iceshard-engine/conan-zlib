# conan-recipe-template
A template repository to be used for new Conan recipes.

## The '.gitattributes'

Required to ensure that both on Windows and Linux files used in calculating the Recipe Revision Hash are exactly the same.
The problem here is, that different line endings will produce a different recipe hash, which in turn will make packages incompatible depending on which system was uploading it's recipe first.

## The 'conanfile.py' 

This file provides a skeleton that can be used withing this repository to build recipes. 
