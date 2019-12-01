class Settings():
    settings = {
        "Streams": {
            "function": "AutoStream",
            "data": [
                {"name": "BandPower", "api": True, "type": "band", "page": "/band_power"}#,
                #{"name": "Focus", "api": False, "type": "fft", "page": "/fft"}
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