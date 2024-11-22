rename_process("mkgtouch")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
if not ("h" in vr("opts")["o"] or "help" in vr("opts")["o"]):
    vr("i2c", 0)
    if "i2c" in vr("opts")["o"]:
        vr("i2ct", vr("opts")["o"]["i2c"])
        if vr("i2ct") is not None and vr("i2ct").startswith("/dev/i2c"):
            try:
                vr("i2c", int(vr("i2ct")[8:]))
            except:
                term.write("Error: Invalid I2C bus!")
        else:
            term.write("Error: Invalid I2C bus!")
    vr("addr", 93)
    if "addr" in vr("opts")["o"]:
        try:
            vr("addr", int(vr("opts")["o"]["addr"]))
        except:
            pass
    vr("intr", None)
        try:
            vr("intr", be.devices["gpiochip"][0].input(vr("opts")["o"]["intr"]))
        except:
            pass
    try:
        vr("i2c", be.devices["i2c"][vr("i2c")])
        if not vr("i2c").try_lock():
            raise RuntimeError("I2C bus in use")
        vr("i2c").unlock()
        be.based.run("mknod gtouch")
        vr("node", be.api.getvar("return"))
        be.api.subscript("/bin/stringproccessing/devid.py")
        try:
            from gt911 import GT911
            be.devices["gtouch"][vr("dev_id")] = GT911(vr("i2c"), i2c_address=vr("addr"), int_pin=vr("intr"))
            del GT911
            be.api.setvar("return", "0")
            dmtex("gtouch device registered at /dev/gtouch" + str(vr("dev_id")))
        except:
            term.write("Could not init touch!")
    except:
        term.write("Error: Invalid I2C bus!")
else:
    term.write("Usage:\n    mkgtouch --i2c /dev/i2cX --addr I2C_ADDRESS --intr INTERRUPT_PIN\n")
    be.api.setvar("return", "0")
