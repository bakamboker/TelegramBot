class Config:
    token = '1790675914:AAH6AnHpY2WndsNx3LjOZyN84eOAniFkF_s'
    likes_token = '1802072002:AAEfJeXK2x_PYqako8h2-uvGutWTSmqsCRY'
    debug_main_token = '1955715267:AAFZx7RHHjNHCya-JJKcuF0slXZZ9DnqJDI'

    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'inforesult.json'
    folder_id = '1Vxf88kP7QhgnPL3E_IUZe6DD8ENy4XFP'
    path_to_file = 'https://drive.google.com/file/d/'

    def debug(self):
        self.token, self.debug_main_token = self.debug_main_token, self.token


config = Config()