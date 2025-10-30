from flask import Flask, request, jsonify, render_template, send_file
import qrcode
import qrcode.image.svg
from io import BytesIO
import base64
import os
import uuid

app = Flask(__name__)

# Directory to store uploaded files (for file QR codes)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# =====================
# TEXT TO QR
# =====================
# TEXT TO QR
@app.route('/generate-qr-text', methods=['POST'])
def generate_qr_text():
    text = request.form.get('text') or (request.json.get('text') if request.is_json else None)
    if not text:
        return jsonify({'success': False, 'error': 'No text provided'}), 400

    img = qrcode.make(text)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return jsonify({'success': True, 'data': text, 'qr_code': f'data:image/png;base64,{qr_base64}'})

# =====================
# LINK TO QR
# =====================
@app.route('/generate-qr-link', methods=['POST'])
def generate_qr_link():
    link = request.form.get('link') or (request.json.get('link') if request.is_json else None)
    if not link:
        return jsonify({'success': False, 'error': 'No link provided'}), 400

    img = qrcode.make(link)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return jsonify({'success': True, 'data': link, 'qr_code': f'data:image/png;base64,{qr_base64}'})

# =====================
# FILE TO QR
# =====================
@app.route('/generate-qr-file', methods=['POST'])
def generate_qr_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part in request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'}), 400

    filename = f"{uuid.uuid4()}_{file.filename}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    access_url = request.url_root.rstrip('/') + '/' + UPLOAD_FOLDER + '/' + filename

    img = qrcode.make(access_url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return jsonify({'success': True, 'access_url': access_url, 'qr_code': f'data:image/png;base64,{qr_base64}'})

# =====================
# Serve uploaded files
# =====================
@app.route(f'/{UPLOAD_FOLDER}/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))

# =====================
# QR DOWNLOAD
# =====================
@app.route('/download-qr/<qr_type>', methods=['POST'])
def download_qr(qr_type):
    data_to_encode = request.form.get('data')
    image_format = request.form.get('format')

    if not data_to_encode or not image_format:
        return jsonify({'success': False, 'error': 'Missing data or format for download'}), 400

    buffer = BytesIO()
    if image_format == 'png':
        img = qrcode.make(data_to_encode)
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return send_file(buffer, mimetype='image/png', as_attachment=True, download_name=f'qrcode_{qr_type}.png')
    elif image_format == 'svg':
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(data_to_encode, image_factory=factory)
        img.save(buffer)
        buffer.seek(0)
        return send_file(buffer, mimetype='image/svg+xml', as_attachment=True, download_name=f'qrcode_{qr_type}.svg')
    else:
        return jsonify({'success': False, 'error': 'Unsupported format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
