from odoo import models, fields, api # type: ignore
import qrcode
from io import BytesIO
import base64
from PIL import Image
class EventRegistration(models.Model):
    _inherit = 'event.registration'

    pickup = fields.Char(string='Pick up', translate=True)

    @api.model
    def generate_qr_code(self, data):
        # Tạo mã QR từ dữ liệu
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Tạo hình ảnh từ mã QR
        img = qr.make_image(fill='black', back_color='white')
        byte_io = BytesIO()
        img.save(byte_io, 'PNG')
        byte_io.seek(0)

        # Mã hóa hình ảnh dưới dạng base64
        return base64.b64encode(byte_io.read()).decode('utf-8')