#!/usr/bin/python3

def validUTF8(data):

    n_bytes = 0

    m_1 = 1 << 7
    m_2 = 1 << 6

    for i in data:

        m_byte = 1 << 7

        if n_bytes == 0:

            while m_byte & i:
                n_bytes += 1
                m_byte = m_byte >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (i & m_1 and not (i & m_2)):
                return False

        n_bytes -= 1

    if n_bytes == 0:
        return True

    return False