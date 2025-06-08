import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QComboBox, QWidget, QVBoxLayout, QTextEdit, QCheckBox)
from PyQt5.QtCore import Qt


class SongData:
    def __init__(self):
        self.songs = {
            "Creep": {
                "lines": [
                    ("When you were here before", "G     B     C     Cm"),
                    ("I don't care if it hurts", "G     B     C     Cm"),
                    ("I want a perfect body", "G     B     C     Cm"),
                    ("You're so f***ing special", "G     B     C     Cm")
                ]
            },
            "Karma Police": {
                "lines": [
                    ("Karma police, arrest this man", "Am     D       G"),
                    ("He talks in maths", "Am     D       G"),
                    ("This is what you get", "Am     D       G"),
                    ("For a minute there, I lost myself", "Am     D       G")
                ]
            },
            "No Surprises": {
                "lines": [
                    ("A heart that's full up like a landfill", "F     Am    Dm    Bb"),
                    ("Bring down the government", "F     Am    Dm    Bb"),
                    ("They don't speak for us", "F     Am    Dm    Bb"),
                    ("No alarms and no surprises", "F     Am    Dm    Bb")
                ]
            },
            "High and Dry": {
                "lines": [
                    ("Two jumps in a week, I bet you think that's pretty clever", "E     A     C#m     B"),
                    ("You'd kill yourself for recognition", "E     A     C#m     B"),
                    ("You're just like an angel", "E     A     C#m     B"),
                    ("Drying up in conversation", "E     A     C#m     B")
                ]
            },
            "Street Spirit (Fade Out)": {
                "lines": [
                    ("Rows of houses all bearing down on me", "Em     C     G     Bm"),
                    ("I can feel their blue hands touching me", "Em     C     G     Bm"),
                    ("All these things into position", "Em     C     G     Bm"),
                    ("Fade out again", "Em     C     G     Bm")
                ]
            }
        }

    def get_full_text(self, song_name, include_tabs=True):
        song = self.songs.get(song_name, {})
        lines = song.get("lines", [])
        full_text = ""
        for lyric, tab in lines:
            full_text += f"{lyric}\n"
            if include_tabs:
                full_text += f"🎸 {tab}\n"
            full_text += "\n"
        return full_text


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("radioheda")
        self.setGeometry(100, 100, 700, 500)

        self.song_data = SongData()


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("აირჩიე სიმღერა:")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Creep", "Karma Police", "No Surprises",
            "High and Dry", "Street Spirit (Fade Out)"])
        self.layout.addWidget(self.combo_box)


        self.checkbox = QCheckBox("გიტარის აკორდები? მონიშნე :)")
        self.checkbox.setChecked(True)
        self.layout.addWidget(self.checkbox)


        self.button = QPushButton("გამოუშვი")
        self.layout.addWidget(self.button)


        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.layout.addWidget(self.text_area)

        self.button.clicked.connect(self.display_lyrics)

        self.footer_label = QLabel("RADIOHEAD")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #555; letter-spacing: 2px;")
        self.layout.addWidget(self.footer_label)

    def display_lyrics(self):
        selected_song = self.combo_box.currentText()
        show_tabs = self.checkbox.isChecked()
        text = self.song_data.get_full_text(selected_song, include_tabs=show_tabs)
        self.text_area.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

