from functools import wraps
import datetime
import os


def log_decorator(adress = 'logs.txt'):

    def log_decorator_1(old_f):
        # adress = 'logs/logs.txt'
        adress_list = adress[:(adress.rfind('/'))].split('/')

        @wraps(old_f)
        def new_f(*args, **kwargs):
            try:
                with open(adress, "r", encoding='utf-8') as f:
                    log_f = f.read()
            except:
                adress_1 = ''
                for folder in adress_list:
                    if adress_1 == '': adress_1 = folder
                    else: adress_1 += '/' + folder
                    if not os.path.isdir(adress_1): os.mkdir(adress_1)
                log_f = ''


            if log_f != '': log_f += '\n'

            log_f += datetime.datetime.now().strftime('%Y.%m.%d %H:%M') + '\n    Function name: ' + old_f.__name__
            if args: log_f += '\n    Args: ' + str(args)
            if kwargs: log_f += '\n    Kwargs: ' + str(kwargs)
            result = old_f(*args, **kwargs)
            log_f += '\n    Result: ' + str(result) + '\n'

            with open(adress, "w", encoding='utf-8') as f:
                f.write(log_f)
            return result

        return new_f

    return log_decorator_1