### Where on Earth IDentifier Python API


This is an API for the getting the WOEID for city. 

> What is Where on Earth IDentifier?
> https://en.wikipedia.org/wiki/WOEID

This project is made possible by using the following:
* [Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model/)
* [SAM Local](https://github.com/awslabs/aws-sam-local)
* [YQL](https://developer.yahoo.com/yql/)

#### Code Structure
* README.md - this file
* buildspec.yml - This YAML file is used by AWS CodeBuild to create an artifact
  that can be used to deploy to AWS Lambda through CloudFormation.
* code/index.py - This file contains the AWS Lambda code used to interact with YQL to retrieve the WOEID for a city in a  country.
* events.json -  This file contains a sample of list of events that can be used to do local development using [sam-local](https://github.com/awslabs/aws-sam-local)
* template.yml - This YAML file is used by AWS CloudFormation to update AWS Lambda
  and manage any additional AWS resources.

#### API Doc
`GET /`
| Parameter  | Required  | Default  |
|---|---|---|---|---|
| city  | Yes  | n/a  |
| countryCode  | No  | 'US'  |


#### Development
1. Clone this repository
2. Install `sam-local` from steps [here](https://github.com/awslabs/aws-sam-local#installation)
3.
* To invoke an event use the `events.json`
```
sam local invoke GetWoeid --event events.json
```
* To start the API server
```
sam local start-api
```
Then go to http://localhost:3000/?city=Seattle&countryCode=US
