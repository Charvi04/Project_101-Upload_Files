import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'zwxqQ-AhkhUAAAAAAAAAAbpUotA6Dh8_rOQHlxzQ5ckMtdXs_Jy_4eFaYj8mWRIt'
    transferData = TransferData(access_token)

    file_from = 'Sample_File/sampleFile.txt'
    file_to = '/Project_101/sampleFile.txt'

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()