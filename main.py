from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
import requests
import json

kv = """
<MainBoxLayout>:
    orientation: "vertical"
    padding: "10dp"
    spacing: "10dp"

    MDTextField:
        id: text_field
        hint_text: "Entre une URL (ex: http://localhost:3000/api/post/)"
        size_hint_x: 1

    MDLabel:
        id: label_status
        text: "Status : en attente"
        halign: "center"

    MDLabel:
        id: label_response
        text: "Réponse :"
        halign: "center"

    MDRaisedButton:
        text: "Faire la requête"
        size_hint: 1, None
        on_press: root.message_request()
"""

class MainBoxLayout(MDBoxLayout):
    def message_request(self):
        url = self.ids.text_field.text.strip()

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # lève erreur HTTP si 4xx ou 5xx

            # Essayer de parser en JSON
            try:
                data = response.json()
                message = json.dumps(data, indent=2, ensure_ascii=False)
            except ValueError:
                # Si pas du JSON, afficher brut
                message = response.text

            self.ids.label_status.text = f"✅ Status : {response.status_code}"
            self.ids.label_response.text = f"Réponse :\n{message}"

        except requests.exceptions.ConnectionError:
            self.ids.label_status.text = "❌ Pas de connexion à l'API"
            self.ids.label_response.text = "L'URL est peut-être fausse ou le serveur est éteint."

        except requests.exceptions.Timeout:
            self.ids.label_status.text = "⌛ Timeout"
            self.ids.label_response.text = "Le serveur a mis trop de temps à répondre."

        except requests.exceptions.HTTPError as e:
            self.ids.label_status.text = f"⚠️ Erreur HTTP {e.response.status_code}"
            self.ids.label_response.text = e.response.text

        except requests.exceptions.RequestException as e:
            self.ids.label_status.text = "🚨 Erreur inattendue"
            self.ids.label_response.text = str(e)


class Tasks(MDApp):
    def build(self):
        Builder.load_string(kv)
        return MainBoxLayout()


if __name__ == "__main__":
    Tasks().run()
