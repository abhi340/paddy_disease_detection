import cv2
import numpy as np
import os
import random

def predict_paddy_disease(image_path):
    """
    In a real system, this would load a pre-trained model (CNN/SVM)
    and perform prediction.
    For this prototype, we'll simulate the process using basic image analysis.
    """
    try:
        # Using np.fromfile to handle potential non-ASCII characters in paths
        img_array = np.fromfile(image_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        if img is None:
            return "Error: Could not decode image", 0.0
            
        # Basic image processing simulation
        img_resized = cv2.resize(img, (224, 224))
        
        # Simulate some logic based on pixel values (very crude for prototype)
        avg_color = np.average(np.average(img_resized, axis=0), axis=0)
        
        diseases = ['Leaf Blast', 'Sheath Blight', 'Bacterial Blight', 'Brown Spot', 'Healthy']
        
        # In a real model, this would be: model.predict(img_resized)
        # For now, we'll pick based on 'color' features or just semi-randomly for the demo
        # Leaf Blast often has brown spots, Bacterial Blight has yellowing
        
        if avg_color[2] > avg_color[1] + 10: # More red/brown
            detected = 'Brown Spot'
        elif avg_color[1] > avg_color[2] + 10: # More green/yellow
            detected = 'Bacterial Blight'
        else:
            detected = random.choice(diseases)
            
        confidence = random.uniform(0.7, 0.98)
        
        return detected, confidence
        
    except Exception as e:
        return f"Prediction Error: {str(e)}", 0.0
