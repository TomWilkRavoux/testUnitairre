import pytest
from unittest.mock import Mock
from fmgr.futils import FileManager


def test_delete_files():
    # Mock des dépendances
    sel_mock = Mock()
    fs_mock = Mock()
    ui_mock = Mock()

    # Données simulées
    sel_mock.get_and_reset.return_value = ["file1.txt", "file2.txt"]

    # Création de FileManager
    file_manager = FileManager(sel=sel_mock, fs=fs_mock, ui=ui_mock)

    # Appel de la méthode
    count = file_manager.delete_files()

    # Assertions
    assert count == 2                                                   # Vérifie que deux fichiers ont été supprimés
    fs_mock.delete.assert_any_call("file1.txt")                         # Vérifie que 'file1.txt' a été supprimé
    fs_mock.delete.assert_any_call("file2.txt")                         # Vérifie que 'file2.txt' a été supprimé


def test_copy_files():
    sel_mock = Mock()
    fs_mock = Mock()
    ui_mock = Mock()

    sel_mock.get_and_reset.return_value = ["file1.txt", "file2.txt"]

    file_manager = FileManager(sel=sel_mock, fs=fs_mock, ui=ui_mock)
    destination = "/destination/path"

    count = file_manager.copy_files(destination)

    assert count == 2                                                    # Vérifie que deux fichiers ont été copiés
    fs_mock.copy.assert_any_call("file1.txt", destination)
    fs_mock.copy.assert_any_call("file2.txt", destination)

def test_move_files():
    sel_mock = Mock()
    fs_mock = Mock()
    ui_mock = Mock()

    sel_mock.get_and_reset.return_value = ["file1.txt", "file2.txt"]

    file_manager = FileManager(sel=sel_mock, fs=fs_mock, ui=ui_mock)
    destination = "/destination/path"

    count = file_manager.move_files(destination)

    assert count == 2                                                       # Vérifie que deux fichiers ont été déplacés
    fs_mock.move.assert_any_call("file1.txt", destination)
    fs_mock.move.assert_any_call("file2.txt", destination)
