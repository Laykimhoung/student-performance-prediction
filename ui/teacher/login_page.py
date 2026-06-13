from ui.components.login_template import LoginTemplate
from database.crud import validate_teacher


class TeacherLoginPage(LoginTemplate):

    def __init__(self, parent):

        super().__init__(
            parent=parent,
            role_name="Teacher",
            accent_color="#EF4444",
            accent_hover="#DC2626",
            accent_bg="#7F1D1D",
            icon_path="assets/icons/teacher2.png",
            hero_title="Welcome.",
            hero_subtitle="Access your classroom securely",
            login_command=self.login
        )

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        teacher = validate_teacher(
            username,
            password
        )

        if teacher:
            self.master.master.show_teacher_dashboard()
        else:
            print("Wrong teacher credentials")