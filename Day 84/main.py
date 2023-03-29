import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


class WatermarkGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Add Watermark to Image")

        self.image_path = tk.StringVar()
        self.logo_path = tk.StringVar()
        self.text = tk.StringVar()
        self.font_size = tk.IntVar()
        self.opacity = tk.DoubleVar()

        # Create input widgets
        tk.Label(self.master, text="Select an Image:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.image_path).grid(row=0, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_image).grid(row=0, column=2)

        tk.Label(self.master, text="Select a Logo:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.logo_path).grid(row=1, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_logo).grid(row=1, column=2)

        tk.Label(self.master, text="Text to Add:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.master, textvariable=self.text).grid(row=2, column=1)

        tk.Label(self.master, text="Font Size:").grid(row=3, column=0, sticky="w")
        tk.Scale(self.master, from_=8, to=36, variable=self.font_size, orient="horizontal").grid(row=3, column=1)

        tk.Label(self.master, text="Opacity:").grid(row=4, column=0, sticky="w")
        tk.Scale(self.master, from_=0.0, to=1.0, resolution=0.1, variable=self.opacity, orient="horizontal").grid(row=4, column=1)

        tk.Button(self.master, text="Add Watermark", command=self.add_watermark).grid(row=5, column=1)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image_path.set(file_path)

    def browse_logo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.logo_path.set(file_path)

    def add_watermark(self):
        # Load image and logo
        image = Image.open(self.image_path.get())
        logo = Image.open(self.logo_path.get())

        # Resize logo to fit image
        logo_width, logo_height = logo.size
        image_width, image_height = image.size
        scale_factor = min(image_width / logo_width, image_height / logo_height)
        new_width = int(logo_width * scale_factor)
        new_height = int(logo_height * scale_factor)
        logo = logo.resize((new_width, new_height))

        # Add logo and text to image
        watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))
        watermark.paste(image, (0, 0))
        watermark.paste(logo, ((image_width - new_width) // 2, (image_height - new_height) // 2), mask=logo)
        draw = ImageDraw.Draw(watermark)

        # Add text to image
        text = self.text.get()
        font_size = self.font_size.get()
        opacity = int(self.opacity.get() * 255)
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(text, font)
        text_x = (image_width - text_width) // 2
        text_y = (image_height - text_height) // 2
        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255, opacity))

        # Merge watermark and image
        result = Image.alpha_composite(image.convert("RGBA"), watermark)

        # Save result
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
        if file_path:
            result.save(file_path)
