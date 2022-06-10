import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken=accessToken
    def uploadFile(self,fileFrom, fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        with open(fileFrom, "rb") as f:
            dbx.files_upload(f.read(),fileTo)
def main():
    accessToken="sl.BJN6L0Gul6P_l3jZ0CitQM7tUy1SvG5TeVvVUzBO41ZTvYfYJkw1XVOq3Xj380YrQatRbXogZxIQaxgVirwfeUu9E6CWb_Z0KqRxJBUwTlLb6Caddht5I-3Kus3vAYh7hDGtTQc"
    transferData=TransferData(accessToken)

    fileFrom=input("Enter the file here: ")
    fileTo=input("Enter the place to store: ")

    transferData.uploadFile(fileFrom,fileTo)
    print(fileFrom+"has been moved successfully")
main()

