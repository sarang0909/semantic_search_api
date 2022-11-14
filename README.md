# semantic_search_api   
 
[streamlit_video_semantic_search.webm](https://user-images.githubusercontent.com/31824267/201714751-e68686c8-c144-4ce0-b914-217b2365db90.webm)

## About  
This is a project developed to create a code template and to understand semantic search techniques using elasticsearch. 
I've used news articles as search space,you can easily replace this with you requirement,any knowledge base like project documents,enterprise documents,web data etc.  

## Flow    
1.Create and store embeddings of knowledge base(79 news articles) using sentence transformer and elasticsearch.  
2.When user typen in a query then convert input query to embedding query and compare with knowledge base vectors using cosine similarity.    
3.Return top 5 similar results along with news article text and it's URL.     

### NLP and MLOps techniques to learn/use from this end to end project:
1. collect,clean text data   
2. implement search engine         
3. build inference api   
4. create streamlit application    
5. write unit test cases and performance test cases
6. code documentation
7. code formatting 
8. code deployment using docker and circleci


The basic code template for this project is derived from my another repo <a href="https://github.com/sarang0909/Code_Template">code template</a> 

The project considers following phases in ML project development lifecycle:  
Requirement    
Data Collection   
Search Engine Building   
Inference   
Testing     
Deployment   

We have not considered model evaluation and monitoring.   


### Requirement

Create a semantic search engine where user can search from knowledge base.For demo purpose,knowledge base can be kept small.    

### Data Collection   

News article data is collected by refering my another repo <a href="https://github.com/sarang0909/news_api">news api</a>. 

 Please note that since this is just a demo project,we have not used huge data. We have used only 79 news articles.  

### Search Engine Building   
 
Input vectors used : word embeddings from sentence transformer

Search techniques used : cosine similarity of input query and knowledge base vectors using <a href="https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/overview.html">elasticsearch</a>.               

  


### Inference   
There are 2 ways to deploy this application.   
1. API using FastAPI.
2. Streamlit application

### Testing     
Unit test cases are written   

### Deployment 
Deployment is done locally using docker.   


## Code Oraganization   
Like any production code,this code is organized in following way:   
1. Keep all Requirement gathering documents in docs folder.       
2. Keep Data Collection and exploration notebooks  in src/training folder.  data_collection.ipynb
3. Keep datasets in data folder.    
Raw data kept in raw_data csv.
Cleaned paragraphs stored in paragraph_clean_data.csv    
4. Keep model building notebooks at src/training folder.      
5. Write and keep inference code in src/inference.   
7. Write Logging and configuration code in src/utility.      
8. Write unit test cases in tests folder.<a href="https://docs.pytest.org/en/7.1.x/">pytest</a>,<a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">pytest-cov</a>    
9. Write performance test cases in tests folder.<a href="https://locust.io/">locust</a>     
10. Build docker image.<a href="https://www.docker.com/">Docker</a>  
11. Use and configure code formatter.<a href="https://black.readthedocs.io/en/stable/">black</a>     
12. Use and configure code linter.<a href="https://pylint.pycqa.org/en/latest/">pylint</a>     
13. Use Circle Ci for CI/CD.<a href="https://circleci.com/developer">Circlci</a>    
 
Clone this repo locally and add/update/delete as per your requirement.   
Since we have used different design patterns like singleton,factory.It is easy to add/remove model to this code. You can remove code files for all models except the model which you want to keep as a final.   
Please note that this template is in no way complete or the best way for your project structure.   
This template is just to get you started quickly with almost all basic phases covered in creating production ready code.   

## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main.py 	    <- A main file to run API server.    
├── main_streamlit.py 	    <- A main file to run API server.  
├── src                     <- Source code files to be used by project.    
│       ├── inference 	        <- model output generator code   
│       ├── training 	        <- model training code  
│       ├── utility	        <- contains utility  and constant modules.   
├── logs                    <- log file path   
├── config                  <- config file path   
├── data              <- datasets files   
├── docs               <- documents from requirement,team collabaroation etc.   
├── tests               <- unit and performancetest cases files.   
│       ├── cov_html 	        <- Unit test cases coverage report    

## Installation
Development Environment used to create this project:  
Operating System: Windows 10 Home  

### Softwares
Anaconda:4.8.5  <a href="https://docs.anaconda.com/anaconda/install/windows/">Anaconda installation</a>   
 

### Python libraries:
Go to location of environment.yml file and run:  
```
conda env create -f environment.yml
```

 

## Usage
Here we have created ML inference on FastAPI server with dummy model output.

1. Go inside 'semantic_search_api' folder on command line.  
   Run:
  ``` 
      conda activate semantic_search_api  
      python main.py       
  ```
  Open 'http://localhost:5000/docs' in a browser.
![alt text](docs/fastapi_first.jpg?raw=true)
 
2. Or to start Streamlit application  
5. Run:
  ``` 
      conda activate semantic_search_api  
      streamlit run main_streamlit.py 
  ```  
![alt text](docs/streamlit_first.jpg?raw=true)
 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Open 2 terminals and start main application in one terminal  
  ``` 
      python main.py 
  ```

2. In second terminal,Go inside 'tests' folder on command line.
3. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'semantic_search_api' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'semantic_search_api' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'semantic_search_api' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d --name mycontainer -p 5000:5000 myimage         
  ```


### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.



## Note
1.You'll need to create news api key to get news data,so create and update api key in data_collection notebook.       


## Contributing
Please create a Pull request for any change. 

## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

