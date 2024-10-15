import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")

        # This will store the current expression
        self.expression = ""

        # Entry widget to display the expression
        self.entry = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        # Button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Positioning buttons on the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        self.create_button('C', row_val, col_val, colspan=4)

    def create_button(self, value, row, col, colspan=1):
        button = tk.Button(
            self.root, text=value, font=('Arial', 18),
            command=lambda: self.on_button_click(value)
        )
        button.grid(row=row, column=col, columnspan=colspan, ipadx=20, ipady=20, sticky="nsew")

    def on_button_click(self, value):
        if value == 'C':
            self.expression = ""
        elif value == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += value

        # Update the entry widget with the current expression or result
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
