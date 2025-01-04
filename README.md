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
