import page
from base.base import Base


class PageLogan(Base):
    # 点击我
    def page_click_wo(self):
        self.base_click(page.wo_click)

    # 点击已有账号,去登录
    def page_click_login(self):
        self.base_click(page.login_click)

    # 输入账号
    def page_input_username(self, username):
        self.base_input(page.loc_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.loc_password, password)

    # 点击登录
    def page_click_denglu(self):
        self.base_click(page.loc_btn_click)