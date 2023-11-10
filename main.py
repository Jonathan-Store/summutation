def main(): #use eval()

    import tkinter as tk
    
    root = tk.Tk()
    
    root.geometry("500x300")
    
    nTop = tk.Entry(root)
    nTop.pack()
    
    sigma = tk.Label(root, text= "Σ", font=('Times',50))
    sigma.pack()
    
    nLow = tk.Entry(root)
    nLow.pack()
    
    equationLabel = tk.Label(root, text = "Enter sum: ")
    equationLabel.pack()
    equationEntry = tk.Entry(root)
    equationEntry.pack()
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
