## 7zFolderArchiver

This script can archive nested directories in 7z format and output them in their respective directories
example

If input directory contains:

- directoryA/firstfile.txt 
- directoryA/secondfile.txt 
- directoryA/directoryB/firstfile.txt
- directoryA/directoryB/secondfile.txt
- directoryA/directoryB/thirdfile.txt

output will be:

- directoryA/directoryA.7z
- directoryA/directoryB/directoryB.7z

###  or if nested directory options is disabled the output will be:

- directoryA.7z
- directoryB.7z

Example:
```
import _7zFolderArchiver as _7z

encoder = _7z.SevenZipDirArchiver(os.getenv("7z"))
encoder.enable_nested_dirs(False)
encoder.encode_dir(os.getenv("Folder"), os.getenv("Output"))
```
7z is the path to the 7z executable.

Folder is the folder to archive.

Ouput is the output folder to put the archived files.

