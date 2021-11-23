import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A80tj7kcNlL4zVbSOax4rNFgkZpx2umJ8R-ONxibcR4VElv7DhbsWjnmXmOR-Zzw-M6yT1q75D1oN5H_UvNxijbvnXS4JOEOR4nf71dZW3pxl5XCMXlhLNg6vQ5kwPvSWBU_uto'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer-")
    file_to = input("Enter the path to upload to dropbox-")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    transferData.upload_file(file_from, file_to)
    print("The file has successfully been moved !!!")

main()