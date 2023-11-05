import PySimpleGUI as psg
import zipfile as zip
import pathlib


def make_archive(filepaths, destination_dir):
    ''' Gets the path of choosen files and add to the choosen directory
    '''
    destination_path = pathlib.Path(destination_dir, "compressed.zip")
    with zip.ZipFile(destination_path, 'w') as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


def update_input_boxes(window, first_key, second_key):
    ''' Update the window and input boxes using keys as parameters '''
    window[first_key].update(value='')
    window[second_key].update(value='')


def fail_message(window, first_key, second_key):
    ''' Make fail message appear on screen '''
    window[first_key].update(visible=False)
    window[second_key].update(visible=True)
    window[second_key].update(value="Please enter a path.")


def success_message(window, first_key, second_key):
    ''' Make success message appear and if fail is
    on screen then hide it '''
    window[second_key].update(visible=False)
    window[first_key].update(visible=True)
    window[first_key].update(value="Compressed with success!")