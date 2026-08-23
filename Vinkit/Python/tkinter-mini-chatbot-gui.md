<!-- tags: vinkit, python -->

# Python tkinter: mini-chatbotin GUI

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yksinkertainen esimerkki graafisesta chat-käyttöliittymästä `tkinter`-kirjastolla. Käyttäjä kirjoittaa viestin tekstikenttään, painaa "Send"-nappia, ja botti vastaa aina samalla tavalla.

```python
import tkinter as tk

def respond():
    txt = entry.get()
    chat.insert(tk.END, "You: " + txt + "\nBot: I heard you\n\n")

root = tk.Tk()
chat = tk.Text(root, width=40, height=15)
chat.pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Send", command=respond).pack()
root.mainloop()
```

Esimerkkiajo: kun tekstikenttään kirjoittaa "hello how are you" ja painaa Send, chat-ikkunaan tulostuu:

```
You: hello how are you
Bot: I heard you
```
