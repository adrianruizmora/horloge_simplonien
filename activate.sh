# variable d'environnement sous unix
# pour specifier comment charger l'application
export FLASK_APP=run.py 

# facultatif pour le debug 
# peut être enlevé au moment du deployment 
export FLASK_ENV=1

# démarrer le microframework
flask run --port 8080