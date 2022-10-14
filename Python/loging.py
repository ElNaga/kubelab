import logging  

# Levels - logging!

# CRITICAL 50

# ERROR 40

# WARNING 30

# INFO 20

# DEBUG 10

# NOTSET 0

logging.basicConfig(level=0)
logging.warning('This is a Warning!')


def decoration_sum(func):
    def wrapperFunc():
        logging.info('This si decor for addition')

        
        func()

        logging.info('This is end of decoration')
    return wrapperFunc

@decoration_sum
def addition(): 
    a = input('Input a value\n')
    b = input('Put b value\n')
    sum = int(a) + int(b)
    logging.info('one line here')   
    return print(sum)



addition()

logging.basicConfig(filename='./app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
