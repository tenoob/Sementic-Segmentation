# Semantic-Segmentation

App url : https://tenoob-sementic-segmentation-main-0er9yr.streamlit.app/

## Project Goals:

- Develop a U-Net model to segment objects in Satellite images.
- Train the model on a Dubai dataset.
- Track and monitor training experiments using MLflow.
- Compare different model versions using DagsHub.- 
- Deploy the final model as a user-friendly Streamlit app.

## Technical Stack:

- Deep Learning Framework: TensorFlow
- Model Architecture: U-Net
- Training Environment: Google Colab
- Experiment Tracking: MLflow
- Model Versioning and Comparison: DagsHub
- Deployment Platform: Streamlit

## Performance
-  On an image of size (256,256,3) the model takes ~ 65ms to make a prediction
-  the same image of size (256,256,3) takes ~ 2 sec to give results when using StreamLit app

This project provides a starting point for using U-Net models for image segmentation with experiment tracking, model comparison, and deployment using Streamlit. Feel free to adapt and extend this codebase for your specific image segmentation tasks.
