# FetchRewards Time Series Prediction Application

This Dockerized application allows you to predict the number of scanned receipts for a given month of 2022 based on 2021 data. The application utilizes a time series model to make predictions.

![Capture](https://github.com/sushantmenon1/Time-Series/assets/74258021/e5341c98-0516-403c-b1da-ce5cbf9959b1)

## Prerequisites
Before running the application, make sure you have Docker installed on your system. If you haven't installed Docker yet, you can download and install it from [Docker's official website](https://www.docker.com/get-started).

## How to Run the Application
Follow these steps to run the application on your local machine:

1. **Pull the Docker Image:**
   Open your terminal or command prompt and execute the following command to pull the Docker image from Docker Hub:
   ```bash
   docker pull sushantmenon1/fetchrewards:v1.0
   ```

4. **Run the Application:**
After pulling the image, run the Docker container using the following command:
```bash
docker run -p 8080:8051 sushantmenon1/fetchrewards:v1.0
```

6. **Access the Application:**
Once the container is running, you can access the Streamlit server by opening your web browser and navigating to
```bash
http://localhost:8080
```

## Application Usage
- Upon accessing the application, you will be able to input the necessary parameters (such as number of days or any specific month) to get predictions for the number of scanned receipts in 2022.
- The application will utilize the SARIMAX time series model to generate predictions based on the input data from 2021.

Feel free to explore the application and adjust the input parameters to see different predictions for the scanned receipts in 2022.

Enjoy predicting the scanned receipts for 2022 using the FetchRewards Time Series Prediction Application!
