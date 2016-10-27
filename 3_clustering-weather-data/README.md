The clustering notebook performs Clustering on weather data. Each row contains readings from several sensors (pressure, temperature etc) and a timestamp. We want to group these samples into logical groups that have more things in common.

First we use the describe() function to generate a statistical summary of the dataset. We further clean the dataset by removing unnecessary columns and dropping (using dropna()) the rows which have missing values.

Next, 12 clusters are generated using features mentioned in variable 'featuresUsed'. The cluster centers are displayed. Finally, similar cluster centers are plotted based on thresholds on specific features (such as relative_humidity).
