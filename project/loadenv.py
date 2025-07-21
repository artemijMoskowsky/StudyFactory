import dotenv, os

def load_env():
    env_path = os.path.abspath(os.path.join(__file__ + "/../../.env"))
    dotenv.load_dotenv(env_path)
    migrations_env = os.path.abspath(os.path.join(__file__ + "/../migrations"))
    if not os.path.exists(migrations_env):
        os.system(os.environ["DB_INIT"])
    
    os.system(os.environ["DB_MIGRATE"])
    os.system(os.environ["DB_UPGRADE"])