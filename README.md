# team_83

Placeholder github repo for our project pending when we recieve our team page

## create a pull request

1. clone the repo using `git clone https://github.com/idimmusix/team_8`

2. open your terminal and cd into team_8 using `cd team_8`

3. create a new branch with your username using `git checkout -b <your-username>`
   _please replace your-username with the user name you are using on slack_

4. Then add it to my github using `git remote add upstream https://github.com/idimmusix/team_8`

5. add a file <your-username>.txt

6. push it back to github using `git push -u origin <your-username>`

## configure the project for local machine

1. Create a virtual environment and activate `python -m venv env`
   - To activate in windows powershell `env\Scripts\activate.ps1`
   - To activate in command prompt (cmd) `env\Scripts\activate`
   - To activate in bash `source env/Scripts/activate`
     NB: If you use any other name to replace "env" above, add it to your .gitignore file
2. upgrade pip using `pip install --upgrade pip`
3. install the dependencies using `pip install -r requirements.txt`
4. cd into the project folder `cd fetch_metadata`
5. run `python manage.py runserver`
