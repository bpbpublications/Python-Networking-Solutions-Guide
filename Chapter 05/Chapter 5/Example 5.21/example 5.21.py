from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("commands.txt")

with open("info.yml") as r:
    data = safe_load(r)

with open("conf.txt","w") as w:
    w.write(template.render(data))

connect = InitNornir()
result = connect.run(task=netmiko_send_config, config_file="conf.txt")
print_result(result)
