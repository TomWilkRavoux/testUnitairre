from abc import ABC, abstractmethod

class IFileExplorer(ABC):
    @abstractmethod
    def display_directory_contents(self):
        pass

    @abstractmethod
    def navigate(self, index):
        pass

    @abstractmethod
    def go_to_parent_directory(self):
        pass


class IFileSelector(ABC):
    @abstractmethod
    def load_directory_contents(self, directory_path):
        pass

    @abstractmethod
    def select_files_by_indices(self, indices, directory_path):
        pass

    @abstractmethod
    def get_selected_files(self):
        pass

    @abstractmethod
    def clear_selection(self):
        pass


class IFileManager(ABC):
    @abstractmethod
    def copy_files(self, destination):
        pass

    @abstractmethod
    def move_files(self, destination):
        pass

    @abstractmethod
    def delete_files(self):
        pass
