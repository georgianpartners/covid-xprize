XPRIZE Pandemic Response Challenge
------------
## Added to Repo
There are two new folders `covid_xprize_pipeline` and `covid_xprize_pipeline_downstream_static_feats`
which are two pipelines for rnn models implemented in PyTorch lightening based on the original repo's
lstm baseline. 

You will need to install pytorch and pytorch lightning.

### Data
At a highlevel this baseline splits the covid data by country and incorporates static features that users can add.
Users need to provide a csv that has a column `GeoID` that corresponds to the different regions to predict. See
`covid_xprize_pipeline\data\toy_static_data.csv` for an example.
 
### Model 
The model trains (labels for loss function) on a metric calculated from 
case numbers and population (still not fully understood). There is always a context feature and an action features. The action feature 
corresponds to the prevention actions and the context feature is the metric from previous days.
For predictions it inverses the prediction back to case numbers.
Likewise during inference, each prediction is the input context feature for the next day's prediction.

### Running
To run the pipeline, just run the adapted notebook `predictor_robojudge.ipynb` in each respective folder.
The two folders differ in that `covid_xprize_pipeline_downstream_static_feats` includes static 
features at the end of rnn model. Meanwhile `covid_xprize_pipeline` adds static features to each timestep.
You can also change configurations of the experiment in `constants.py`


### Next steps
This model does not result in good performance when testing from Nov 16 to Dec 7.
It may be worthwhile to understand the unrolling mechanism of the rnn model and the specific
calculations of the metric from case numbers and population used as labels for training. 

--------



## Introduction
Welcome to the [XPRIZE Pandemic Response Challenge](https://xprize.org/pandemicresponse)! This repository contains what you need to get started in creating your submission for the
contest.

Within this repository you will find:
* Sample predictors and prescriptors provided by Cognizant, in the form of Jupyter notebooks and python scripts
* Sample implementations of the "predict" API and the "prescribe" API, which you will be required to implement 
as part of your submission
* Sample IP (Intervention Plan) data to test your submission

## Pre-requisites
To run the examples, you will need:
* A computer or cloud image running a recent version of OS X or Ubuntu (Using Microsoft Windows™ may be possible but
the XPRIZE team and Cognizant will be unable to support you.) 
* Your machine must have sufficient resources in terms of memory, CPU, and disk space to train machine learning models 
and run Python programs.
* An installed version of Python, version ≥ 3.6. To avoid dependency issues, we strongly recommend using a standard Python [virtual environment](https://docs.python.org/3/tutorial/venv.html) with `pip` for package management. The examples in this repo assume you are using such an environment.

Having registered for the contest, you should also have:
* A copy of the Competition Guidelines
* Access to the Support Slack channel
* A pre-initialized sandbox within the XPRIZE system

## Examples
Under the `covid_xprize/examples` directory you will find some examples of predictors and prescriptors that you can 
inspect to learn more about what you need to do:
* `predictors/linear` contains a simple linear model, using the 
[Lasso algorithm](https://en.wikipedia.org/wiki/Lasso_(statistics)).
* `predictors/lstm` contains a more sophisticated [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory) 
model for making predictions.
* `prescriptors/zero` contains a trivial prescriptor that always prescribes no interventions; 
`prescriptors/random` contains one that prescribes random interventions.
* `prescriptors/neat` contains code for training prescriptors with [NEAT](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies)
 
The instructions below assume that you are using a standard Python virtual environment, and `pip` for package 
management. Installations using other environments (such as `conda`) are outside the scope of these steps.

In order to run the examples locally:
1. Ensure your current working directory is the root folder of this repository (the same directory as this README 
resides in). The examples assume your working directory is set to the project root and all paths are relative to 
it.
1. Ensure your `PYTHONPATH` includes your current directory:
    ```shell script
    export PYTHONPATH="$(pwd):$PYTHONPATH"
    ```
1. Create a Python [virtual environment](https://docs.python.org/3/tutorial/venv.html)
1. Activate the virtual environment
1. Install the necessary requirements:
    ```shell script
    pip install -r requirements.txt --upgrade
    ```    
1. Start Jupyter services:
    ```shell script
    jupyter notebook
    ```
    This causes a browser window to launch
1.  Browse to and launch one of the examples (such as `linear`) and run through the steps in the associated 
notebook -- in the case of `linear`, `Example-Train-Linear-Rollout-Model.ipynb`.
1. The result should be a trained predictor, and some predictions generated by running the predictor on test data. 
Details are in the notebooks.

## XPRIZE sandbox
Upon [registering for the contest](https://xprize.org/pandemicresponse), you will have been given access to a "sandbox", 
a virtual area within the XPRIZE cloud within which you can submit your work. 

### Submitting a predictor

In order for the automated judging process to detect and evaluate your submission, you **must** follow the 
instructions below. If your script does not conform to the API in any way, your submission will be omitted from 
judging.

1. Within your sandbox, under your home directory you will find a pre-created `work` directory.
1. Under this `work` directory, you must provide a Python script with the name `predict.py`. Examples of such scripts 
are provided in this repository. This script will invoke your predictor model and save the predictions produced.
1. Your script must accept particular command line parameters, and generate a particular output, as explained below. 
1. Whatever models and other data files your predictor requires must be uploaded to your sandbox and visible to your 
`predict.py` script, for example, by placing them in the `work` directory or subdirectories thereof.
1. Expect that the current working directory will be your sandbox `work` directory when your script is called. Therefore, 
references to other modules and resource files should be relative to that.
1. Expect your script to be called as follows (the dates and filenames are just examples and will vary):
    ```shell script
    python predict.py --start_date 2020-12-01 --end_date 2020-12-31 --interventions_plan ip_file.csv 
      --output_file 2020-12-01_2020_12_31.csv 
    ```
1. It is the responsibility of your script to run your predictor for the dates requested 
(between `start_date` and `end_date` inclusive) and generate predictions in the path and file specified by 
`output_file`, using the provided intervention plan. Take careful note of the performance and timing requirements 
in the Competition Guidelines for running your predictor. 

For more details on this API, consult the Competition Guidelines or the support Slack channel.

### Submitting a prescriptor

In order for the automated judging process to detect and evaluate your submission, you **must** follow the 
instructions below. If your script does not conform to the API in any way, your submission will be omitted from 
judging.

1. Within your sandbox, under your home directory you will find a pre-created `work` directory.
1. Under this `work` directory, you must provide a Python script with the name `prescribe.py`. Examples of such scripts 
are provided in this archive. This script will invoke your prescriptions model and save the prescriptions produced.
1. Your script must accept particular command line parameters, and generate a particular output, as explained below. 
1. Whatever models and other data files your prescriptor requires must be uploaded to your sandbox and visible to your 
`prescribe.py` script, for example, by placing them in the `work` directory or subdirectories thereof.
1. Expect that the current working directory will be your sandbox `work` directory when your script is called. Therefore, 
references to other modules and resource files should be relative to that.
1. Expect your script to be called as follows (the dates and filenames are just examples and will vary):
    ```shell script
    python prescribe.py --start_date 2020-12-01 --end_date 2020-12-31 --interventions_past ip_file.csv 
      --output_file 2020-12-01_2020_12_31.csv 
    ```
1. It is the responsibility of your script to run your prescriptor for the dates requested 
(between `start_date` and `end_date` inclusive) and generate prescriptions in the path and file specified by 
`output_file`. Take careful note of the performance and timing requirements 
in the Competition Guidelines for running your prescriptor. 

Example prescriptors can be found under `covid_xprize/examples/prescriptors/`.

For more details on this API, consult the Competition Guidelines or the support Slack channel.


#### Sample trained predictor

The repo also provides a sample trained predictor to train prescriptors against.
To use it, copy `covid_xprize/examples/predictors/lstm/tests/fixtures/trained_model_weights_for_tests.h5` 
to `covid_xprize/examples/predictors/lstm/models/trained_model_weights.h5`,
and call `covid_xprize/examples/predictors/lstm/predict.py` to make predictions.
See `get_predictions` in `covid_xprize/examples/prescriptors/neat/utils.py` and
`generate_cases_and_stringency_for_prescriptions` in `prescriptor_robojudge.ipynb` for examples of how to make 
this call.


## More information/Support
For more information and support, refer to the [competition guidelines](](https://xprize.org/pandemicresponse)) 
or post your questions in the support Slack channel; you should have gained access to both of these when you created a 
login in the competition platform.

For a concrete visualization of what the competition is about, see Cognizant's 
[COVID-19 intervention optimization demo](https://evolution.ml/demos/npidashboard/). Using this dashboard you can 
select among different prescriptors from the Pareto Front to see the effect on prescriptions for intervention plans 
in various regions.

For more background information please see also the research paper 
[From Prediction to Prescription: Evolutionary Optimization of Non-Pharmaceutical Interventions in the COVID-19 Pandemic](https://arxiv.org/abs/2005.13766). 

Copyright 2020 (c) Cognizant Digital Business, Evolutionary AI. All rights reserved. Issued under the Apache 2.0 License.
