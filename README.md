Hướng dẫn clone addons ticket-services cho Odoo
----

> **Để `clone` addons `ticket-services`, chạy các lệnh sau:**

```bash
cd /opt/odoo/odoo-custom-addons
sudo git clone https://github.com/nghia562001/ticket-services.git
```

> **`Để clone addons ticket-services, chạy các lệnh sau:`**

Hướng dẫn pull addons ticket-services cho Odoo
----

> **`Để pull addons ticket-services, chạy các lệnh sau:`**

```bash
cd /opt/odoo/odoo-custom-addons/ticket-services
sudo git pull origin main
```

> **`Khởi động lại services, chạy các lệnh sau:`**

```bash
sudo systemctl daemon-reload
sudo systemctl restart odoo
sudo systemctl enable odoo
```

> **Kiểm tra trạng thái `status` của dịch vụ:**

```bash
sudo systemctl status odoo
```


# Hướng dẫn Clone Addons `ticket-services` cho Odoo

Hướng dẫn này sẽ giúp bạn `clone` addons **`ticket-services`** vào hệ thống Odoo của bạn. Hãy làm theo các bước dưới đây.

---

## 📂 Bước 1: Chuyển đến thư mục chứa custom addons của Odoo

Trước tiên, hãy đảm bảo bạn đang ở đúng thư mục để lưu trữ các custom addons. Chạy lệnh sau:

```bash
cd /opt/odoo/odoo-custom-addons
