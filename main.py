from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image uploaded", 400

    input_image = request.files['image'].read()
    output = remove(input_image)

    return send_file(
        BytesIO(output),
        mimetype='image/png',
        as_attachment=False,
        download_name='removed.png'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
