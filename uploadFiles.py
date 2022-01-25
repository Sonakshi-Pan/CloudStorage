import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

          # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:

                # construct the full local path
                local_path = os.path.join(root, filename)

                  # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                 # upload the file
                with open(local_path, 'rb') as f:
                     dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BAxVVVSMDaRYQxCQV-9onEHSao9WODOudRI3aYlKmQdlwl7g7D7Z45kMVFXRxLB4_CkzHEEdvQH5q2T4KvWnXQZ0NtrhtGKVnHqbG76zeC0dX8ofaEE33VfHD9YtLpbUpOwGj6c'
    transferData = TransferData(access_token)

    file_from = str(input("enter the folder path to transfer :-"))
    file_to = input("enter the full path to upload to dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("files removed")


main()


