from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

connect = InitNornir()

result = connect.run(task=napalm_cli, commands=["write"])
print_result(result)
