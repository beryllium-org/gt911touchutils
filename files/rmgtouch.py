rename_process("rmgtouch")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
if not ("h" in vr("opts")["o"] or "help" in vr("opts")["o"]):
    if len(vr("opts")["w"]):
        vr("devt", vr("opts")["w"][0])
        if vr("devt").startswith("/dev/gtouch"):
            be.based.run("rmnod " + vr("devt")[5:])
            be.api.setvar("return", "0")
        else:
            term.write("Error: Invalid device!")
    else:
        term.write("Error: No device node specified!")
else:
    term.write("Usage:\n    rmgtouch /dev/gtouchX\n")
    be.api.setvar("return", "0")
