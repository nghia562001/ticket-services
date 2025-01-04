Hướng dẫn clone addons ticket-services cho Odoo
----

> **Để `clone` addons `ticket-services`, chạy các lệnh sau:**

```bash
cd /opt/odoo/odoo-custom-addons
sudo git clone https://github.com/nghia562001/ticket-services.git
```

Hướng dẫn pull addons ticket-services cho Odoo
----

> **Để `pull` addons `ticket-services`, chạy các lệnh sau:**

```bash
cd /opt/odoo/odoo-custom-addons/ticket-services
sudo git pull origin main
```

Khởi động lại các dịch vụ trong services
----
> **Để `restart` dịch vụ cập nhật addons `ticket-services`, chạy các lệnh sau:**

```bash
sudo systemctl daemon-reload
sudo systemctl restart odoo
sudo systemctl enable odoo
```

> **Kiểm tra trạng thái `status` của services:**

```bash
sudo systemctl status odoo
```

