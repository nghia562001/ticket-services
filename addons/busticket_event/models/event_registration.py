from odoo import models, fields, api # type: ignore
import qrcode
from io import BytesIO
import base64
from PIL import Image
class EventRegistration(models.Model):
    _inherit = 'event.registration'

    pickup = fields.Char(string='Pick up', translate=True)
    
    PROVINCE = [
        ('00', 'Null'),
        ('01', 'Sài Gòn'),
        ('02', 'Long An'),
        ('03', 'Tiền Giang'),
        ('04', 'Vĩnh Long'),
        ('05', 'Cần Thơ'),
        ('06', 'Hậu Giang'),
        ('07', 'Sóc Trăng'),
        ('08', 'Bạc Liêu'),
        ('09', 'Cà Mau'),
    ]

    pickup_point = fields.Selection(
        selection=PROVINCE,
        string="Pickup Point",
        required=True,
        default='00',
    )

    dropoff_point = fields.Selection(
        selection=PROVINCE,
        string="Dropoff Point",
        required=True,
        default='00',
    )

    price = fields.Float(string="Price", compute="_compute_price")

    # Bảng giá giữa các tỉnh
    PRICE_MAP = {
        ('01', '09'): 170000,  # Sài Gòn -> Cà Mau
        # Thêm các tuyến khác nếu cần
    }

    @api.depends('pickup_point', 'dropoff_point')
    def _compute_price(self):
        for record in self:
            key = (record.pickup_point, record.dropoff_point)
            reverse_key = (record.dropoff_point, record.pickup_point)  # Kiểm tra chiều ngược lại
            record.price = self.PRICE_MAP.get(key) or self.PRICE_MAP.get(reverse_key) or 0

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