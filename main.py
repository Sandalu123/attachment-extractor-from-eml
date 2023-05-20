import os
import email
from email import policy

def extract_attachments(filename, output_dir, counter):
    with open(filename, 'rb') as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    for part in msg.iter_parts():
        if part.get_content_disposition() == 'attachment':
            data = part.get_payload(decode=True)
            if data is None:
                continue
            filename = part.get_filename()
            if filename:
                filename_mod = filename.replace(".txt","")
                path = os.path.join(output_dir, f"{filename_mod}_{counter}.txt")
                with open(path, 'wb') as out_file:
                    out_file.write(data)
                print(f'Extracted: {path}')
                counter += 1
    return counter

def crawl_directory(directory, output_dir):
    counter = 1
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.eml'):
                counter = extract_attachments(os.path.join(root, file), output_dir, counter)

if __name__ == "__main__":
    crawl_directory('C:\\Users\\Desktop-SandaluP\\Desktop\\mail\\mails', 'C:\\Users\\Desktop-SandaluP\\Desktop\\mail\\attach')
