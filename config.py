class Settings:
    def __init__(self):
        self.name = "My tamagochi"
        self.theme = "green"
        self.SPACE = 640
    def get_caption(self) -> str:
        return self.name + " - Retrogochi"
config = Settings()