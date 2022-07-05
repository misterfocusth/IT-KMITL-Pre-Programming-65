"""This is Docstring"""


def main():
    """วันจันทร์ฉันคิดถึงเธออยู่ วันอังคารไปหาได้ไหม"""
    input_seconds = int(input())
    days = str(input_seconds // 86400).zfill(2)
    hours = str(input_seconds // 3600 % 24).zfill(2)
    mins = str(input_seconds // 60 % 60).zfill(2)
    seconds = str(input_seconds % 60).zfill(2)
    print("%s:%s:%s:%s" % (days, hours, mins, seconds))


main()
