from urllib.request import urlopen
from urllib.error import HTTPError
import asyncio

decrypted_text_files = []


# gets the content from the url and writes to the target file in binary mode
async def downloadThread(url, target_file):
    try:
        response = urlopen(url)
        with open(target_file, 'wb') as f:
            f.write(response.read())
    except HTTPError as err:
        print(f'status of the request is {err.code}')
        print(f'reason of the error is {err.reason}')


# put the file content in a string, decrypt it and add it to the global list data structure
async def decryptThread(encrypted_text):
    result = ''
    offset = 8
    try:
        with open(encrypted_text) as f:
            decrypted_text = f.read()
    except FileNotFoundError:
        print('The file to decrypt does not exist.')

    # for each lower case letter perform the Caesar decryption (it is known that the text letters are in lower case)
    for c in decrypted_text:
        if c.islower():
            c_index = ord(c) - ord('a')
            new_index = (c_index - offset) % 26
            new_unicode = new_index + ord('a')
            new_character = chr(new_unicode)
            result = result + new_character
        else:
            result += c

    decrypted_text_files.append(result)


# gets a future aggregating the results from the given coroutines, in the order of the original sequence
async def asyncMain():
    await asyncio.gather(
        downloadThread('https://advpython.000webhostapp.com/s1.txt', 's1_enc.txt'),
        downloadThread('https://advpython.000webhostapp.com/s2.txt', 's2_enc.txt'),
        downloadThread('https://advpython.000webhostapp.com/s3.txt', 's3_enc.txt'),
        decryptThread('s1_enc.txt'),
        decryptThread('s2_enc.txt'),
        decryptThread('s3_enc.txt')
    )


# if the list with decrypted texts is not empty, join them and write to a file
def combiner():
    if decrypted_text_files:
        with open('s_final.txt', 'w') as f:
            f.write('\n'.join(decrypted_text_files))

        with open('s_final.txt', 'r') as f:
            print(f'Enjoy this beautiful song:\n\n{f.read()}')
    else:
        print('Could not properly combine the text...')


if __name__ == '__main__':
    asyncio.run(asyncMain())
    combiner()
