import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        vegies = {0: "Bean", 1: "Bitter Gourd", 2: "Bottle Gourd", 3: "Brinjal", 4: "Broccoli", 5: "Cabbage",
                  6: "Capsicum", 7: "Carrot", 8: "Cauliflower", 9: "Cucumber", 10: "Papaya", 11: "Potato", 12: "Pumpkin", 13: "Radish", 14: "Tomato"}

        if result[0] in vegies:
            prediction = vegies[result[0]]
            return [{"image": prediction}]
        else:
            return "Not Found"
