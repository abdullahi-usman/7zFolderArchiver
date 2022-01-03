


import os

class SevenZipDirArchiver:
	def __init__(self, seven_zip=os.getenv("7z")):
		self.seven_zip = self.__quote_str(seven_zip)
		
		
	def __quote_str(self, _str):	
		if ' ' in _str and len(_str) > 0:
			_str_new = ''

			if _str[0] == os.sep:
				_str_new += os.sep

			for split in _str.split(os.sep):
				
				if split.isspace():
					continue

				if " " in split:
					split = "\"" + split + "\""

				_str_new += split + os.sep
			else:
				_str_new = _str_new.removesuffix(os.sep)
			
			return _str_new
		return _str

					
	def __exceve(self, files):
		if len(files) <= 0 or files.isspace():
			return

		pr = "{program} a {output} {files}".format_map({"program":  self.seven_zip, "output": self.__quote_str(self.folder_name.strip()), "files": files})
		
		os.system(pr)
		

	def __encode(self, cur_folder):

		if self.nest_dir:
			output_path = self.output + cur_folder.replace(self.folder, '')
		else:
			output_path = self.output

		if not os.path.exists(output_path):
			os.makedirs(output_path, exist_ok=True)

		if os.getcwd() != output_path:
			os.chdir(output_path)

				
		files = ''
		for name in os.listdir(cur_folder):
			dir_name = cur_folder + os.sep + name
			
			
			if os.path.isdir(dir_name):
				self.folder_name = name
				self.__encode(dir_name)

			elif os.path.isfile(dir_name):
				if len(files) >= 8000:
					self.__exceve(files)
					files = ''
					
				else:
					if " " in dir_name:
						dir_name = self.__quote_str(dir_name.strip())
				
					files += dir_name + ' '
		else:
			self.__exceve(files)
			
			if self.nest_dir:
				output_path = os.path.dirname(output_path)
				os.chdir(output_path)

			files = ''

	def enable_nested_dirs(self, enabled=True):
		self.nest_dir = enabled
		
	def encode_dir(self, folder, output):
		self.folder = folder

		if output.isspace():
			output = "output"

		self.output = os.path.abspath(output)

		self.folder_name = os.path.basename(self.folder)

		if self.seven_zip == None or self.folder == None:
			print("Either 7z executable path is nor set or Folder to zip is not set")
			exit(0)

		if not os.path.exists(self.output):
			os.makedirs(output)

		self.__encode(self.folder)