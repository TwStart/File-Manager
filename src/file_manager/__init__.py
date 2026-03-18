from .file_manager import FileManager

def create_folder(path_name):
    return FileManager.create_folder(path_name)

def create_file(name, content=""):
    return FileManager.create_file(name, content)

def rename(current_name, new_name):
    return FileManager.rename(current_name, new_name)

def delete(path):
    return FileManager.delete(path)

def list_files(directories=None):
    return FileManager.list_files(directories)