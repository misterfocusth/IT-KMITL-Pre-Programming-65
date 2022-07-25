"""เรียงข้อความ ยามเธออ่านไม่ตอบ // https://ejudge.it.kmitl.ac.th/problem/7916"""


def solve(txt1, txt2, txt3):
    """Sort text array by text length"""
    text_arr = sorted([txt1, txt2, txt3], key=len)
    print(str(text_arr[0]).title())
    print(str(text_arr[1]).title())
    print(str(text_arr[2]).title())


def main():
    """Main Function"""
    txt1, txt2, txt3 = input(), input(), input()
    solve(txt1, txt2, txt3)


main()
