from PIL import Image
import sys

PALETTE_DATA = [
    0x00, 0x00, 0x00, 0x00, 0x00, 0xAA, 0x00, 0xAA, 0x00, 0x00, 0xAA, 0xAA, 0xAA, 0x00, 0x00, 0xAA, 0x00, 0xAA, 0xAA, 0x55, 0x00, 0xAA, 0xAA, 0xAA,
    0x55, 0x55, 0x55, 0x55, 0x55, 0xFF, 0x55, 0xFF, 0x55, 0x55, 0xFF, 0xFF, 0xFF, 0x55, 0x55, 0xFF, 0x55, 0xFF, 0xFF, 0xFF, 0x55, 0xFF, 0xFF, 0xFF,
    0x00, 0x00, 0x00, 0x10, 0x10, 0x10, 0x20, 0x20, 0x20, 0x35, 0x35, 0x35, 0x45, 0x45, 0x45, 0x55, 0x55, 0x55, 0x65, 0x65, 0x65, 0x75, 0x75, 0x75,
    0x8A, 0x8A, 0x8A, 0x9A, 0x9A, 0x9A, 0xAA, 0xAA, 0xAA, 0xBA, 0xBA, 0xBA, 0xCA, 0xCA, 0xCA, 0xDF, 0xDF, 0xDF, 0xEF, 0xEF, 0xEF, 0xFF, 0xFF, 0xFF,
    0x00, 0x00, 0xFF, 0x41, 0x00, 0xFF, 0x82, 0x00, 0xFF, 0xBE, 0x00, 0xFF, 0xFF, 0x00, 0xFF, 0xFF, 0x00, 0xBE, 0xFF, 0x00, 0x82, 0xFF, 0x00, 0x41,
    0xFF, 0x00, 0x00, 0xFF, 0x41, 0x00, 0xFF, 0x82, 0x00, 0xFF, 0xBE, 0x00, 0xFF, 0xFF, 0x00, 0xBE, 0xFF, 0x00, 0x82, 0xFF, 0x00, 0x41, 0xFF, 0x00,
    0x00, 0xFF, 0x00, 0x00, 0xFF, 0x41, 0x00, 0xFF, 0x82, 0x00, 0xFF, 0xBE, 0x00, 0xFF, 0xFF, 0x00, 0xBE, 0xFF, 0x00, 0x82, 0xFF, 0x00, 0x41, 0xFF,
    0x82, 0x82, 0xFF, 0x9E, 0x82, 0xFF, 0xBE, 0x82, 0xFF, 0xDF, 0x82, 0xFF, 0xFF, 0x82, 0xFF, 0xFF, 0x82, 0xDF, 0xFF, 0x82, 0xBE, 0xFF, 0x82, 0x9E,
    0xFF, 0x82, 0x82, 0xFF, 0x9E, 0x82, 0xFF, 0xBE, 0x82, 0xFF, 0xDF, 0x82, 0xFF, 0xFF, 0x82, 0xDF, 0xFF, 0x82, 0xBE, 0xFF, 0x82, 0x9E, 0xFF, 0x82,
    0x82, 0xFF, 0x82, 0x82, 0xFF, 0x9E, 0x82, 0xFF, 0xBE, 0x82, 0xFF, 0xDF, 0x82, 0xFF, 0xFF, 0x82, 0xDF, 0xFF, 0x82, 0xBE, 0xFF, 0x82, 0x9E, 0xFF,
    0xBA, 0xBA, 0xFF, 0xCA, 0xBA, 0xFF, 0xDF, 0xBA, 0xFF, 0xEF, 0xBA, 0xFF, 0xFF, 0xBA, 0xFF, 0xFF, 0xBA, 0xEF, 0xFF, 0xBA, 0xDF, 0xFF, 0xBA, 0xCA,
    0xFF, 0xBA, 0xBA, 0xFF, 0xCA, 0xBA, 0xFF, 0xDF, 0xBA, 0xFF, 0xEF, 0xBA, 0xFF, 0xFF, 0xBA, 0xEF, 0xFF, 0xBA, 0xDF, 0xFF, 0xBA, 0xCA, 0xFF, 0xBA,
    0xBA, 0xFF, 0xBA, 0xBA, 0xFF, 0xCA, 0xBA, 0xFF, 0xDF, 0xBA, 0xFF, 0xEF, 0xBA, 0xFF, 0xFF, 0xBA, 0xEF, 0xFF, 0xBA, 0xDF, 0xFF, 0xBA, 0xCA, 0xFF,
    0x00, 0x00, 0x71, 0x1C, 0x00, 0x71, 0x39, 0x00, 0x71, 0x55, 0x00, 0x71, 0x71, 0x00, 0x71, 0x71, 0x00, 0x55, 0x71, 0x00, 0x39, 0x71, 0x00, 0x1C,
    0x71, 0x00, 0x00, 0x71, 0x1C, 0x00, 0x71, 0x39, 0x00, 0x71, 0x55, 0x00, 0x71, 0x71, 0x00, 0x55, 0x71, 0x00, 0x39, 0x71, 0x00, 0x1C, 0x71, 0x00,
    0x00, 0x71, 0x00, 0x00, 0x71, 0x1C, 0x00, 0x71, 0x39, 0x00, 0x71, 0x55, 0x00, 0x71, 0x71, 0x00, 0x55, 0x71, 0x00, 0x39, 0x71, 0x00, 0x1C, 0x71,
    0x39, 0x39, 0x71, 0x45, 0x39, 0x71, 0x55, 0x39, 0x71, 0x61, 0x39, 0x71, 0x71, 0x39, 0x71, 0x71, 0x39, 0x61, 0x71, 0x39, 0x55, 0x71, 0x39, 0x45,
    0x71, 0x39, 0x39, 0x71, 0x45, 0x39, 0x71, 0x55, 0x39, 0x71, 0x61, 0x39, 0x71, 0x71, 0x39, 0x61, 0x71, 0x39, 0x55, 0x71, 0x39, 0x45, 0x71, 0x39,
    0x39, 0x71, 0x39, 0x39, 0x71, 0x45, 0x39, 0x71, 0x55, 0x39, 0x71, 0x61, 0x39, 0x71, 0x71, 0x39, 0x61, 0x71, 0x39, 0x55, 0x71, 0x39, 0x45, 0x71,
    0x51, 0x51, 0x71, 0x59, 0x51, 0x71, 0x61, 0x51, 0x71, 0x69, 0x51, 0x71, 0x71, 0x51, 0x71, 0x71, 0x51, 0x69, 0x71, 0x51, 0x61, 0x71, 0x51, 0x59,
    0x71, 0x51, 0x51, 0x71, 0x59, 0x51, 0x71, 0x61, 0x51, 0x71, 0x69, 0x51, 0x71, 0x71, 0x51, 0x69, 0x71, 0x51, 0x61, 0x71, 0x51, 0x59, 0x71, 0x51,
    0x51, 0x71, 0x51, 0x51, 0x71, 0x59, 0x51, 0x71, 0x61, 0x51, 0x71, 0x69, 0x51, 0x71, 0x71, 0x51, 0x69, 0x71, 0x51, 0x61, 0x71, 0x51, 0x59, 0x71,
    0x00, 0x00, 0x41, 0x10, 0x00, 0x41, 0x20, 0x00, 0x41, 0x31, 0x00, 0x41, 0x41, 0x00, 0x41, 0x41, 0x00, 0x31, 0x41, 0x00, 0x20, 0x41, 0x00, 0x10,
    0x41, 0x00, 0x00, 0x41, 0x10, 0x00, 0x41, 0x20, 0x00, 0x41, 0x31, 0x00, 0x41, 0x41, 0x00, 0x31, 0x41, 0x00, 0x20, 0x41, 0x00, 0x10, 0x41, 0x00,
    0x00, 0x41, 0x00, 0x00, 0x41, 0x10, 0x00, 0x41, 0x20, 0x00, 0x41, 0x31, 0x00, 0x41, 0x41, 0x00, 0x31, 0x41, 0x00, 0x20, 0x41, 0x00, 0x10, 0x41,
    0x20, 0x20, 0x41, 0x28, 0x20, 0x41, 0x31, 0x20, 0x41, 0x39, 0x20, 0x41, 0x41, 0x20, 0x41, 0x41, 0x20, 0x39, 0x41, 0x20, 0x31, 0x41, 0x20, 0x28,
    0x41, 0x20, 0x20, 0x41, 0x28, 0x20, 0x41, 0x31, 0x20, 0x41, 0x39, 0x20, 0x41, 0x41, 0x20, 0x39, 0x41, 0x20, 0x31, 0x41, 0x20, 0x28, 0x41, 0x20,
    0x20, 0x41, 0x20, 0x20, 0x41, 0x28, 0x20, 0x41, 0x31, 0x20, 0x41, 0x39, 0x20, 0x41, 0x41, 0x20, 0x39, 0x41, 0x20, 0x31, 0x41, 0x20, 0x28, 0x41,
    0x2D, 0x2D, 0x41, 0x31, 0x2D, 0x41, 0x35, 0x2D, 0x41, 0x3D, 0x2D, 0x41, 0x41, 0x2D, 0x41, 0x41, 0x2D, 0x3D, 0x41, 0x2D, 0x35, 0x41, 0x2D, 0x31,
    0x41, 0x2D, 0x2D, 0x41, 0x31, 0x2D, 0x41, 0x35, 0x2D, 0x41, 0x3D, 0x2D, 0x41, 0x41, 0x2D, 0x3D, 0x41, 0x2D, 0x35, 0x41, 0x2D, 0x31, 0x41, 0x2D,
    0x2D, 0x41, 0x2D, 0x2D, 0x41, 0x31, 0x2D, 0x41, 0x35, 0x2D, 0x41, 0x3D, 0x2D, 0x41, 0x41, 0x2D, 0x3D, 0x41, 0x2D, 0x35, 0x41, 0x2D, 0x31, 0x41,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

def main():
    image = Image.open(sys.argv[1])
    image = image.convert("RGB")

    render = Image.new("RGB", (320, 200), (0, 0, 0))
    mask = Image.new("P", (16, 16))

    mask.putpalette(PALETTE_DATA)

    width = int(image.width * (200 / image.height))
    position = (320 - width) // 2

    image = image.resize((width, 200))
    render.paste(image, (position, 0))

    render = render.quantize(palette=mask, dither=Image.FLOYDSTEINBERG)

    data = bytes(render.getdata())
    #render.show()

    with open(sys.argv[2], "wb") as file:
        file.write(data)

if __name__ == "__main__":
    main()