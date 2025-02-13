import time
import fireducks.pandas as pd
import logging 
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
# CSV file path
CSV_FILE_PATH = '/Users/constah/Documents/dlight/datasets/Movies.csv'
def load_and_transform_data():
    logger.info("Starting load with Pandas...")
    start_time = time.time()  
    # Read the CSV file using Pandas
    df = pd.read_csv(CSV_FILE_PATH)
    read_time = time.time()
    logger.info(f"Time to read CSV with Pandas: {read_time - start_time:.2f} seconds") 
    # Filter the data
    filtered_df = df[(df['vote_count'] > 20000) & (df['status'] == 'Released')]
    filter_time = time.time()
    logger.info(f"Time to filter data with Pandas: {filter_time - read_time:.2f} seconds")
    logger.info(f"Number of records after filtering: {len(filtered_df)}")
    # Select the top 10 Movies by vote_average
    top_movies = filtered_df.sort_values(by='vote_average', ascending=False).head(10)
    top_time = time.time()   
    # Return the top 10 movies as a DataFrame
    logger.info(f"Time to execute with Pandas: {top_time - start_time:.2f} seconds")
    return top_movies

if __name__ == '__main__':
    top_10_movies = load_and_transform_data() 