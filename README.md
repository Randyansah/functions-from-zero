# functions-from-zero
#functions-from-zero
A repo to learn functions

## Step1: Configure Development Environment
* COnfigure Github codespaces or the equivalent(Cloud9, etc)
* Create scaffold for structure or projects
* Optional(setup virtualenv) (install ipython outside of rewuirements.txt))

  
[![Python application test with Github Actions](https://github.com/Randyansah/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/Randyansah/functions-from-zero/actions/workflows/main.yml)

### To call Microservice

something like this
```bash
curl -X 'POST' \
  'https://crispy-pancake-gr6979rgqjgf94r9-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```
### Build container
'docker build .'
'docker image ls'

### Run container
something like this
'docker run -p 127.0.0.0.1:8080:8080 01168e511c4b '

### Invoke POST REQUEST
run 'invoke.sh'
