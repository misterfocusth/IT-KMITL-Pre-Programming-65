"""This is Docstring"""


def main():
    """เลือกคนคุยให้หน่อย"""
    char_1 = input()
    char_2 = input()
    if (char_1 == "Calm" and char_2 == "Empathetic") \
            or (char_2 == "Calm" and char_1 == "Empathetic"):
        print("Ice")
    elif (char_1 == "Reliable" and char_2 == "Courageous") \
            or (char_2 == "Reliable" and char_1 == "Courageous"):
        print("Fern")
    elif (char_1 == "Optimistic" and char_2 == "Cheerful") \
            or (char_2 == "Optimistic" and char_1 == "Cheerful"):
        print("Bam")
    elif (char_1 == "Attractive" and char_2 == "Creative") \
            or (char_2 == "Attractive" and char_1 == "Creative"):
        print("Tangmo")
    elif (char_1 == "Cheerful" and char_2 == "Creative") \
            or (char_2 == "Cheerful" and char_1 == "Creative"):
        print("Mild")
    elif (char_1 == "Reliable" and char_2 == "Optimistic") \
            or (char_2 == "Reliable" and char_1 == "Optimistic"):
        print("Prae")
    elif (char_1 == "Courageous" and char_2 == "Calm") \
            or (char_2 == "Courageous" and char_1 == "Calm"):
        print("Dream")
    elif (char_1 == "Empathetic" and char_2 == "Attractive") \
            or (char_2 == "Empathetic" and char_1 == "Attractive"):
        print("Aom")


main()
