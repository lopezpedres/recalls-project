import logging

def configure_logging(app):
    #borramos todo en caso de que hayamos añadido algo
    del app.logger.handlers[:]
    #Volvemos a poner los loggers de fabrica
    loggers=[app.logger]

    handlers=[]

    console_handler=logging.StreamHandler()
    console_handler.setFormatter(verbose_formatter())
    console_handler.setLevel(logging.DEBUG)
    handlers.append(console_handler)

    for l in loggers:
        for h in handlers:
            l.addHandler(h)
        l.propagate=False
        l.setLevel(logging.INFO)

def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
