import PySimpleGUI as psg
import zip_creator as zip


label_1 = psg.Text("Select files to compress: ")
input_1 = psg.Input("", key="files_input")
button_choose_1 = psg.FilesBrowse("Choose", key="files") # choose file(s)

label_2 = psg.Text("Select destination folder: ")
input_2 = psg.Input("", key="folder_input")
button_choose_2 = psg.FolderBrowse("Choose", key="folder") # choose folder

button_compress = psg.Button("Compress")
button_exit = psg.Button("Exit")
success_output_label = psg.Text(key="success", text_color="green")
fail_output_label = psg.Text(key="fail", text_color="blue")

window_layout = [[label_1, input_1, button_choose_1],
                [label_2, input_2, button_choose_2],
                [button_compress,  button_exit, 
                success_output_label, fail_output_label]]

window = psg.Window("File Zipper", 
                    layout=window_layout)

while True:
        event, values = window.read()
        match event:
                case "Compress":
                        filepaths = values["files"].split(";")
                        folder = values["folder"]
                        if len(filepaths) >= 1 and len(folder) >= 1:
                                ''' Test if there's an input '''
                                zip.success_message(window, first_key="success", second_key="fail")
                                zip.make_archive(filepaths, folder)
                                zip.update_input_boxes(window, first_key="files_input", second_key="folder_input")
                        else:
                                zip.fail_message(window, first_key="success", second_key="fail")
                                continue
                case "Exit":
                        break
                case psg.WINDOW_CLOSED:
                        break

window.close()
