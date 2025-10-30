# QR Code Generator

A modern, responsive web application for generating QR codes from links, files, and text. Built with Python (Flask) and Tailwind CSS.

## Features

- **Link to QR**: Generate QR codes from any valid URL
- **File to QR**: Upload files (PDF, JPG, PNG, DOCX, etc.) and generate QR codes that link to the file
- **Text to QR**: Convert any text message into a QR code
- **Download Options**: Save QR codes as PNG or SVG
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## Tech Stack

- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Backend**: Python (Flask)
- **Database**: MongoDB (optional, for file storage)
- **QR Libraries**: qrcode, segno

## Installation

### Prerequisites

- Python 3.7+
- MongoDB (optional, for file storage)

### Setup

1. Clone the repository or download the files

2. Create a virtual environment and activate it:

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and navigate to `http://127.0.0.1:5000`

## MongoDB Setup (Optional)

If you want to use MongoDB for file storage:

1. Install and start MongoDB on your system
2. The application will automatically connect to MongoDB at `mongodb://localhost:27017/`
3. If MongoDB is not available, the application will fall back to local file storage

## Usage

### Link to QR
1. Enter a valid URL in the input field
2. Click "Generate QR Code"
3. Download the QR code as PNG or SVG

### File to QR
1. Upload a file (supported formats: PDF, JPG, PNG, DOCX, etc.)
2. Click "Generate QR Code"
3. Download the QR code or use the provided access link

### Text to QR
1. Enter your text message
2. Click "Generate QR Code"
3. Download the QR code as PNG or SVG

## Mobile Accessibility

The application is fully responsive and optimized for mobile devices:
- Touch-friendly buttons and input fields
- Adaptive layout that works on all screen sizes
- Fast-loading interface optimized for mobile data usage

## License

This project is open source and available under the MIT License.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [qrcode](https://github.com/lincolnloop/python-qrcode)
- [segno](https://github.com/heuer/segno)