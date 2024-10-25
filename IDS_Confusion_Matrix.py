import tkinter as tk
from tkinter import messagebox

class EvaluationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluation Metrics")

        # Create input fields
        self.create_widgets()

    def create_widgets(self):
        # True Negative
        tk.Label(self.root, text="True Negative (TN)").grid(row=0, column=0)
        self.tn_entry = tk.Entry(self.root)
        self.tn_entry.grid(row=0, column=1)

        # False Negative
        tk.Label(self.root, text="False Negative (FN)").grid(row=1, column=0)
        self.fn_entry = tk.Entry(self.root)
        self.fn_entry.grid(row=1, column=1)

        # False Positive
        tk.Label(self.root, text="False Positive (FP)").grid(row=2, column=0)
        self.fp_entry = tk.Entry(self.root)
        self.fp_entry.grid(row=2, column=1)

        # True Positive
        tk.Label(self.root, text="True Positive (TP)").grid(row=3, column=0)
        self.tp_entry = tk.Entry(self.root)
        self.tp_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(self.root, text="Calculate", command=self.calculate_metrics).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Reset", command=self.reset_fields).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Info", command=self.show_info).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=7, column=0, columnspan=2)

        # Output fields
        self.create_output_labels()

    def create_output_labels(self):
        # True Negative Rate
        tk.Label(self.root, text="True Negative Rate (TNR)").grid(row=8, column=0)
        self.tnr_value = tk.Label(self.root, text="value")
        self.tnr_value.grid(row=8, column=1)

        # Detection Rate
        tk.Label(self.root, text="Detection Rate (DR)").grid(row=9, column=0)
        self.dr_value = tk.Label(self.root, text="value")
        self.dr_value.grid(row=9, column=1)

        # False Positive Rate
        tk.Label(self.root, text="False Positive Rate (FPR)").grid(row=10, column=0)
        self.fpr_value = tk.Label(self.root, text="value")
        self.fpr_value.grid(row=10, column=1)

        # False Negative Rate
        tk.Label(self.root, text="False Negative Rate (FNR)").grid(row=11, column=0)
        self.fnr_value = tk.Label(self.root, text="value")
        self.fnr_value.grid(row=11, column=1)

        # Accuracy
        tk.Label(self.root, text="Accuracy (ACC)").grid(row=12, column=0)
        self.acc_value = tk.Label(self.root, text="value")
        self.acc_value.grid(row=12, column=1)

        # Precision
        tk.Label(self.root, text="Precision (PRE)").grid(row=13, column=0)
        self.pre_value = tk.Label(self.root, text="value")
        self.pre_value.grid(row=13, column=1)

    def calculate_metrics(self):
        try:
            tn = float(self.tn_entry.get())
            fn = float(self.fn_entry.get())
            fp = float(self.fp_entry.get())
            tp = float(self.tp_entry.get())

            # Calculating metrics
            tnr = tn / (tn + fp) if (tn + fp) > 0 else 0
            dr = tp / (tp + fn) if (tp + fn) > 0 else 0
            fpr = 1 - tnr
            fnr = 1 - dr
            acc = (tn + tp) / (tn + tp + fp + fn) if (tn + tp + fp + fn) > 0 else 0
            pre = tp / (tp + fp) if (tp + fp) > 0 else 0

            # Update output labels
            self.tnr_value.config(text=f"{tnr:.4f}")
            self.dr_value.config(text=f"{dr:.4f}")
            self.fpr_value.config(text=f"{fpr:.4f}")
            self.fnr_value.config(text=f"{fnr:.4f}")
            self.acc_value.config(text=f"{acc:.4f}")
            self.pre_value.config(text=f"{pre:.4f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def reset_fields(self):
        self.tn_entry.delete(0, tk.END)
        self.fn_entry.delete(0, tk.END)
        self.fp_entry.delete(0, tk.END)
        self.tp_entry.delete(0, tk.END)
        self.tnr_value.config(text="value")
        self.dr_value.config(text="value")
        self.fpr_value.config(text="value")
        self.fnr_value.config(text="value")
        self.acc_value.config(text="value")
        self.pre_value.config(text="value")

    def show_info(self):
        messagebox.showinfo("Info", "The calculation is driven based on the following:\n"
                                    "TNR=(TN / (TN+FP))\n"
                                    "DR=(TP / (TP+FN))\n"
                                    "FPR=(1-TNR)\n"
                                    "FNR=(1-DR)\n"
                                    "Accuracy=(TN+TP) / (TN+TP+FN+FP)\n"
                                    "Precision=(TP / (TP+FP))\n"
                                    "Where:\n"
                                    "FP: False Positive\n"
                                    "TP: True Positive\n"
                                    "FN: False Negative\n"
                                    "TN: True Negative")

if __name__ == "__main__":
    root = tk.Tk()
    app = EvaluationApp(root)
    root.mainloop()
