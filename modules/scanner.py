import pyautogui
from barcode import Scanner


def read_barcode():
    with Scanner.Scanner() as scn:
        for barcode in scn.scan("/dev/input/eventX"):
            barcode_data = barcode.data
            # Process the barcode data
            print("Barcode Scanned:", barcode_data)
            return barcode_data


def send_barcode_data():

    pyautogui.typewrite(read_barcode())


if __name__ == "__main__":
    send_barcode_data()
