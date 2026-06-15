import requests


class GSTService:

    @staticmethod
    def verify_gst(gst_number):

        headers = {
            "x-api-key": "YOUR_API_KEY"
        }

        response = requests.get(
            f"https://provider-api-url/{gst_number}",
            headers=headers
        )

        return response.json()