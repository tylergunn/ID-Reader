# Raspberry Pi Barcode Scanner

## Overview

This program is designed to run on a Raspberry Pi W and interact with a 2D barcode scanner, specifically for the PDF417 barcode format. The program reads the barcode information and logs it into a database for further analysis and storage.

## Prerequisites

Before running this program, ensure that you have the following prerequisites set up:

- Raspberry Pi W: Make sure you have a Raspberry Pi W set up and running with an operating system (e.g., Raspbian) and the necessary peripherals (keyboard, mouse, display, etc.).
- Barcode Scanner: Connect a 2D barcode scanner capable of reading PDF417 barcodes to the Raspberry Pi W via a suitable interface (e.g., USB, serial, etc.).
- Database: Set up a database system (e.g., MySQL, SQLite, etc.) and create a database to store the barcode information.

## Installation

1. Clone the repository to your Raspberry Pi W:
   $ git clone https://github.com/your-username/your-repo.git

2. Install the required dependencies:
   $ pip install -r requirements.txt

3. Configure the database connection:

- Open the `config.py` file.
- Modify the configuration variables (e.g., database name, host, username, password) to match your database setup.

4. Set up the database schema:

- Using your preferred database management tool, execute the SQL script provided in `database_schema.sql` to create the necessary table structure.

## Usage

1. Connect the 2D barcode scanner to the Raspberry Pi W.

2. Run the program:
   $ python barcode_scanner.py

3. The program will wait for a barcode scan. Once a barcode is scanned, the information will be logged into the configured database.

Entering virtual environment venv\Scripts\activate and to leave deactivate

## Troubleshooting

- **Barcode scanner not detected**: Ensure that the barcode scanner is properly connected to the Raspberry Pi W and that it is compatible with the Raspberry Pi's interface. Check the scanner's documentation for any specific setup instructions.

- **Database connection issues**: Verify that the database configuration in `config.py` is correct. Ensure that the database server is running and accessible from the Raspberry Pi W.

- **Barcode not recognized**: Double-check that the barcode being scanned is in the PDF417 format and that it is compatible with the connected barcode scanner. Test with different barcodes or consult the scanner's documentation for troubleshooting.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -am 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to modify and distribute the code as per the terms of this license.

## Acknowledgments

Special thanks to the open-source community for providing the necessary libraries and tools used in this project.

If you have any questions or need further assistance, please don't hesitate to contact us. Happy scanning!
