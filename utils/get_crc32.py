import zlib


def get_crc32(data: str) -> str:
    """Вычислить CRC32 для строки"""
    return format(zlib.crc32(data.encode()), '08x')