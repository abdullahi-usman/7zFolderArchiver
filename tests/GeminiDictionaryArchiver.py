import _7zFolderArchiver as _7z
import os



def main():
	encoder = _7z.SevenZipDirArchiver(os.getenv("7z"))
	encoder.enable_nested_dirs(False)
	encoder.encode_dir(os.getenv("Folder"), os.getenv("Output"))


if __name__ == "__main__":
	main()