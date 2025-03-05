import pyautogui
import pyperclip
import tkinter
import time

def automacao(root):
    with open (r"caminho do txt com os emails") as txt_emails:
        emails = txt_emails.read()
        pyperclip.copy(emails)

    ASSUNTO_MENSAGEM = ""
    MENSAGEM = ""
    TITULO_IMG = ""

    time.sleep(1)
    pyautogui.press("win")
    pyautogui.write("outlook")
    pyautogui.press("enter")

    time.sleep(5)

    pyautogui.press(["alt", "c", "t", "o"])

    time.sleep(1)
    with pyautogui.hold("alt"):
        pyautogui.press("space")
        pyautogui.press("x")

    pyautogui.write("Marcelo Prates")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.3)
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("tab")

    pyautogui.write(ASSUNTO_MENSAGEM)
    pyautogui.press("tab")

    pyperclip.copy(MENSAGEM)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press(["enter", "enter"])
    time.sleep(0.5)

    pyautogui.press(["alt", "t", "i", "1", "d"])
    pyperclip.copy(TITULO_IMG)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    pyautogui.moveTo(x = 1347, y = 688)
    pyautogui.click()

    pyautogui.press(["alt", "t", "p", "s", "enter"])
    # abaixo ele envia o email, 
    # preferi desativar pois prefiro verificar primeiro
    # with pyautogui.hold("alt"):
        # pyautogui.press("e")
    root.destroy()

def tempo():
    global timer
    timer = root.after(60000, lambda : automacao(root))

def formatarCentro(tela):
    w = 50
    h = 400

    ws = tela.winfo_screenwidth()
    hs = tela.winfo_screenheight()
        
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return tela.geometry("%dx%d+%d+%d" % (w, h, x, y))

root = tkinter.Tk()
alerta = tkinter.Label(
    root,
    text="Atenção, em 1 minuto o programa irá rodar"
).pack()

botao = tkinter.Button(
    root, 
    text="Rodar Agora", 
    command= lambda : automacao(root)
).pack()

timer = None
tempo()

root.title("ATENÇÃO!")
formatarCentro(root)
root.geometry("250x100")
root.mainloop()