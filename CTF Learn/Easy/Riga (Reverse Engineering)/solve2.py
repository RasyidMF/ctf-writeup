import angr
import claripy

base_addr = 0x100000

project = angr.Project("Riga", main_opts={'base_addr': base_addr})
args    = claripy.BVS('flag', 30 * 8)

# target  = 0x1194 # IDA
target  = 0x00101194 # Ghidra

state = project.factory.entry_state(args=["./Riga", args])
simum = project.factory.simulation_manager(state)

print(simum.explore(find = target))

print("SIMUM : " + str(simum.found))
result = simum.found[0]

print(result.solver.eval(args, cast_to=bytes))