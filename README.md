# Azur
Little github osint tool 


# How use it 
```
python3 main.py -u <github username>
```
else 
```
python main.py -u <github username>
```

# Package 
```
pip install requests
pip install colorama
pip install argparse
```

# How Azur work ?
He use the link of the commit with a .patch like this :
```
https://github.com/<username>/<repo name>/commit/<sha>.patch
```
