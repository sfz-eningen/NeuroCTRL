class Settings():
    settings = {
        "Streams": {
            "function": "AutoStream",
            "data": [
                {"name": "BandPower", "api": False, "type": "band", "page": "/band_power"}
            ]
        },

        "ui": {
            "gui": False,
            "data": [
                "band"
            ]
        },
    }
    def __init__(self):
        self.Streams = self.settings["Streams"]["data"]
        pass