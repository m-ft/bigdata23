# Big-Data-Group-23

The second assignment consists of the construction of a predictive model.

The data set describes features of laptops. For each laptop, the prices were followed daily over a three week time span, leading to a minimum ("min_price") and maximum ("max_price") for each laptop.
The data is attached to this item. Note that a train set and test set are provided. The test set does not contain the outcomes, so you will need to split up the train set accordingly into your own validation and test set. The test set provided here is to rank and assess your outcomes on the competition leaderboard (see below).
Your task is to construct a predictive model which can predict these prices ranges. Note that this setting is harder than simply predicting the price of a laptop, as we're also interested to get a prediction towards the future in terms of which models will be discounted or will go up, i.e. the price variability over three weeks.
Instructions:

The goal is to construct a predictive model to predict the min-max price range of a given laptop
Your model needs to be build using R or Python. As an environment, you can use e.g. Jupyter (Notebook or Lab), RStudio, Google Colaboratory, Microsoft Azure Machine Learning Studio, ...
The second part of your lab report should contain a clear overview of your whole modeling pipeline, including approach, exploratory analysis (if any), preprocessing, construction of model, set-up of validation and results of the model:

Feel free to use code fragments, tables, visualisations, ...
You can use any predictive technique/approach you want. The focus is not on the absolute outcome, but rather on the whole process: general setup, critical thinking, and the ability to get and validate an outcome
Take care of: performing a thorough validation, selecting an appropriate metric, thinking about your model setup (multiple ways to predict the two targets is possible), featurization (there are a lot of textual features)
You're free to use unsupervised technique for your data exploration part, too. When you decide to build a black box model, you're free to experiment and include ideas regarding making the result more understandable
Any other assumptions or insights are thoughts can be included as well: the idea is to take what we've seen in class, get your hands dirty and reflect on what we've seen
Important: All groups should submit the results of their predictive model at least once to the leaderboard

See: http://seppe.net/aa/assignment2/ to submit your predictions to the leaderboard
An e-mail with a password will be mailed to the group members
The goal is not to "win", but to help you reflect on your model's results, seeing how others are doing, ...
The leaderboard is based on the mean summed average error measure. The results of your latest submission are used to rank.
This means it is your job to keep track of different model versions / approaches / outputs in case you'd like to go back to an earlier result
The public leaderboard calculates your score for a predetermined set 50% of the instances in the test set
Later on, the leaderboard will be frozen (you'll be warned in advance) and the other 50% results (hidden leaderboard) will be shown
You should then reflect on both results and explain accordingly in your report. E.g. if you did well on the public leaderboard but not on the hidden one, what might have caused this?
Also take some time the reflect on the score measure being used here. Is the the measure you'd have chosen in this setting?

#username: 23
#password: vvcfgvfr
