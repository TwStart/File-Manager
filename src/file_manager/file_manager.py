import os
from send2trash import send2trash

class FileManager:

    """

    A SIMPLIFIED LIBRARY FOR FILE AND FOLDER
    MANAGEMENT. IDEAL FOR FAST SCRIPTING AND
    SAVING TIME.

    """

    MAX_NAME_LENGHT = 30
    
    @staticmethod
    def _validate_name(name):

        """
        validation of allowed characters for the name of a folder or file.
        """

        if len(name) > FileManager.MAX_NAME_LENGHT:
            return False, f"Error: Name '{name}' exceeds {FileManager.MAX_NAME_LENGTH} characters."
        if not name.strip():
            return False, f"Error: name cannot be empty."
        return True, None

    @staticmethod
    def create_folder(path_name):

        """
        function for creating folders.
        """

        is_valid, error_msg = FileManager._validate_name(path_name)
        if not is_valid: return error_msg

        try:
            os.makedirs(path_name, exist_ok=True)
            return f"folder: '{path_name}' created successfully."
        except Exception as Folder:
            return f"Error creating folder: {Folder}"
        
    @staticmethod
    def create_file(file_name, content=""):

        """
        function for a creation files.
        """

        is_valid, error_msg = FileManager._validate_name(file_name)
        if not is_valid: return error_msg

        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(content)
            return f"File: '{file_name}' created successfully."
        except Exception as e:
            return f"Error creating file: {e}"

    @staticmethod    
    def rename(current_name, new_name):
        is_valid, error_msg = FileManager._validate_name(new_name)
        if not is_valid: return error_msg

        try:
            os.rename(current_name, new_name)
            return f"{current_name} has been renamed to {new_name}"
        except FileNotFoundError:
            return "Error: The file or folder does not exist."
        except Exception as e:
            return f"Renaming error: {e}"
        
    @staticmethod
    def delete(path):
        if not os.path.exists(path):
            return f"Error: '{path}' does not exist."

        try:
            if os.path.isfile(path):
                os.remove(path)
                return f"File '{path}' deleted."
            elif os.path.isdir(path):
                send2trash(path)
                return f"Folder '{path}' and its contents deleted."
            else:
                return "Error: The path does not exist."
        except Exception as e:
            return f"Error deleting: {e}"
        
    @staticmethod
    def list_files(directories=None):
        target = directories if directories else "."

        if not os.path.exists(target):
            return f"Error: The path '{target}' does not exist."

        print(f"--- Exploring all the content of: {os.path.abspath(target)} ---")

        for root, dirs, files in os.walk(target):
            level = root.replace(target, '').count(os.sep)
            index = ' ' * 4 * level

            print(f"{index}📁 [{os.path.basename(root)}/]")
            sub_index = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{sub_index}📄 {f}")

    @staticmethod            
    def move_files(source_path, destination_route):

        """
        function to manage and move files.
        """

        if not os.path.exists(source_path):
            raise FileNotFoundError(f"The source file does not exist: {source_path}")
        
        directory = os.path.dirname(destination_route)

        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        os.rename(source_path, destination_route)
        print(f"File successfully moved to: {destination_route}")