Scraping Tool

File Structure:
  1. dao   # Directory for DAO Classes
     1. storage.py # Abstract Class
          1. dbstorage.py # To store data into DB
          2. filestorage.py # To store Data into File       
  2. Model # Model classes
     1. product.py # Model class for storing product
     2. scrapeconfiguration #  RequestBody having two optional settings - No of pages and proxy   
  3. Service
     1. scraper.py # Actual Scraper Logic is written here
  4. Utility
     1. Notifier
        1. notifier.py # Abstract class
           1. terminalnotifier.py # To notify in terminal
     2. cache.py # Implemented Cache in this
     3. saveimage.py # To store images in file system
  5. Data # To store data
  6. authentication.py # Token Based Authentication
  7. main.py # scrape API is written here
  8. settings.py # Configuration file 
