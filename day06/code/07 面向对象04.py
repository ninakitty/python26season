class Msg:
    def email(self):
        pass
    def chat(self):
        pass
    def wechat(self):
        pass
    def app(self):
        pass

    def important(self):
        self.email()
        self.chat()
        self.app()

msg = Msg()
msg.important()