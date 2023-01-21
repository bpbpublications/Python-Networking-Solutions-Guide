from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("commands.txt")

with open("info.yml") as r:
    data = safe_load(r)

print(template.render(data))
