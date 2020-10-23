### Using aws cli to make a lambda function

All the command line commands:     
<img width="682" alt="nano trust-policy.json" src="https://user-images.githubusercontent.com/38410965/96945870-e131cd80-14ac-11eb-9a42-7d5aeb5c2b37.png">

- [x] step 01: create policy:
     - `touch trust-policy.json`
     - `nano trust-policy.json`
<img width="682" alt="aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json" src="https://user-images.githubusercontent.com/38410965/96945884-eb53cc00-14ac-11eb-9e5b-a7d6943de11f.png">

- [x] step 02: create role:
     - `aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json`
<img width="682" alt="lambda-ex3" src="https://user-images.githubusercontent.com/38410965/96945890-f0b11680-14ac-11eb-9001-56c3f6d77161.png">

- [x] step 03: attach policy to role:
     - `aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole`
- [x] step 04: author the lamnda_function in python and zip it up:
     - `touch lambda_function.py`
     - `nano lambda_function.py`
     - `zip function.zip lambda_function.py`
<img width="682" alt="lambda-ex4" src="https://user-images.githubusercontent.com/38410965/96945902-f575ca80-14ac-11eb-9290-e8734ff5873f.png">
<img width="682" alt="lambda-ex5" src="https://user-images.githubusercontent.com/38410965/96945924-feff3280-14ac-11eb-9a8b-c23d6950afc1.png">
- [x] step 05: obtaining my user arn for the next step:
     - `aws iam get-user`
<img width="682" alt="lambda-ex6" src="https://user-images.githubusercontent.com/38410965/96945935-08889a80-14ad-11eb-9214-f5fde902a38d.png">
- [x] step 06: create the lambda function:
     - `aws lambda create-function --function-name my-function --zip-file fileb://function.zip --handler lambda_function.lambda_handler --runtime python3.8 --role arn:aws:iam::606363841935:role/lambda-ex`
            - `--handler is the python module name without .py suffix concatenated to the defined function's name inside 'lambda_function.lambda_handler'`
            - `--role is the arn obtained in step 5`
<img width="682" alt="lambda-ex7" src="https://user-images.githubusercontent.com/38410965/96945943-0de5e500-14ad-11eb-8e96-618d667cc53c.png">


<img width="682" alt="lambda-ex8" src="https://user-images.githubusercontent.com/38410965/96945960-13432f80-14ad-11eb-8ff4-9d9bcb216a9d.png">
