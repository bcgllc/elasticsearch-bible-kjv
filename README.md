elasticsearch-bible-kjv
=======================

The Holy Bible (KJV) for Elasticsearch

This project is 100% free to use.

The purpose of this project is to be able to search for any word or string in the KJV Bible using backend Elasticsearch engine with Kibana frontend.

The Kibana dashboard interface has been pre-configured to present upon search the results by:
- Total Hits
- Testament
- Book
- Chapter
- Verse
- Top 60 Near Words
- Up to 300 documents can be navigated

* Knowledge of how to setup and use Elasticsearch Server, Kibana, and Apache (HTTPD) is required. Install instructions can be provided if needed.
* Word 2007 or greater is required if you wish to use the XLSX files.

The project comes with the following files:
1. Python script (kjv.py)
2. Kibana script (kibana-kjv.json)
3. CSV files for each book of the Bible (created from XLSX files)
4. XLSX files for each book of the Bible

In order to run the Python script kjv.py, Elasticsearch for Python must be installed using the following command:
pip install elasticsearch

Only Python version 2.7 has been tested.

* An index must be created in Elasticsearch instance before import script is run. Create an index called 'bible'.
If you wish to use another name for the index go ahead, just make sure you update the python script where "index_name = bible".

To import the CSV files into your Elasticsearch instance, run this command:
python kjv.py


