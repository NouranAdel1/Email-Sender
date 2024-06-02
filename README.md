# EmailSender

**Description:**
EmailSender is a Python script that sends an email with an attachment using the SMTP protocol. It uses the `smtplib` library for connecting to an SMTP server and `email` library for constructing the email.

**Features:**
- **SMTP Authentication:** Authenticates with the SMTP server using the provided sender email and password.
- **Email Construction:** Constructs the email with a subject, body text, and an attachment.
- **File Attachment:** Attaches a text file and an image file to the email.

**Files:**
1. **email_sender.py** - This file contains the code to send the email:
    - Connects to the SMTP server.
    - Authenticates using the sender's email and password.
    - Constructs the email with the specified subject, body, and attachments.
    - Sends the email to the recipient.

2. **test.txt** - A sample text file to be attached to the email.
3. **cat.jpg** - A sample image file to be attached to the email.
