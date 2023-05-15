pip3 instal pandas
pip3 install numpy
python3 combine.py

# # metabase operations

# going to metabase folder
cd ./metabase

# check if metabase.jar is present, if not download it
if [ ! -f metabase.jar ]; then
    wget https://downloads.metabase.com/v0.46.0/metabase.jar
fi

# run metabase
java -jar metabase.jar