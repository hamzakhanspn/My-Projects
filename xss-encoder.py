import urllib.parse

def encode_url(url):
    return urllib.parse.quote(url, safe='')

def encode_html(html):
    return html.replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

def encode_payloads(file_path, encoding_type):
    with open(file_path, 'r') as file:
        payloads = file.read().splitlines()

    encoded_payloads = []
    for payload in payloads:
        if encoding_type == 'url':
            encoded_payloads.append(encode_url(payload))
        elif encoding_type == 'html':
            encoded_payloads.append(encode_html(payload))

    with open('encoded_payloads.txt', 'w') as file:
        file.write('\n'.join(encoded_payloads))

if __name__ == '__main__':
    file_path = input("Enter the file path of the XSS payloads: ")
    encoding_type = input("Enter the encoding type (url or html): ")
    encode_payloads(file_path, encoding_type)

    print("Encoded payloads have been written to 'encoded_payloads.txt'.")