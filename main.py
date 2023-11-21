import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark App")

        # Variables
        self.image_path = tk.StringVar()
        self.watermark_text = tk.StringVar()

        # GUI components
        self.create_widgets()

    def create_widgets(self):
        # Image selection
        tk.Label(self.root, text="Select Image:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.image_path, state="readonly", width=40).grid(row=0, column=1, padx=5,
                                                                                           pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_image).grid(row=0, column=2, pady=5)

        # Watermark text input
        tk.Label(self.root, text="Watermark Text:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.watermark_text, width=40).grid(row=1, column=1, padx=5, pady=5)

        # Add Watermark button
        tk.Button(self.root, text="Add Watermark", command=self.add_watermark).grid(row=2, column=1, pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.image_path.set(file_path)




    def add_watermark(self):
        image_path = self.image_path.get()
        watermark_text = self.watermark_text.get()

        if not (image_path and watermark_text):
            tk.messagebox.showwarning("Warning", "Please select an image and enter watermark text.")
            return

        try:
            image = Image.open(image_path)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error opening image: {e}")
            return

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Load a font
        font = ImageFont.load_default()

        # Set the position for the watermark (you can adjust this based on your preference)
        text_position = (100, 100)

        # Set the color for the watermark (black in this case)
        text_color = (0, 0, 0)

        # Add the watermark text to the image
        draw.text(text_position, watermark_text, font=font, fill=text_color)

        # Save the watermarked image or display it
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            image.save(save_path)
            tk.messagebox.showinfo("Success", "Watermark added successfully!")
        else:
            image.show()






if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
