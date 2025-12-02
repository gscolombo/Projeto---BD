#! /bin/bash

read -p "Insira o nome do banco de dados: " db
read -p "Insira o nome de usuário: " username
read -sp "Insira a senha do usuário: " password

PGPASSWORD=$password psql -d $db -U $username -c "\i sql/drop_db.sql"
PGPASSWORD=$password psql -d $db -U $username -c "\i sql/create_db.sql"
PGPASSWORD=$password psql -d $db -U $username -c "\i sql/populate_db.sql"


base_path=$(dirname "${BASH_SOURCE[0]}")

views_dir="$base_path/views"
procedures_dir="$base_path/procedures"

if [[ -d $views_dir ]]; then
    for file in "$views_dir"/*; do
        if [[ -f $file ]] && [[ $file == *.sql ]]; then 
            PGPASSWORD=$password psql -d $db -U $username -c "\i $file"
        fi
    done
fi

if [[ -d $procedures_dir ]]; then
    for file in "$procedures_dir"/*; do
        if [[ -f $file ]] && [[ $file == *.sql ]]; then 
            PGPASSWORD=$password psql -d $db -U $username -c "\i $file"
        fi
    done
fi