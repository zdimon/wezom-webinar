## Make a virtual environment
    mkdir backend
    cd backend 
    virtualenv -p python3 venv
    . ./venv/bin/activate

Small tip. Rewrite the cd func in the .bashrc file to activate VO automatically.

    cd () {
        builtin cd ${1:+"$@"} 
        if [ -d "venv" ]
    then
        source ./venv/bin/activate
        fi  
    }    

## Requirements.

    Django
