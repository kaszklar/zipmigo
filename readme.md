# Zipmigo
Zipmigo is intended to assist fledgling data analysts and scientists with the process of downloading a zip file via http and unzipping it into the working directory when working in a notebook environment, saving them time and energy wading through `os`, `requests`, and running shell commands to inspect the directory structure.

### Story
This package was born of the author's hatred for recursive folders within zip files, as well as her need to use the same commands over and over again to download & unpack zip archives. Over the course of a project, she found herself constantly reusing code snippets - a sign that one should wrap it up into a script. However, she was working in google colab, which was designed for collaborative notebook workflows. It seemed that distributing a package on PyPi was the easiest way to import a script into colab for her audience, and thus zipmigo was born.

### Installation
Zipmigo is available for commandline installation from PyPi via `pip install zipmigo`.

#### Google Colab
Run `!pip install zipmigo`  

Or, as of February 2020, to pull in Zipmigo *directly from github*;
```sh
!curl --remote-name \
     -H 'Accept: application/vnd.github.v3.raw' \
     --location https://raw.githubusercontent.com/kaszklar/zipmigo/master/zipmigo.py
```

### Examples
#### Importing
If you installed via pip:  
`from zipmigo import zipmigo`  
If you are working from the source file:  
`import zipmigo`  

#### Download a zip file
Download a file to the current working directory. The status of the connection and the progress of the download will be printed out.

```python  
zipmigo.download("https://geo.nyu.edu/download/file/harvard-ntadcd106-shapefile.zip", 'congressdistricts.zip')
```

#### Print out the contents of the current working directory & subdirectories
```python
zipmigo.list_dir()
```

#### Unzip
Unpack zip file into current directory. If the archive has only directories in the root, those directories will be placed in the current working directory.

```python
zipmigo.unzip("congressdistricts.zip")
```

### Release History
[1.0.1] 2020.05.05  
Some error handling and type assertions  
Correct readme instructions  

[1.0.0] 2020.02.13  
Initial Release :tada:  

### Future features?
* Inspect zip archive prior to opening
* Extract a single file from the archive
