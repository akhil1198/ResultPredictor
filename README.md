## An end-to-end Machine Learning Score Predictor Project
This is an end-to-end Machine Learning project which predicts the math score of students given different criteria and scores. It is accessible on http://resultgenerator-env.eba-hbg2tp66.us-east-2.elasticbeanstalk.com/predictdata, deployed using aws beanstalk and ci/cd using codepipeline. It is a modular project where every section is split into different modules. 

### Running the project on your Local Server
run `export PYTHONPATH=/Path/To/Your/Project` to set the pythonpath
Start the data ingestion by running the data_ingestion.py file. This will create the train, test and raw.csv. It will also start the data transformation, preprocess the data and train the model. 

Once the model is trained, we can go ahead and start our application. 
To start application, run the command python3 application.py to start the flask server. 
The site will run at localhost:5000/predictdata