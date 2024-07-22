import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Subtotal and Grand Total Calculator")

        # Input field for initial amount
        self.label_initial = tk.Label(root, text="Enter initial amount:")
        self.label_initial.pack()
        
        self.entry_initial = tk.Entry(root)
        self.entry_initial.pack()

        # Input field for number of steps
        self.label_steps = tk.Label(root, text="Enter number of steps:")
        self.label_steps.pack()

        self.entry_steps = tk.Entry(root)
        self.entry_steps.pack()

        # Button to start calculation
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        # Button to copy subtotal values
        self.copy_button = tk.Button(root, text="Copy Subtotals", command=self.copy_subtotals)
        self.copy_button.pack()

        # Text widget to display results
        self.result_text = tk.Text(root, height=20, width=50)
        self.result_text.pack()


    def calculate(self):
        try:
            initial_amount = float(self.entry_initial.get())
            steps = int(self.entry_steps.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
            return

        sub_totals = []
        current_amount = initial_amount

        # Example fixed formula: multiply by 1.1 at each step
        for _ in range(steps):
            current_amount *= 1.1
            sub_totals.append(current_amount)

        # Clear text widget
        self.result_text.delete(1.0, tk.END)

        # Display sub-totals and grand total
        result_str = f"Initial amount: {initial_amount}\n"
        for i, sub_total in enumerate(sub_totals, start=1):
            result_str += f"Step {i}: {sub_total:.2f}\n"
        result_str += f"Grand Total: {sub_totals[-1]:.2f}"

        self.result_text.insert(tk.END, result_str)


    def copy_subtotals(self):
        subtotals = "\n".join([f"{sub_total:.2f}" for sub_total in self.extract_subtotals()])
        self.root.clipboard_clear()
        self.root.clipboard_append(subtotals)
        self.root.update()  # Required on some systems to ensure clipboard updates immediately
        messagebox.showinfo("Copied", "Subtotals copied to clipboard!")


    def extract_subtotals(self):
        lines = self.result_text.get(1.0, tk.END).strip().split("\n")
        subtotals = []
        for line in lines:
            if line.startswith("Step"):
                subtotals.append(float(line.split(":")[1].strip()))
        return subtotals


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
