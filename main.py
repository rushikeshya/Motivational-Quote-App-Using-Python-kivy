import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import choice

# List of Motivational Quotes
quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
     "Act as if what you do makes a difference. It does. - William James",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Quality is not an act, it is a habit. - Aristotle",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau"
]

class QuoteApp(App):
    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Quote Labels
        self.quote_label = Label(text="Tap the button to get a quote", font_size=18, halign='center', size_hint_y=None, height=150)
        layout.add_widget(self.quote_label)

        # Button to get a new quote
        btn = Button(text="New Quote", size_hint_y=None, height=50, on_press=self.update_quote)
        layout.add_widget(btn)

        return layout
    
    def update_quote(self, instance):
        """This function updates the quote text."""
        new_quote = choice(quotes)
        parts = new_quote.split(" - ")
        self.quote_label.text = f"[b]{parts[0]}[/b]\n\n- {parts[1]}" if len(parts) > 1 else new_quote
        self.quote_label.markup = True 

# Run the App

if __name__ == "__main__":
    QuoteApp().run()