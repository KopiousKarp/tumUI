import imaplib
import email

imap_server = "imap.gmail.com"
email_address = "evanstum369@gmail.com"
password = "*******"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, "hmmk flxo bdvk uskn")

imap.select("Inbox")
_, msgnums = imap.search(None, "ALL")

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    strcheck = message.get('From')
    str_subject_check = message.get('Subject')
    if strcheck == "evanstum369@gmail.com":
        print(f"Message Number: {msgnum}")
        print(f"From: {message.get('From')}")
        print(f"To: {message.get('To')}")
        print(f"Date: {message.get('Date')}")
        print(f"Subject: {message.get('Subject')}")
        if str_subject_check == "TUMBOT, Go to 3D Printers":
            tcp_comm = 1;imap.close()
        if str_subject_check == "TUMBOT, Go to Oscilloscope":
            tcp_comm = 1;imap.close()
        if str_subject_check == "TUMBOT, Go to soldering iron":
            tcp_comm = 1;imap.close()
        if str_subject_check == "TUMBOT, Go to multimeter":
            tcp_comm = 1;imap.close()
        if str_subject_check == "TUMBOT, Go to screw drivers":
            tcp_comm = 1;imap.close()
