import hashlib


def cal_sha1(message):
    """
        Trans the str into its SHA-1 style
    :param message: a str
    :return: 160 bits SHA-1 encoded str
    """
    sha1 = hashlib.sha1()
    data = message
    sha1.update(data.encode('utf-8'))
    sha1_data = sha1.hexdigest()
    # print(sha1_data, ', length = ', len(sha1_data), 'Bytes')
    return sha1_data


if __name__ == '__main__':
    ' For .test stuff, ... '
    print(" Calling cal_sha1(): ", cal_sha1('Python 3000'))
    print(" Calling hashlib's : ", '57065656bf4e4803789bbc52cfd63edf0533d55b')
