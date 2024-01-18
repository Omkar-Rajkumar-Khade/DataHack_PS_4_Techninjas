import tkinter as tk
from PIL import Image, ImageTk
import cv2
import pytesseract
import os

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # OpenCV setup
        self.camera = cv2.VideoCapture(0)
        self.current_page = 1
        self.pages_to_capture = 2  # Set the number of pages to capture
        self.captured_images = []

        # Canvas to display the camera preview
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Button to capture image
        self.capture_button = tk.Button(window, text="Capture Page", command=self.capture_page)
        self.capture_button.pack(pady=10)

        # Button to perform OCR on captured images
        self.ocr_button = tk.Button(window, text="Perform OCR", command=self.combine_and_ocr)
        self.ocr_button.pack(pady=10)

    def show_frame(self):
        # Read frame from the camera
        ret, frame = self.camera.read()

        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a PIL Image
        image = Image.fromarray(frame_rgb)

        # Convert the PIL Image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Update the canvas with the new PhotoImage
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.photo = photo

        # Schedule the next update
        self.window.after(10, self.show_frame)

    def capture_page(self):
        # Read frame from the camera
        ret, frame = self.camera.read()

        # Save the captured image
        image_path = f"captured_page_{self.current_page}.jpg"
        cv2.imwrite(image_path, frame)
        self.captured_images.append(image_path)

        # Increment the page counter
        self.current_page += 1

        # If all pages are captured, disable capture button
        if self.current_page > self.pages_to_capture:
            self.capture_button.config(state=tk.DISABLED)

    def combine_and_ocr(self):
        if not self.captured_images:
            print("No images captured.")
            return

        combined_text = ""
        for idx, image_path in enumerate(self.captured_images, start=0):
            # Perform OCR on the captured image
            text_result = self.perform_ocr(image_path)

            # Append OCR result to combined text
            combined_text += f"--- Page {idx} ---\n{text_result}\n\n"

        # Save combined OCR results to a single text file
        combined_file_path = "combined_ocr_results.txt"
        with open(combined_file_path, "w", encoding="utf-8") as combined_file:
            combined_file.write(combined_text)

        print(f"Combined OCR results saved to: {combined_file_path}")

    def perform_ocr(self, image_path):
        # Use Tesseract through pytesseract
        text = pytesseract.image_to_string(Image.open(image_path))
        return text

    def run(self):
        # Show the camera preview
        self.show_frame()

        # Run the Tkinter event loop
        self.window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root, "Document Scanner")
    app.run()
