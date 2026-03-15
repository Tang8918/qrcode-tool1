try:
    import qrcode
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'qrcode[pil]', '-q'])
    import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data('https://qrcode-tool1.vercel.app')
qr.make(fit=True)
img = qr.make_image(fill_color='#4f46e5', back_color='white')
img.save('E:/2026新/qrcode-site/site-qrcode.png')
print('done')
