import os
import hashlib
import qrcode
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from blockchain import w3, contract, default_account, private_key

app = Flask(__name__)

# Folder configuration
UPLOAD_FOLDER = 'static/uploads/'
QR_FOLDER = 'static/qrcodes/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['QR_FOLDER'] = QR_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(QR_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_qr_code(image_url, qr_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(image_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(os.path.join(QR_FOLDER, qr_filename))

@app.route('/')
def home():
    return render_template('home.html', qr_code=request.args.get('qr_code'))

@app.route('/debug')
def debug():
    return "✅ Flask app is running and blockchain connected!"

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('No file selected.')
            return redirect(request.url)

        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            # Generate SHA256 hash → bytes32
            with open(file_path, 'rb') as f:
                hex_hash = hashlib.sha256(f.read()).hexdigest()
                bytes32_hash = w3.to_bytes(hexstr=hex_hash)

            # Send transaction
            try:
                tx = contract.functions.storeQRHash(bytes32_hash).build_transaction({
                    'from': default_account,
                    'nonce': w3.eth.get_transaction_count(default_account),
                    'gas': 300000,
                    'gasPrice': w3.to_wei('10', 'gwei')
                })
                signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
                tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
                w3.eth.wait_for_transaction_receipt(tx_hash)
                flash("✅ QR hash stored on blockchain.")
            except Exception as e:
                flash(f"❌ Blockchain error: {e}")
                return redirect(request.url)

            # Create QR code
            image_url = url_for('static', filename=f'uploads/{filename}', _external=True)
            qr_filename = f"{os.path.splitext(filename)[0]}_qr.png"
            generate_qr_code(image_url, qr_filename)
            return redirect(url_for('home', qr_code=qr_filename))
        else:
            flash('Invalid file type.')
    return render_template('generate.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('No file selected.')
            return redirect(request.url)

        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            with open(file_path, 'rb') as f:
                hex_hash = hashlib.sha256(f.read()).hexdigest()
                bytes32_hash = w3.to_bytes(hexstr=hex_hash)

            try:
                is_valid = contract.functions.verifyQRHash(bytes32_hash).call()
                if is_valid:
                    flash("✅ QR code is VALID and exists on blockchain.")
                else:
                    flash("❌ QR code NOT found on blockchain.")
            except Exception as e:
                flash(f"❌ Blockchain error during validation: {e}")
            return redirect(url_for('validate'))
        else:
            flash('Invalid file type.')
    return render_template('validate.html')

if __name__ == '__main__':
    app.run(debug=True)
