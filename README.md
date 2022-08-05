# Install 

postgresql

`sudo apt -y install postgresql; sudo -i -u postgres`

`sudo systemctl start postgresql.service`

or

`sudo service postgresql start`


`sudo -i -u postgres`


`psql`

`createdb fastapi_error;`

`ALTER USER postgres PASSWORD 'pass';`


`\q`

` exit`

`pip install --upgrade pip`


`pip install -r freeze.txt`

# run 
`uvicorn fastapi_service.main:app --reload --log-level debug --port 6007`



