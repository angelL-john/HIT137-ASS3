import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

# Base class for any Image-related features
class ImageProcessor:
    def load_image(self, path):
        raise NotImplementedError("Subclass must implement this method")

    def process_image(self):
        raise NotImplementedError("Subclass must implement this method")


# Inherit from ImageProcessor to handle face detection (Encapsulation)
class FaceDetector(ImageProcessor):
    
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Method overriding (from ImageProcessor)
    def load_image(self, path):
        self.image = cv2.imread(path)
        return self.image

    # Method overriding (from ImageProcessor)
    def process_image(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return self.image

# Main Application GUI
class ImageRecognitionApp(tk.Tk, FaceDetector):  # Multiple Inheritance
    def __init__(self):
        super().__init__()  # Polymorphism
        self.title("Facial Recognition App")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        # Decorators for button click method (Multiple Decorators)
     #   @self._button_click_decorator_1
        def load_image():
            file_path = filedialog.askopenfilename()
            if file_path:
                image = self.load_image(file_path)  # Polymorphism (method from FaceDetector)
                processed_image = self.process_image()  # Polymorphism
                self.display_image(processed_image)

        self.load_button = tk.Button(self, text="Load Image", command=load_image)
        self.load_button.pack()

        self.image_label = tk.Label(self)
        self.image_label.pack()

    def display_image(self, cv2_image):
        # Convert the image to RGB mode
        cv_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image)
        imgtk = ImageTk.PhotoImage(image=pil_image)
        self.image_label.imgtk = imgtk
        self.image_label.configure(image=imgtk)

    # Example of a decorator
    def _button_click_decorator_1(func):
        def wrapper(*args, **kwargs):
            print("Decorator 1: Before the button click")
            result = func(*args, **kwargs)
            print("Decorator 1: After the button click")
            return result
        return wrapper


# Entry point for application
if __name__ == "__main__":
    app = ImageRecognitionApp()
    app.mainloop()