from ui.components.login_template import LoginTemplate
from database.crud import validate_admin

class AdminLoginPage(LoginTemplate):

    def __init__(self, parent):

        super().__init__(
            parent=parent,
            role_name="Admin",
            accent_color="#3B82F6",
            accent_hover="#2563EB",
            accent_bg="#1E3A8A",
            icon_path="assets/icons/admin2.png",
            hero_title="Admin Access.",
            hero_subtitle="Securely manage EduVision AI",
            login_command=self.login
        )

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        admin = validate_admin(
            username,
            password
        )

        if admin:
            self.master.master.show_admin_dashboard()
        else:
            print("Wrong admin credentials")