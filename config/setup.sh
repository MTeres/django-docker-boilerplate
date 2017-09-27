#!/bin/bash

declare file=$HOME"/.bash_profile"
declare regex="/usr/local/bin/virtualenvwrapper.sh"
declare file_content=$( cat "${file}" )
declare env="env_desafio"


if [[ " $file_content " =~ $regex ]]
    then
        echo "virtualenv wrapper instalado previamente"
    else
#        instalando virtualenvwrapper
        pip install --user virtualenvwrapper
#        Compiando arquivo para o local correto
        cp -v ./virtualenvwrapper.sh /usr/local/bin/virtualenvwrapper.sh
#        configurando
        echo export WORKON_HOME=$HOME/.virtualenvs >> $HOME"/.bash_profile"
        echo export PROJECT_HOME=$HOME/Devel >> $HOME"/.bash_profile"
        echo source /usr/local/bin/virtualenvwrapper.sh >> $HOME"/.bash_profile"
        echo "virtualenv wrapper instalado com sucesso!"
fi


