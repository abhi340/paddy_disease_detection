# Paddy Disease Detection System using Machine Learning

A comprehensive Django-based web application designed to help farmers identify and manage rice crop diseases through AI-powered image analysis and environmental data integration.

## 🌾 Project Overview
Paddy crop diseases can lead to substantial yield loss and impact the livelihoods of millions. This system provides an automated, real-time solution for early disease identification, focusing on the most destructive types:
- **Leaf Blast** (*Pyricularia oryzae*)
- **Sheath Blight** (*Rhizoctonia solani*)
- **Bacterial Blight** (*Xanthomonas oryzae*)
- **Brown Spot** (*Cochliobolus miyabeanus*)

## ✨ Key Features
- **AI-Powered Detection:** High-resolution image analysis using Convolutional Neural Networks (CNN) and OpenCV.
- **Environmental Integration:** Analyzes images alongside real-time data such as **Temperature**, **Humidity**, and **Location** for more accurate results.
- **Admin Authorization:** Secure user management system where administrators must authorize new registrations before they can access the detection tools.
- **Social Connectivity:** Features for searching other farmers and sending/receiving friend requests to build a supportive agricultural community.
- **Responsive UI:** Modern, minimalist interface with a **Glassmorphism** aesthetic, optimized for both desktop and mobile devices.

## 🛠️ Technical Stack
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3 (Glassmorphism), Bootstrap 5, JavaScript
- **Machine Learning:** OpenCV, NumPy, Scikit-learn (TensorFlow ready)
- **Database:** SQLite (ACID compliant)

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Pip (Python Package Manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/abhi340/paddy_disease_detection.git
   cd paddy_disease_detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create an admin account:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure
- `paddy_app/`: Main application logic, views, and models.
- `paddy_app/utils.py`: Image processing and disease prediction logic.
- `media/`: Storage for uploaded paddy images for analysis.
- `templates/`: Professional Glassmorphism UI components.

## 📝 License
This project is developed for educational purposes as part of the Final Year Project requirements.

---
*Note: This system is a prototype designed to demonstrate the potential of AI in agriculture. For critical agricultural decisions, always consult a certified professional.*
